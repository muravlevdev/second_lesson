# -*- coding: utf8 -*-
"""3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными."""

import yaml

json_data = {'first': ['раз', 'два', 'три'],
             'second': 5,
             'third': {'key1': '1€', 'key2': '2€'}
             }


def write_data_to_yaml(data):
    with open('third_task/data.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(data, file, indent=4, allow_unicode=True, default_flow_style=False)


def read_yaml():
    with open('third_task/data.yaml', 'r', encoding='utf-8') as file:
        print(yaml.load(file))


if __name__ == '__main__':
    write_data_to_yaml(json_data)
    read_yaml()
