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
oct1 = int(network[0])
oct2 = int(network[1])
oct3 = int(network[2])
oct4 = int(network[3])



print_template = ''' 
Адрес: {}
Принадлежит сети - {}
'''
network_correct = True

while not network_correct:
	for i in network:
		if int(i) < 0 or int(i) > 255:			# Проверка на корректность введенного IP
			print('Incorrect IPv4 address')
			break

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
