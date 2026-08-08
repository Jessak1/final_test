# Нефедьев Евгений, 45-я когорта — Финальный проект. Инженер по тестированию плюс
from orders_api import get_order_by_track
 
 
class TestOrderTrack:
 
    def test_get_order_by_track(self, order_track):
        get_response = get_order_by_track(order_track)
        assert get_response.status_code == 200, (
            f"Не удалось получить заказ по треку {order_track}, "
            f"код ответа: {get_response.status_code}, "
            f"тело ответа: {get_response.text}"
        )