import allure
import pytest
import requests
import generators
from data import ResponseBody
from urls import urls


class TestLoginCourier:
    @allure.title('Тест успешного входа курьера. Эндпоинт: /api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        with allure.step('Отправка POST-запроса для входа курьера'):
            response = requests.post(urls.courier_login, json=create_courier['login_body'])

        login_json = response.json()
        assert response.status_code == 200
        assert (
            ('id' in login_json and isinstance(login_json['id'], str) and len(login_json['id']) > 0),
            f"Некорректный ID: {login_json.get('id')}"
        )


    @allure.title('Тест входа с незарегистрированной учетной записью')
    def test_unregistered_courier_login(self):
        login_data = {
            'login': generators.login_generator(),
            'password': generators.password_generator()
        }
        with allure.step('Отправка POST-запроса с незарегистрированными данными'):
            response = requests.post(urls.courier_login, json=login_data)

        assert response.status_code == 404
        assert response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND


    @allure.title('Тест входа с пустым полем: {empty_field}')
    @pytest.mark.parametrize('empty_field, login, password', [
        ('login', '', 'correct_password'),
        ('password', 'correct_login', '')
    ])
    def test_courier_empty_field_error(self, empty_field, login, password):
        payload = {
            'login': login,
            'password': password
        }

        with allure.step(f'Отправка POST-запроса с пустым полем: {empty_field}'):
            response = requests.post(urls.courier_login, json=payload)

        assert response.status_code == 400
        assert response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA
