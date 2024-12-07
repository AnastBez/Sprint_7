class Urls:
    URL = 'https://qa-scooter.praktikum-services.ru'


class Endpoint:
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    CREATE_ORDER = '/api/v1/orders/'
    ORDER_LIST = '/api/v1/orders?limit=10&page=0'


class Testdata:
    TEST_ORDER = {"firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": 4,
                  "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06",
                  "comment": "Saske, come back to Konoha"}
