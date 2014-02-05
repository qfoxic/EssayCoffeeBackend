import lib.yaml as yaml, re, os.path

def merge(d1, d2):
  """Function merge two dictionary into one and retun merged dictionary.
  NOTE!!! It doesn't overload existing data but just extend them.

  d1 - dictinary that will be populated with d2.
  """
  keys1 = set(d1)
  common_keys = keys1.intersection(set(d2))
  for key in common_keys:
    d2_tmp = d2.pop(key)
    if isinstance(d1[key], list):
      d1[key].extend(d2_tmp)
    elif isinstance(d1[key], dict):
      merge(d1[key], d2_tmp)

  d1.update(d2)
  return d1

def fload(module_path):
  file = module_path + '/config/settings.yml'

  if os.path.exists(file):
    general_config = open(file, 'r')
  else:
    print 'Module Config file [%s] not found' % file
    return None
  
  try:  
    general_settings = yaml.load(general_config.read())
  except yaml.YAMLError, e:
    print 'Yaml parse error: %s' % (str(e))
    return {}
  return general_settings
  
def load(request, module_path):
  """Looks for settings.yml in local module's directory and
       ../config/settings.yml in the root directory, in addition load data
       from database and merge all settings into one dictionary.
       In case of errors also return empty dictionary.

       uid - user id the db settings belong to. NB!!! Function doesn't check 
              the presence of the user.
       module_path = the name of the module that was requested.
       request - this is actually Http request.

      Usage:
        settings = load() or
        settings = load()
  """
  settings_dict = {}
  files = [module_path + '/config/settings.yml', 'config/settings.yml','general/config/settings.yml']
  settings = {} 
  #extract current module name(?) and action from request
  res = filter(None,re.split('/',request.path))

  # If action exists then it will have second position in the res list
  # otherwise the IndexError will be raised - it means that there is no action.
  try:
    # We must cast from unicode to string to avoid error in dispatch method.
    command = str(res[1])
  except IndexError:
    command = 'index'
  # module name
  try:
    # We must cast from unicode to string to avoid error in dispatch method.
    appname = str(res[0])
  except IndexError:
    appname = 'dashboard'
  # Read main config.
  if os.path.exists(files[1]):
    main_config = open(files[1], 'r')
  else:
    print 'Main Config file [%s] not found' % files[1]
    main_config = None

  # Read module's config.
  if os.path.exists(files[0]):
    module_config = open(files[0], 'r')
  else:
    print 'Module Config file [%s] not found' % files[0]
    module_config = None
  
  # Read general module config.
  if os.path.exists(files[2]):
    general_config = open(files[2], 'r')
  else:
    print 'Module Config file [%s] not found' % files[2]
    general_config = None

  # Read all configs and parse them.
  general_settings = main_settings = module_settings = {}
  try:
    if main_config:
      main_settings = yaml.load(main_config.read())
    if module_config:
      module_settings = yaml.load(module_config.read())
    if general_config:
      general_settings = yaml.load(general_config.read())
  except yaml.YAMLError, e:
    print 'Yaml parse error: %s' % (str(e))
    return {}
    
  # We assume the main_settings are in global section by default.
  main_settings.update({'app': {'name':appname,'action':command, }}) 
  main_settings.update( general_settings )  
  main_dict = main_settings
  
  # And, in addition, we merge our main dict only with module settings that
  # contains current action section + global section.
  module_current_section_dict = merge (module_settings.get('global', {}),module_settings.get(command, {}) )
  static_settings = merge(main_dict, module_current_section_dict)
  
  return static_settings
