import allure
import pytest
import requests
import generators
from urls import urls


@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()

    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}

    with allure.step('Создание тестового курьера'):
        requests.post(urls.create_courier, json=create_courier_body)

    login_response = requests.post(urls.courier_login, json=login_courier_body)
    login_json = login_response.json()
    courier_id = login_json.get('id')

    yield {
        'create_body': create_courier_body,
        'login_body': login_courier_body,
        'login': login,
        'password': password,
        'courier_id': courier_id,
        'login_response': login_response
    }

    with allure.step('Удаление тестового курьера'):
        if courier_id:
            requests.delete(urls.courier_delete + str(courier_id))


@pytest.fixture
def courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}

    yield [creation_courier_body, login_courier_body]

    with allure.step('Очистка созданного курьера'):
        login_response = requests.post(urls.courier_login, json=login_courier_body)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            requests.delete(urls.courier_delete + str(courier_id))


@pytest.fixture
def create_and_cancel_order():
    orders = []
    yield orders
    for track in orders:
        with allure.step(f'Отмена заказа с треком {track}'):
            requests.put(urls.order_cancel + str(track))
