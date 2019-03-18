# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
import ipaddress
import platform
import subprocess
from tabulate import tabulate
from task_12_1 import ping, check_ip_addresses
from task_12_2 import check_ip_availability
from itertools import zip_longest # позволяет зиповать списки не по кратчайшему, а по длиннейшему из зипуемых объектов


with open('adress_list.txt', 'r') as file:
	adress_list=file.read().rstrip().split('\n') #записываем адреса из файла в список


ip_list=check_ip_availability(adress_list)
available, not_available = check_ip_addresses(ip_list)

def ip_table(available, not_available):
	'''Функция ожидает как аргументы два списка:
		* список доступных IP-адресов
		* список недоступных IP-адресов

		Результат работы функции - вывод на стандартный поток вывода таблицы вида:

		Reachable    Unreachable
		-----------  -------------
		10.1.1.1     10.1.1.7
		10.1.1.2     10.1.1.8
					 10.1.1.9
	'''
	zip_list=list(zip_longest(available, not_available, fillvalue='')) # сливаем два списка в один список по парам- доступный-не доступный-не
	return zip_list

zip_list=ip_table(available, not_available)
	
columns=['Доступные IP:', 'Недоступные IP:']
print(tabulate(zip_list, headers=columns))


