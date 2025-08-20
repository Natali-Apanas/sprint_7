import allure
import requests
from data import Flags
from urls import urls


class TestOrderList:
    @allure.title('Тест получения списка заказов. Эндпоинт: /api/v1/orders')
    def test_successful_get_order_list(self):
        with allure.step('Отправка GET-запроса для получения списка заказов'):
            response = requests.get(urls.get_order_list)
        assert response.status_code == 200
        assert Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()
