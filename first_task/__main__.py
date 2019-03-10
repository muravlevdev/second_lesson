"""Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
    данных.
    В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
    соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
    os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
    поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
    «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
    каждого файла);
    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
    через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
    Проверить работу программы через вызов функции write_to_csv()."""

import csv
import re

files = ['first_task/info_1.txt', 'first_task/info_2.txt', 'first_task/info_3.txt']


def get_data(file_names):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    # Ищем нужные строки и заполняем ими списки
    for file in file_names:
        with open(file) as txt_file:
            strings = txt_file.readlines()
            for i in strings:
                if re.search(r'Изготовитель системы:', i):
                    os_prod_list.append(i.replace(r'Изготовитель системы:', '').strip())
                if re.search(r'Название ОС:', i):
                    os_name_list.append(i.replace(r'Название ОС:', '').strip())
                if re.search(r'Код продукта:', i):
                    os_code_list.append(i.replace(r'Код продукта:', '').strip())
                if re.search(r'Тип системы:', i):
                    os_type_list.append(i.replace(r'Тип системы:', '').strip())

    # Заполняем отчёт
    for i in range(len(os_prod_list)):
        a = []
        a.append(os_prod_list[i])
        a.append(os_name_list[i])
        a.append(os_code_list[i])
        a.append(os_type_list[i])
        main_data.append(a)

    return main_data


def write_to_csv(csv_link, result):
    with open(csv_link, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(result)


if __name__ == '__main__':
    write_to_csv('first_task/report.csv', get_data(files))
