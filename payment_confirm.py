from uuid import uuid4

from yookassa import Configuration, Payment

from constants import SHOP_ID, SECRET_KEY

Configuration.account_id = SHOP_ID
Configuration.secret_key = SECRET_KEY

'''Подтверждение платежа'''
payment_id = '2ddef455-000f-5000-a000-1c972693cc22'
response = Payment.capture(
  payment_id,
  {
    "amount": {
      "value": "100.00",
      "currency": "RUB"
    }
  },
  uuid4()
)


payment_id = '2ddef455-000f-5000-a000-1c972693cc22'
payment = Payment.find_one(payment_id)
print(payment.__dict__)
