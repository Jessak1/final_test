import pytest

from orders_api import create_order


@pytest.fixture
def order_track():
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    response = create_order(order_data)
    assert response.status_code == 201, (
        f"Не удалось создать заказ, код ответа: {response.status_code}, "
        f"тело ответа: {response.text}"
    )
    return response.json()["track"]