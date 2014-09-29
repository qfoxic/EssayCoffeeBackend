from payments.models import Payment
from general.models import Task
from django.http import HttpResponse
from django.views.generic import View
import json
import constants as co
from django.views.decorators.csrf import csrf_exempt

def lds(values):
    try:
      return json.loads(values)
    except (TypeError, ValueError):
      return {}


def _two_checkout_payment(request):
  pst = request.POST
  order_id = pst.get('vendor_order_id')
  order = Task.objects.all().filter(id=order_id)
  order = order and order[0]
  if order:
    vals = {'sale_id': request.POST.get('sale_id'),
            'customer_ip': request.POST.get('customer_ip'),
            'amount': request.POST.get('invoice_usd_amount')}
    payment = Payment(powner=order.owner, ptask=order,
                      values=json.dumps(vals), payment_status=co.IN_PROCESS,
                      payment_type=co.TWOCHECKOUT)
    payment.save()


@csrf_exempt
def two_checkout_payment_notification(request):
  _two_checkout_payment(request)
  return HttpResponse('Thanks, Accepted.')


def update_payment_status(ptype, task, request, data=None):
  data = data or {}
  status = co.IN_PROCESS
  if ptype == co.LIQPAY:
    from liqpay.liqpay import LiqPay
    liq = LiqPay(co.LIQ_PUB_KEY, co.LIQ_PRIV_KEY)
    liq = liq.api("payment/status", {"order_id": task.id})
    try:
      values = json.dumps(liq)
    except:
      values = '{}'
    if liq.get('result') == 'ok' and liq.get('status') in ['success', 'sandbox']:
      fraud = float(task.get_price()) - float(liq.get('amount', 0.00)) > 0.03
      status = co.PAID
      if fraud:
        status = co.UNDERPAID
  elif ptype == co.TWOCHECKOUT:
    import twocheckout
    # mode: production, mode:sandbox
    twocheckout.Api.auth_credentials({'private_key': co.TWO_PRIV_KEY,
                                      'seller_id': co.TWOSID,'mode': 'sandbox'})
    twocheckout.Api.credentials({'username': co.TWO_USERNAME,
                                 'password': co.TWO_PASSWORD,'mode': 'sandbox'})
    sale_id = data.get('sale_id')
    try:
      sale_status = twocheckout.Sale.find({'sale_id': sale_id})['invoices'][0]['status']
      amount = twocheckout.Sale.find({'sale_id': sale_id})['invoices'][0]['usd_total']
    except (twocheckout.error.TwocheckoutError, KeyError, IndexError):
      return
    if sale_status in ['deposited']:
      fraud = float(task.get_price()) - float(amount) > 0.03
      status = co.PAID
      if fraud:
        status = co.UNDERPAID
      payment = Payment(powner=task.owner, ptask=task,
                        values=json.dumps(data), payment_status=status,
                        payment_type=ptype)
      payment.save()


def get_payments_status():
  sql = ('SELECT max(id) as id, powner_id, ptask_id,'
         ' SUBSTRING_INDEX(GROUP_CONCAT(`payment_status` ORDER BY `Id` DESC SEPARATOR \',\'),\',\',1)'
         ' as status, payment_type, '
         'SUBSTRING_INDEX(GROUP_CONCAT(`values` order by `Id` desc separator \'|\'),\'|\',1) as ovalues'
         ' FROM payments GROUP BY ptask_id')
  _d = {}
  [_d.setdefault(int(i.ptask_id),
             [
               co.PAYMENT_STATUS_DICT.get(int(i.status)),
               int(i.status),
               i.powner_id,
               int(i.payment_type),
               lds(i.ovalues)
             ],
             ) for i in Payment.objects.raw(sql)]
  return _d


def get_payment_url(ptype, request, params):
  """Params: price, title, order_id"""
  if ptype == co.TWOCHECKOUT:
    params['sid'] = co.TWOSID
    params['currency_code'] = 'USD'
    return ('https://www.2checkout.com/checkout/purchase/?sid=%(sid)s&mode=2CO&'
            'li_0_type=product&li_0_name=%(title)s&li_0_quantity=1&li_0_tangible=N&currency_code=%(currency_code)s&'
            'li_0_description=%(title)s&li_0_product_id=%(order_id)s&merchant_order_id=%(order_id)s&li_0_price=%(price)s' % params)
  elif ptype == co.LIQPAY:
    params['mode'] = 1#To disable test mode use 0
    params['callback_url'] = request.get_host()
    params['pub'] = co.LIQ_PUB_KEY
    params['currency'] = 'UAH'#'USD'
    params['price'] = '0.1'#Remove this
    return ('https://www.liqpay.com/api/pay?public_key=%(pub)s&amount=%(price)s'
            '&currency=%(currency)s&description=%(title)s&type=buy&sandbox=%(mode)s&pay_way'
            '=card&server_url=%(callback_url)s&order_id=%(order_id)s&language=en' % params)
