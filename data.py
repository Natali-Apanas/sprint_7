import generators


class DataForOrder:
    order_data = {
        'FirstName': 'Natali',
        'LastName': 'Apanasevich',
        'address': 'Minsk, Bulbash Land',
        'metroStation': 13,
        'phone': '+375331234567',
        'rentTime': 5,
        'deliveryDate': '2025-08-22',
        'comment': 'Пу-пу-пу...'
    }
    scooter_colors = [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ]


class DataForRegistration:
    reg_data = [
        {'password': generators.password_generator()},
        {'login': generators.login_generator()},
        {},
        {'login': '', 'password': generators.password_generator()},
        {'login': generators.login_generator(), 'password': ''}
    ]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {
        'ok': True
    }
    COURIER_NAME_ALREADY_EXIST = {
        'code': 409,
        'message': 'Этот логин уже используется. Попробуйте другой.'
    }
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {
        'code': 400,
        'message':'Недостаточно данных для создания учетной записи'
    }
    COURIER_ACCOUNT_NOT_FOUND = {
        'code': 404,
        'message':'Учетная запись не найдена'
    }
    COURIER_LOGIN_NOT_ENOUGH_DATA = {
        'code': 400,
        'message':'Недостаточно данных для входа'
    }


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'
