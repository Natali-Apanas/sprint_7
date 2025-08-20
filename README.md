# qa_python_7_sprint

Проект 7 спринта, тестирование [API](https://qa-scooter.praktikum-services.ru/docs/) учебного сервиса [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/) с помощью библиотеки [Requests](https://requests.readthedocs.io/en/latest/) и с сохранением результатов тестирования в Allure-отчёт. Структура проекта:

- `allure_report/` - каталог с отчетом о тестировании
- `tests/` - каталог с тестами
- `tests/test_create_courier.py` - файл с проверками создания курьерского аккаунта
- `tests/test_get_order_list.py` - файл с проверкой получения списка заказов
- `tests/test_login_courier.py` - файл с проверками входа в курьерский аккаунт
- `tests/test_make_order.py` - файл с проверками создания нового заказа
- `conftest.py` - файл с фикстурами
- `data.py` - вспомогательные данные для тестирования
- `generators.py` - файл с функциями для генерации фейковых данных (логины, пароли и т.д.)
- `urls.py` - файл с константами URL

Список тестов был подробно описан в финальном задании 7 спринта.

Все необходимые для запуска зависимости перечислены в `requirements.txt`. Перед запуском тестов рекомендуется создать виртуальное окружение:

```bash
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

Затем установить зависимости:

```bash
pip install -r requirements.txt
```

Теперь тесты готовы к запуску. Запуск одного конкретного теста:

```bash
pytest .\tests\test_create_courier.py::TestCreateNewCourier
```

Запуск всех тестов в одном конкретном файле:

```bash
pytest .\tests\test_create_courier.py
```

Запуск тестов сразу во всех файлах с сохранением резльтатов в отчёт Allure:

```bash
pytest . --alluredir=allure_report
```

Просмотр отчёта в веб версии Allure:

```bash
allure serve allure_report
```
