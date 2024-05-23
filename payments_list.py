from yookassa import Configuration, Payment
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.domain.response.payment_list_response import PaymentListResponse

from constants import SHOP_ID, SECRET_KEY

Configuration.account_id = SHOP_ID
Configuration.secret_key = SECRET_KEY


'''Данные одного платежа'''
payment_id = '2ddf0352-000f-5000-9000-1197f79bf990'
payment: PaymentResponse = Payment.find_one(payment_id)
print(payment.status)


'''Список всех платежей'''
filter_params = {
    'status': 'pending',
    'limit': 2,
    "payment_method_data": "bank_card"
}
res: PaymentListResponse = Payment.list(filter_params)
for payment in res.items:
    print('\n_________________')
    print(payment.id)
    print(payment.created_at)
    print(payment.captured_at)
    print(payment.recipient)
    print(payment.status)
    print(payment.paid)