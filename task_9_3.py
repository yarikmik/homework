'''
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:

словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
 {'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17]}
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(filename):

	'''обработка файла, разделение на транковые и не транковые порты'''
	sw_print=[]
	with open(filename) as sw:
		for line in sw:
			line=line.strip()
			line=line.strip('! ') # убираем символы пробела и !
			if line=='':		# Пропускаем пустые строки
				continue
			else:
				sw_print.append(line)
	vlan_int={}
	trunk_int={}
	
	
	for line in sw_print:
		if 'FastEthernet' in line:
			
	
	
	
	
	
	
	return(sw_print)
	
print ('\n'.join(get_int_vlan_map('config_sw1.txt')))