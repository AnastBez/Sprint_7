import allure
import pytest
from methods.courier_methods_2 import CourierMethods, generate_random_string


class TestLoginCourier:

    @allure.title("Проверка, что курьер может авторизоваться и для авторизации нужно передать все обязательные поля;")
    def test_login_courier(self):
        login_pass = CourierMethods.register_new_courier_and_return_login_password()
        response_code, response_json = CourierMethods.login_courier(login_pass[0], login_pass[1])
        assert (response_code == 200 and 'id' in response_json)


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10))
        ]
)
@allure.title("Проверка, что система вернёт ошибку, если неправильно указать логин или пароль")
def test_login_courier_error_not_found(login, password, first_name):
    status_code_reg, status_json_reg = CourierMethods.register_new_courier(login, password, first_name)
    status_code_login, status_json_login = CourierMethods.login_courier(login, 'abcdere')

    assert (status_code_reg == 201 and 'ok' in status_json_reg and status_code_login == 404 and
            'Учетная запись не найдена' in status_json_login['message'])


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10))
        ]
)
@allure.title("Проверка если какого-то поля нет, запрос возвращает ошибку")
def test_login_courier_error_not_data(login, password, first_name):
    status_code_reg, status_json_reg = CourierMethods.register_new_courier(login, password, first_name)
    status_code_login, status_json_login = CourierMethods.login_courier(login, '')

    assert (status_code_reg == 201 and 'ok' in status_json_reg and status_code_login == 400 and
    'Недостаточно данных для входа' in status_json_login['message'])


@pytest.mark.parametrize(
        'login, password',
        [
            ('111',
             '111')
        ]
)
@allure.title("Проверка если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
def test_login_not_exist_courier(login, password):
    status_code_login, status_json_login = CourierMethods.login_courier(login, password)

    assert status_code_login == 404 and 'Учетная запись не найдена' in status_json_login['message']


@pytest.mark.parametrize(
        'login, password, first_name',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10))
        ]
)
@allure.title("Проверка, что успешный запрос возвращает id")
def test_login_courier_id(login, password, first_name):
    status_code_reg, status_json_reg = CourierMethods.register_new_courier(login, password, first_name)
    status_code_login, status_json_login = CourierMethods.login_courier(login, password)
    assert status_code_reg == 201 and 'id' in status_json_login
