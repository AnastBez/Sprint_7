import pytest
import allure
from methods.courier_methods_2 import CourierMethods, generate_random_string


class TestCreateCourier:
    @allure.title("Проверка создания курьера, передача в ручку все обязательные поля")
    def test_pass_create_courier(self):
        login_pass = CourierMethods.register_new_courier_and_return_login_password()
        assert len(login_pass) > 0

    @pytest.mark.parametrize(
        'login, password, first_name',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10))
        ]
    )
    @allure.title("Проверка,что нельзя создать двух одинаковых курьеров")
    def test_similar_create_courier(self, login, password, first_name):
        status_code_1, status_json_1 = CourierMethods.register_new_courier(login, password, first_name)
        status_code_2, status_json_2 = CourierMethods.register_new_courier(login, password, first_name)
        assert (status_code_1 == 201 and status_json_1['ok'] and status_code_2 == 409 and
                "Этот логин уже используется" in status_json_2['message'])

    @pytest.mark.parametrize(
        'login, password, first_name',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10))
        ]
    )
    @allure.title('Проверка, что запрос возвращает правильный код ответа и успешный запрос возвращает {"ok":true}')
    def test_response(self, login, password, first_name):
        status_code, status_json = CourierMethods.register_new_courier(login, password, first_name)

        assert status_code == 201 and status_json['ok']

    @pytest.mark.parametrize(
        'login, password, first_name',
        [
            ('',
             generate_random_string(10),
             generate_random_string(10)),
            (generate_random_string(10),
             '',
             generate_random_string(10)),
        ]
    )
    @allure.title("Проверка если одного из полей нет, запрос возвращает ошибку")
    def test_not_all_fields(self, login, password, first_name):
        status_code, status_json = CourierMethods.register_new_courier(login, password, first_name)
        assert status_code == 400 and "Недостаточно данных для создания учетной записи" in status_json["message"]

    @pytest.mark.parametrize(
        'login, password_1, first_name_1, password_2, first_name_2',
        [
            (generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10),
             generate_random_string(10)
             )
        ]
    )

    @allure.title('Проверка если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_not_unique_login(self, login, password_1, first_name_1, password_2, first_name_2):
        status_code_1, status_json_1 = CourierMethods.register_new_courier(login, password_1, first_name_1)
        status_code_2, status_json_2 = CourierMethods.register_new_courier(login, password_2, first_name_2)
        assert (status_code_1 == 201 and status_json_1['ok'] and status_code_2 == 409 and
                "Этот логин уже используется" in status_json_2['message'])
