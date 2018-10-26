'''
Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:

ключи: имена интерфейсов, вида 'FastEthernet0/12'
значения: список команд, который надо выполнить на этом интерфейсе:

'''


access_dict = { 'FastEthernet0/12':10,
				'FastEthernet0/14':11,
				'FastEthernet0/16':17,
				'FastEthernet0/17':150 }


def generate_access_config(access, portsec=False):
	"""генератор конфигурации access для портов"""
	access_template = ['switchport mode access',
					   'switchport access vlan',
					   'switchport nonegotiate',
					   'spanning-tree portfast',
					   'spanning-tree bpduguard enable']
	
	port_security = ['switchport port-security maximum 2',
					 'switchport port-security violation restrict',
					 'switchport port-security']

	access_port={}
	
	for intf, vlan in access.items():
		
		
		for line in access_template:
			if line.endswith('vlan'):
				access_port['interface ' + intf] = line + ' ' + str(vlan)
			else:
				access_port['interface ' + intf] = line 
		if portsec:
				access_port['interface ' + intf] = port_security 
	return access_port

print('\n'.join(generate_access_config(access_dict, True)))
