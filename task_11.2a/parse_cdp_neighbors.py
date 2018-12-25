
if __name__ == "__main__":
	from open_file import *

def parse_cdp_neighbors(line):

	'''функция возвращает словарь из пары ключ(имя собственного устройства, интерфейс подключения) 
	и значение (имя устройства соседа, интерфейс подключения соседа)'''
	line=line.strip() # убираем возможные невидимые символы в начале и конце
	for s in line:
		if s == '>':
			self_name = line[0:line.index(s)] #мыводим собственное имя устройства

	list=line.split('\n')
	list.pop(0) # удаляем первый элемет в списке что бы он больше не учавствовал в дальнейшем отборе на условие
	cdp_neighbors = {}
	for s in list:
		devise=['R', 'T', 'B', 'S', 'H', 'I', 'r', 'P'] 
		# проверяем строку на условие
		if any(s.startswith(d) for d in devise) and (s[1].isdigit or s[2].isdigit):
			neighbors=s.split()	
			#расспаковываем переменные по нужным параметрам соседа:
			n_router, int, local_int, port, port_id = neighbors[0],neighbors[1], neighbors[2], neighbors[-2], neighbors[-1]
			key=[self_name, int+local_int] 
			value=[n_router, port+port_id] #присваиваем нужные параметры переменным для словаря
			cdp_neighbors[tuple(key)]=tuple(value)
			#cdp_neighbors[key]=value
	return cdp_neighbors


	
if __name__ == "__main__":
	print(parse_cdp_neighbors(line1))
	print(parse_cdp_neighbors(line2))
	print(parse_cdp_neighbors(line3))
	print(parse_cdp_neighbors(line4))
	input()