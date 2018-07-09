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
networkstr=network

					
network=network.strip(',').split('.')				
				
print_template = ''' 
Адрес: {}
Принадлежит сети - {}
'''
				
#network_correct = False				
				
				
while True:
		
	#Проверка на наличие заяпятых в строке адреса
	if networkstr.count(',')>0:
		print('\n Incorrect IPv4 address (Адрес не должен содержать запятых) \n ')
	
	#Проверка на наличие букв в записи адреса	
	elif (''.join(network)).isdigit()==False:
		print('\n Incorrect IPv4 address (Необходимо вводить числовые значения) \n ')
	
	# Проверка на колличество октетов в IP адресе		
	elif len(network)!=4:
		print('\n Incorrect IPv4 address (октетов должно быть 4) \n ')
		
	# Проверка на корректность введенного IP
	elif ( int(network[0])<0 or int(network[0])>255 
		or int(network[1])<0 or int(network[1])>255 
		or int(network[2])<0 or int(network[2])>255 
		or int(network[3])<0 or int(network[3])>255):
		print('\n Incorrect IPv4 address (число в октете должно быть в диапазоне от 0 до 255)\n')
	

	else:
		network_correct = True
		
		oct1 = int(network[0])
		oct2 = int(network[1])
		oct3 = int(network[2])
		oct4 = int(network[3])
		
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
		
		break
	network = input('Введите IP адрес еще раз:')
	networkstr=network
	network=network.strip(',').split('.')


