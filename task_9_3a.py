'''
Дополнить скрипт:

добавить поддержку конфигурации, когда настройка access-порта выглядит так:
interface FastEthernet0/20
  switchport mode access
  duplex auto
То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

Пример словаря:

{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/20':1 }
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
'''


def get_int_vlan_map(filename):

	'''обработка файла, разделение на транковые и не транковые порты,
	вывод в два словаря
	'''
	
	with open(filename) as sw:

		vlan_int={}
		trunk_int={}
		
		for line in sw:
			
			if 'FastEthernet' in line:				# Ищем строку с номером интерфейса
				*n, nameint = line.split()
				vlan_int[nameint] = 1				## Ставим по умолчанию всем интерфейсам vlan1
			elif 'access vlan' in line:				#Определяем тип порта как access
				vlan = line.split()[-1]
				vlan_int[nameint] = int(vlan)		# Присваиваем номер влана ключу с именем интерфейса
			elif 'allowed vlan' in line:			#определяем тип порта как транковый
				vlan = line.split()[-1]				#выделяем последний элемент строки, там где номера вланов
				vlan = vlan.split(',')				#переводим в список
				vlan = [int(item) for item in vlan]	#переводим в int
				trunk_int[nameint] = vlan
				del(vlan_int[nameint])				## в случае если порт транковый удаляем ключ-значение из вланов по умолчанию
				
	
	return(print(vlan_int), print(trunk_int))
	
get_int_vlan_map('config_sw2.txt')