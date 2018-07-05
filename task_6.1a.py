'''
A: 1-127
B: 128-191
C: 192-223
D: 224-239

'unicast' - если IP-адрес принадлежит классу A, B или C
'multicast' - если IP-адрес принадлежит классу D
'local broadcast' - если IP-адрес равен 255.255.255.255
'unassigned' - если IP-адрес равен 0.0.0.0
'unused' - во всех остальных случаях
'''

network = input('Введите IP адрес:')

network=network.strip(',').split('.')


network_string_correct = False

while not network_string_correct:
		if len(network)!=4:
		# Проверка на колличество октетов в IP адресе
			print('Incorrect IPv4 address (октетов должно быть 4)')
			network = input('Введите IP адрес еще раз:')
			network=network.strip(',').split('.')
		else:
			try:
				oct1 = int(network[0])
				oct2 = int(network[1])
				oct3 = int(network[2])
				oct4 = int(network[3])
				network_string_correct = True
			except (ValueError):
				print('Необходимо вводить числовые значения')





print_template = ''' 
Адрес: {}
Принадлежит сети - {}
'''
network_correct = False

while not network_correct:
	if oct1<0 or oct1>255 or oct2<0 or oct2>255 or oct3<0 or oct3>255 or oct4<0 or oct4>255:			
	# Проверка на корректность введенного IP
		print('Incorrect IPv4 address (число в октете должно быть в диапазоне от 0 до 255)')
		network = input('Введите IP адрес еще раз:')
		network=network.strip(',').split('.')
		oct1 = int(network[0])
		oct2 = int(network[1])
		oct3 = int(network[2])
		oct4 = int(network[3])
	
	else:
		if oct1==oct2==oct3==oct4==255:
			print (print_template.format('.'.join(network), "local broadcast"))
		elif oct1 >= 1 and oct1 <= 223:
			print (print_template.format('.'.join(network), "unicast"))
		elif oct1 >= 224 and oct1 <= 239:
			print (print_template.format('.'.join(network), "multicast"))
		elif oct1==oct2==oct3==oct4==0:
			print (print_template.format('.'.join(network), "unassigned"))
		else:
			print (print_template.format('.'.join(network), "unused"))
		network_correct = True