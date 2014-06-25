from payments.models import Payment
import json
import constants as co

#TODO. 1. Add payment_type to payments to all handlers. Just test.
# Update mysql dump in both projects.
# add get_payment_status.
# test update_payment_status.
def update_payment_status(ptype, task):
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
  payment = Payment(powner=task.owner, ptask=task,
                    values=values, payment_status=status, payment_type=ptype)
  payment.save()


def get_payments_status():
  sql = ('SELECT max(id) as id, powner_id, ptask_id,'
         ' SUBSTRING_INDEX(GROUP_CONCAT(`payment_status` ORDER BY `Id` DESC SEPARATOR \',\'),\',\',1)'
         ' as status, payment_type FROM payments GROUP BY ptask_id')
  _d = {}
  [_d.setdefault(int(i.ptask_id), [
             co.PAYMENT_STATUS_DICT.get(int(i.status)),
             int(i.status),
             i.powner_id,
             int(i.payment_type)]) for i in Payment.objects.raw(sql)]
  return _d

 
def get_payment_url(ptype, request, params):
  """Params: price, title, order_id"""
  if ptype == co.LIQPAY:
    params['mode'] = 1#To disable test mode use 0
    params['callback_url'] = request.get_host()
    params['pub'] = co.LIQ_PUB_KEY
    params['currency'] = 'UAH'#'USD'
    params['price'] = '0.1'#Remove this
    return ('https://www.liqpay.com/api/pay?public_key=%(pub)s&amount=%(price)s'
            '&currency=%(currency)s&description=%(title)s&type=buy&sandbox=%(mode)s&pay_way'
            '=card&server_url=%(callback_url)s&order_id=%(order_id)s&language=en' % params)
