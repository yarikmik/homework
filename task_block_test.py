

network = input('Введите IP адрес:')
networkstr=network



network_string_correct = False	

while not network_string_correct:
	if network_string_correct == False:
		for i in networkstr:
			if  i == ",":
			
				print('Incorrect IPv4 address (адрес не должен содержать запятых)')
				network = input('Введите IP(,) адрес еще раз:')
				networkstr=network
			
			else:
				network_string_correct= True
				
				
	
		
	else:
		network_string_correct= True
	break