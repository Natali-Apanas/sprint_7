import allure
import pytest
import requests
from data import ResponseBody, DataForRegistration
from urls import urls


class TestCreateNewCourier:
    @allure.title('Тест успешного создания нового курьера. Эндпоинт: /api/v1/courier')
    def test_creation_courier_success(self, courier_data):
        with allure.step('Отправка POST-запроса на создание курьера'):
            registration = requests.post(urls.create_courier, json=courier_data[0])

        assert registration.status_code == 201
        assert registration.json() == ResponseBody.COURIER_CREATION_SUCCESS


    @allure.title('Тест ошибки при повторной регистрации одного и того же курьера. Эндпоинт: /api/v1/courier')
    def test_creation_courier_error(self, create_courier):
        with allure.step('Отправка запроса на повторную регистрацию курьера'):
            response = requests.post(urls.create_courier, json=create_courier['create_body'])

        assert response.status_code == 409
        assert response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST


    @allure.title('Тест ошибки регистрации курьера, если данных для регистрации не достаточно. Эндпоинт: /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        with allure.step('Отправка запроса на регистрацию с неполными данными'):
            response = requests.post(urls.create_courier, json=data_setup)

        assert (
            response.status_code == 400,
            f'Ожидается статус 400 для данных: {data_setup}, получен {response.status_code}'
        )
        assert (
            response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA,
            f'Неожиданное тело ответа для данных: {data_setup}'
        )
