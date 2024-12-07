import pytest
from methods import order_methods
from data import Testdata
import allure


class TestCreateOrder:

    @pytest.mark.parametrize(
        'color', [
            (['BLACK']),
            (['GREY']),
            (['GREY', 'BLACK']),
            ([''])
            ]
        )
    @allure.title("Проверка,что можно указать один из цветов — BLACK или GREY, можно указать оба цвета,"
                  "можно совсем не указывать цвет и тело ответа содержит track.")
    def test_create_order(self, color):
        dictionary = Testdata.TEST_ORDER
        dictionary['color'] = color
        status_code, status_json = order_methods.OrderMethods.create_order(dictionary)
        assert status_code == 201 and 'track' in status_json
