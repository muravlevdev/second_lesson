# -*- coding: utf8 -*-
"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена
(price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""

import json


def set_order():
    order_info = {}
    order_info['item'] = input('Введите товар: ')
    order_info['quantity'] = input('Введите количество: ')
    order_info['price'] = input('Введите цену: ')
    order_info['buyer'] = input('Введите покупателя: ')
    order_info['date'] = input('Введите дату: ')
    return order_info


def write_order_to_json(order):
    with open('second_task/orders.json', 'r', encoding='utf-8') as file:
        orders_data = json.load(file)
    with open('second_task/orders.json', 'w', encoding='utf-8') as file:
        orders_data['orders'].append(order)
        json.dump(orders_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    write_order_to_json(set_order())