import pytest
from methods.courier_methods_2 import CourierMethods

@pytest.fixture()
def courier():
    login_pass = CourierMethods.register_new_courier_and_return_login_password()
    response_code, response_json = CourierMethods.login_courier(login_pass[0], login_pass[1])
    yield response_json['id']
    CourierMethods.delete_courier(response_json['id'])
    #тут дописать удаление



