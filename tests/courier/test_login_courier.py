import response
import allure
import pytest
from methods import courier_methods_2
import requests


class TestLoginCourier:

    @allure.title("Проверка, что курьер может авторизоваться и для авторизации нужно передать все обязательные поля;")
    def test_login_courier(self, courier):
        assert courier > 0


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10))
        ]
)
@allure.title("Проверка, что система вернёт ошибку, если неправильно указать логин или пароль")
def test_login_courier_error_not_found(login, password, first_name):
    status_code_reg, status_json_reg = courier_methods_2.CourierMethods.register_new_courier(login, password,
                                                                                             first_name)
    status_code_login, status_json_login = courier_methods_2.CourierMethods.login_courier(login, 'abcdere')

    assert status_code_reg == 201 and status_code_login == 404


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10))
        ]
)
@allure.title("Проверка если какого-то поля нет, запрос возвращает ошибку")
def test_login_courier_error_not_data(login, password, first_name):
    status_code_reg, status_json_reg = courier_methods_2.CourierMethods.register_new_courier(login, password,
                                                                                             first_name)
    status_code_login, status_json_login = courier_methods_2.CourierMethods.login_courier(login, '')

    assert status_code_reg == 201 and status_code_login == 400


@pytest.mark.parametrize(
        'login, password',
        [
            ('111',
             '111')
        ]
)
@allure.title("Проверка если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
def test_login_not_exist_courier(login, password):
    status_code_login, status_json_login = courier_methods_2.CourierMethods.login_courier(login, password)

    assert status_code_login == 404


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10),
             courier_methods_2.generate_random_string(10))
        ]
)
@allure.title("Проверка, что успешный запрос возвращает id")
def test_login_courier_id(login, password, first_name):
    status_code_reg, status_json_reg = courier_methods_2.CourierMethods.register_new_courier(login, password,
                                                                                             first_name)
    status_code_login, status_json_login = courier_methods_2.CourierMethods.login_courier(login, password)
    assert status_code_reg == 201 and 'id' in status_json_login
