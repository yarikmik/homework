'''
Функция ожидает, как аргумент, словарь access-портов, вида:

{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17,
 'FastEthernet0/17':150}
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
'''


access_dict = { 'FastEthernet0/12':10,
				'FastEthernet0/14':11,
				'FastEthernet0/16':17,
				'FastEthernet0/17':150 }


def generate_access_config(access):
	"""генератор конфигурации access портов"""
	access_template = ['switchport mode access',
					   'switchport access vlan',
					   'switchport nonegotiate',
					   'spanning-tree portfast',
					   'spanning-tree bpduguard enable']
	access_list=[]
	
	for intf, vlan in access.items():
		access_list.append('interface' + intf )
		for line in access_template:
			if line.endswith('vlan'):
				access_list.append(line + ' ' + str(vlan))
			else:
				access_list.append(line)
	return access_list

print('\n'.join(generate_access_config(access_dict)))
