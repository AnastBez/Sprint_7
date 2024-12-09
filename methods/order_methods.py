import requests
import allure
from data import *
import json


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(dictionary):

        response = requests.post(f'{Urls.URL}{Endpoint.CREATE_ORDER}', data=json.dumps(dictionary))
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Получение списка заказов")
    def take_order_list():
        response = requests.get(f'{Urls.URL}{Endpoint.ORDER_LIST}')
        return response.status_code, response.json()
