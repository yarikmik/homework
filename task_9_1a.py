'''
ввести дополнительный параметр, который контролирует будет ли настроен port-security
имя параметра 'psecurity'
по умолчанию значение False
Проверить работу функции на примере словаря access_dict, с генерацией конфигурации port-security и без.
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

	access_port=[]
	
	for intf, vlan in access.items():
		access_port.append('interface' + intf )
		
		for line in access_template:
			if line.endswith('vlan'):
				access_port.append(line + ' ' + str(vlan))
			else:
				access_port.append(line)
		if portsec:
				access_port.extend(port_security)
	return access_port

print('\n'.join(generate_access_config(access_dict, True)))
