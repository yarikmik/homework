
if __name__ == "__main__":
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
			#cdp_neighbors[key]=value
	return cdp_neighbors


	
if __name__ == "__main__":
	print(parse_cdp_neighbors(line))
	input()