from uuid import uuid4
import json

from yookassa import Configuration, Payment
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.domain.response.payment_list_response import PaymentListResponse

from constants import SHOP_ID, SECRET_KEY, CONFIRMATION_URL

Configuration.account_id = SHOP_ID
Configuration.secret_key = SECRET_KEY


# создание платежа
payment: PaymentResponse = Payment.create(
    {
        "amount": {
            "value": "100.00",
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": CONFIRMATION_URL
        },
        "capture": True,
        "description": "Заказ №1"
    },
    uuid4()  # ключ идемпонентности
)


# создается платеж со статусом pending
print(payment.id)
print(payment.confirmation.confirmation_url)

# нужно сделать редирект пользователя на payment.confirmation.confirmation_url для оплаты

# после оплаты пользователем статус изменится на waiting_for_capture (или сразу на succeeded)
# его нужно подтвердить за определенное время, иначе статус изменится на canceled и деньги вернутся пользователю