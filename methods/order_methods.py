import requests
from data import *
import random
from methods.courier_methods_2 import generate_random_string
import json


def random_order_dictionary():
    dictionary = {}
    for key in ['firstName', 'lastName', 'address', 'metroStation', 'phone', 'deliveryDate', 'comment']:
        dictionary[key] = generate_random_string(10)
    dictionary['rentTime'] = random.randint(1, 100)
    return dictionary


class OrderMethods:
    @staticmethod
    def create_order(dictionary):

        response = requests.post(f'{Urls.URL}{Endpoint.CREATE_ORDER}', data=json.dumps(dictionary))
        return response.status_code, response.json()

    @staticmethod
    def take_order_list():
        response = requests.get(f'{Urls.URL}{Endpoint.ORDER_LIST}')
        return response.status_code, response.json()
