# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import platform
import subprocess


with open('ip_list.txt', 'r') as file:
	ip_list=file.read().rstrip().split('\n') #записываем адреса из файла в список
#print (ip_list)


print_template='''
Доступные адреса:
{}

Недоступные адреса:
{}

'''

def ping(host):

	'''Функция проверяет адрес на доступность (ping), если доступно возвращает True
	в зависимости от платформы подтсавляет нужный ключ'''
	param = '-n' if platform.system()=='Windows' else '-c' #проверка платформы для определения ключа
	shell_needed = True if platform.system()=='Windows' else False #проверка плотформы для определения необходимости в shell
	ping_command = ['ping', param, '1', host] # запись команды пинга
	
	ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE, encoding="utf_8", errors='ignore')
	
	#Проверяем есть ли TTL в выводе команды ping:
	return True if 'TTL' in ping_output.stdout else False

#print(ping('127.0.0.1'))


def check_ip_addresses(ip_list):
	'''Функция ожидает как аргумент список IP-адресов.
		И возвращает два списка:
		* список доступных IP-адресов
		* список недоступных IP-адресов'''
	available_ip=[]
	not_available_ip=[]
	#Проверка на доступность адреса:
	for ip in ip_list:
		if ping(ip) == True:
			available_ip.append(ip)
		else:
			not_available_ip.append(ip)
	return available_ip, not_available_ip


if __name__ == "__main__":
	available, not_available = check_ip_addresses(ip_list)


	print(print_template.format(available, not_available))



