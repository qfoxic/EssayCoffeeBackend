# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from lib.confreader import load,fload
#from django.utils import simplejson as json
from django.http import HttpResponse
from django.conf import settings
from django.utils import translation

import socket, re, os, json

reg_b = re.compile(r"android.+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|"\
                   "fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|meego.+mobile|"\
                   "midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|"\
                   "pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|"\
                   "windows (ce|phone)|xda|xiino", re.I|re.M)
reg_v = re.compile(r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|"\
                   "ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|"\
                   "au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|"\
                   "bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|"\
                   "da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|"\
                   "em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|"\
                   "gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|"\
                   "hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|"\
                   "i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|"\
                   "iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|"\
                   "le(no|xi)|lg( g|\\/(k|l|u)|50|54|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|"\
                   "ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|"\
                   "mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|"\
                   "n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|"\
                   "nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|"\
                   "\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|"\
                   "qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|"\
                   "s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|"\
                   "sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|"\
                   "sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|"\
                   "tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|"\
                   "v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|"\
                   "w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\\-|your|zeto|zte\\-", re.I|re.M)

def check_mobile(request):
  if request.META.has_key('HTTP_USER_AGENT'):
    user_agent = request.META['HTTP_USER_AGENT']
    b = reg_b.search(user_agent)
    v = reg_v.search(user_agent[0:4])
    if b or v:
      return True

  return False

def send_api_call(json_data):
  """Make call to backend and retuns json string as response.
     json_data - python dictionary.
  """
  settings = fload('general')
  if not settings:
      return '{"error": "Unable to proceed request, general configuration [settings.yml] file is missed"}'
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Set timeout to 9 seconds.
  sock.settimeout(300)
  resp = ''
  try:
#    sock.connect(settings.BACKEND_ADDR)
    sock.connect((settings.get('cloud',{}).get('backend_addr','127.0.0.1'), settings.get('cloud',{}).get('backend_port',9991)))
    data_to_send = json_data + '\n'
    sock.send(data_to_send)
    while 1:
     data = sock.recv(4096)
     resp += data
     # The last symbol MUST be \n
     if data[-1] == '\n':
       break
  except Exception, e:
    sock.close()
    return '{"error": "api call was unsuccessful %s"}' % str(e)
  sock.close()
  return resp

    

class LoginView(TemplateView):
  def dispatch(self, request, *args, **kwargs):
    self.settings = load(request, kwargs.get('module_path','general'))

    if check_mobile(request):
      self.template_name = 'mobile/'+ self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    else:  
      self.template_name = self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    self.settings.update({'auth_error': request.auth_error})                     
    return login(request, self.template_name, extra_context = self.settings)
  

class BaseView(TemplateView):
  """Base class for all views. That class provide login page in case user 
  wasn't authorized. In addition,  it loads settings from "config/" 
  module's directory and then from database. User's limits and max available 
  limits are also provided by that class. Limits are accessible through 
  "limits" key, available limits - through "available_limits" key of 
  settings dictionary.
  """

#  @method_decorator(login_required(login_url="/login/"))
  def dispatch(self, request, *args, **kwargs):
    # Swap default request user with our updated.
    self.settings = load(request, kwargs.get('module_path','general'))
    self.settings['request'] = request
    return super(BaseView, self).dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    if check_mobile(self.request):
      self.template_name = 'mobile/'+ self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    else:  
      self.template_name = self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    return kwargs
  
  
  def json_to_response(self, content):
    """The content is JSON formatted string"""
    return HttpResponse(content, content_type='application/json')

class SudoView(BaseView):
  def get(self, *args, **kwargs):
    return HttpResponse("", content_type='application/json') 

  def post(self, *args, **kwargs):
    import copy
    user = self.request.session.get('_cloud_user_data')
    new_euid = self.request.POST.get('euid')
    if not (user or new_euid):
      return self.json_to_response('{"error": "Unable to sudo. Sorry"}')
    is_sudo = kwargs.get('is_sudo')
    if not int(user.rid) == int(new_euid):
      
      response = send_api_call('{"command": "user_data", "euid": "%s", "uid": "%s", "remote_addr": "%s", "lang": "%s"}' % (
                               user.rid, new_euid, self.request.META['REMOTE_ADDR'], self.request.LANGUAGE_CODE))
      response = json.loads(response)
      if response.get('error'):
        return self.json_to_response('{"error": "%s"}' % response.get('error'))

    if is_sudo: 
      #save original user to stack.
      user.stack.append(copy.copy(user))
      #change effective id.
      user.id = new_euid
      user.role = response['result']['role']
      user.pid = response['result']['pid']
      user.username = response['result']['username']
      user.first_name = response['result']['first_name']
      user.last_name = response['result']['last_name']
    else:
      _s = user.stack
      #check if user exists in stack during unsudo. 
      usr = filter(lambda x: int(x.id) == int(new_euid), _s)
      if not usr:
        return self.json_to_response('{"result": "Unsudo failed."}')
      #Remove all users from stack up to exiting one.
      map(_s.remove, _s[_s.index(usr[0]):])
      user.id = usr[0].id 
      user.role = usr[0].role 
      user.pid = usr[0].pid
      user.username = usr[0].username
      user.first_name = usr[0].first_name
      user.last_name = usr[0].last_name
      
    self.request.session['_cloud_user_data'] = user
    return self.json_to_response('{"result": "success"}')

class ResetView(TemplateView):
  def dispatch(self, request, *args, **kwargs):
    # Swap default request user with our updated.
    self.settings = load(request, kwargs.get('module_path','general'))
    self.settings['request'] = request
    if check_mobile(request):
      self.template_name = 'mobile/'+ self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    else:  
      self.template_name = self.settings['layout']['skin_prefix'] + '/' \
                         + self.template_name
    return super(ResetView, self).dispatch(request, *args, **kwargs)
    
  def post(self, *args, **kwargs):
    d = {"command": "user_resetpswd", "email": ""}
    d['email'] = self.request.POST.get('email') 
    d["remote_addr"] = self.request.META['REMOTE_ADDR']
    d['lang'] = self.request.LANGUAGE_CODE
    responce = send_api_call(json.dumps(d))
    resp = json.loads(responce)
    return HttpResponse(responce, content_type='application/json')

  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    return kwargs
      
class FileView(BaseView):
  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    self.template_name = self.settings['layout']['skin_prefix'] + '/' \
                         + kwargs['module'] + '/_%s' % kwargs['file']
    return kwargs    

class TipView(BaseView):
  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    lang = translation.get_language()
    real_path = os.path.join(settings.SITE_ROOT, 'templates', 'tips/%s/%s.html' % ( lang, kwargs['id'] ))
    if_not_path = os.path.join(settings.SITE_ROOT, 'templates', 'tips/en/%s.html' % kwargs['id'])
    
    if not os.path.exists(real_path):
      if not os.path.exists(if_not_path):
        self.template_name = 'tips/en/not_found.html'
      else:  
        self.template_name = 'tips/en/%s.html' % kwargs['id']
    else:
      self.template_name = 'tips/%s/%s.html' % ( lang, kwargs['id'] )
    return kwargs

class HelpView(BaseView):
  def get_context_data(self, **kwargs):
    kwargs.update(self.settings)
    lang = translation.get_language()
    if not kwargs['id']:
      kwargs['id'] = 'index'  
    real_path = os.path.join(settings.SITE_ROOT, 'templates', 'help/%s/%s.html' % ( lang, kwargs['id'] ))
    if_not_path = os.path.join(settings.SITE_ROOT, 'templates', 'help/en/%s.html' % kwargs['id'])
    
    if not os.path.exists(real_path):
      if not os.path.exists(if_not_path):
        self.template_name = 'help/en/not_found.html'
      else:  
        self.template_name = 'help/en/%s.html' % kwargs['id']
    else:
      self.template_name = 'help/%s/%s.html' % ( lang, kwargs['id'] )
    return kwargs
  
class ApiView(BaseView):
  def get(self, *args, **kwargs):
    return self.post(self, *args, **kwargs)

  def post(self, *args, **kwargs):
    #Required parameter for all api calls.
#    import pdb; pdb.set_trace()
    json_object = {'euid': self.request.user.id, 
                   'kid': self.settings['api']['kid'], 
                   'key': self.settings['api']['key']
                   }
    json_object.update(kwargs)

    if self.request.GET:
      json_object.update(self.request.GET)
    if self.request.POST:
      json_object.update(self.request.POST)

    # Django put all urls params into list, i.e.
    # api?param1=value become {param1: [value]}, however we need simply key:value.
    def parser(_key):
      key, value = _key[0], _key[1]
      if key.endswith("[]"):
        key = key.strip("[]")
        return key, ",".join(value)
      if isinstance(value, list):
        if len(value) == 1:
          return key, value[0]
      return key, value
    parsed_json_object = dict(map(parser, json_object.items()))
    parsed_json_object["remote_addr"] = self.request.META['REMOTE_ADDR']
    parsed_json_object["lang"] = self.request.LANGUAGE_CODE
    responce = send_api_call(json.dumps(parsed_json_object))
    return self.json_to_response(responce)

