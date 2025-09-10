import allure
import pytest
import requests
from data import DataForOrder, Flags
from urls import urls


class TestCreationOrder:
    @allure.title('Успешное создание заказа с цветом: {scooter_color}')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_colors)
    def test_create_with_dif_colors(self, create_and_cancel_order, scooter_color):
        order_data = DataForOrder.order_data.copy()
        order_data['color'] = scooter_color

        with allure.step('Отправка POST-запроса на создание заказа'):
            response = requests.post(urls.create_order, json=order_data)

        assert response.status_code == 201
        assert Flags.SUCCESSFUL_ORDER_CREATION in response.json()

        track = response.json()['track']
        create_and_cancel_order.append(track)
