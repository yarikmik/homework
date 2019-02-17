# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
import ipaddress
import platform
import subprocess
from task_12_1 import ping, check_ip_addresses

with open('adress_list.txt', 'r') as file:
	adress_list=file.read().rstrip().split('\n') #записываем адреса из файла в список


def check_ip_availability(adress_list):
	list_ip=[] #лист, куда будут заносится значения ip
	for string in adress_list:
		if '-' in string:	# если в строке есть разделитель "-", значет это диапазон адресов
			range_ip = string.split('-')
			
			start_ip = ipaddress.IPv4Address(str(range_ip[0]))# начальный адрес
			end_ip = ipaddress.IPv4Address(str('.'.join(range_ip[0].split('.')[0:3]))+'.'+str(range_ip[1].split('.')[-1]))	# конечный адрес
			for ip_int in range(int(start_ip), int(end_ip)+1): # добавляем 1, т.к. последний адрес не включен в цикл
				list_ip.append(str(ipaddress.IPv4Address(ip_int)))
			
		else:
			list_ip.append(string)
	return list_ip

#print (check_ip_availability(adress_list))


print_template='''
Доступные адреса:
{}

Недоступные адреса:
{}

'''

ip_list=check_ip_availability(adress_list)

available, not_available = check_ip_addresses(ip_list)

print(print_template.format(available, not_available))



