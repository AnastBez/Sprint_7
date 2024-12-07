import pytest
from methods import order_methods
import allure


class TestOrderList:

    @allure.title("Проверка, что в тело ответа возвращается список заказов.")
    def test_order_list(self):
        status_code, status_json = order_methods.OrderMethods.take_order_list()
        assert status_code == 200 and len(status_json['orders']) > 0
