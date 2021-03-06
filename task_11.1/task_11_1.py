'''
\Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (а не имя файла).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:

R4>show cdp neighbors

Device ID	 Local Intrfce	 Holdtme	 Capability		  Platform	  Port ID
R5			 Fa 0/1			 122		   R S I		   2811		  Fa 0/1
R6			 Fa 0/2			 143		   R S I		   2811		  Fa 0/0
Функция должна вернуть такой словарь:

{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
 ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from open_file import line

def parse_cdp_neighbors(cdp):

	'''функция возвращает словарь из пары ключ(имя собственного устройства, интерфейс подключения) 
	и значение (имя устройства соседа, интерфейс подключения соседа)'''

	for s in cdp:
		if s == '>':
			self_name = cdp[0:cdp.index(s)] #мыводим собственное имя устройства
	list=cdp.split('\n')
	cdp_neighbors = {}
	for s in list:
		if s.startswith('R' or 'T' or 'B' or 'S' 
		or 'H' or 'I' or 'r' or 'P') and s[1].isdigit:	# проверяем строку на условие
			neighbors=s.split()	
			#расспаковываем переменные по нужным параметрам соседа:
			n_router, int, local_int, port, port_id = neighbors[0],neighbors[1], neighbors[2], neighbors[-2], neighbors[-1]
			key=[self_name, int+local_int] 
			value=[n_router, port+port_id] #присваиваем нужные параметры переменным для словаря
			cdp_neighbors[tuple(key)]=tuple(value)
	return cdp_neighbors

print(parse_cdp_neighbors(line))