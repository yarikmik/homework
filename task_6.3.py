access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'}, 
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('\n')
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
				

#print('\n' )
print('\n' + '-'* 35)


for intf, trunkstr in fast_int['trunk'].items():
	print('interface FastEthernet' + intf)
	for command in trunk_template:
		# определяем строку для добавления влана и проверяем первый индекс на условие написание команды
		if command.endswith('allowed vlan') and trunkstr[0] == 'add':
			list_vlan=[str(trunk) for trunk in trunkstr] #Генерируем лист из вланов
			list_vlan.remove('add') #Удаляем вспомогательный первый элемент
			print(' {} add {}'.format(command, ','.join(list_vlan)))
			print('\n')
		elif command.endswith('allowed vlan') and trunkstr[0] == 'only':
			list_vlan=[str(trunk) for trunk in trunkstr] #Генерируем лист из вланов
			list_vlan.remove('only') #Удаляем вспомогательный первый элемент
			print(' {} {}'.format(command, ','.join(list_vlan)))
			print('\n')
		elif command.endswith('allowed vlan') and trunkstr[0]== 'del':
			list_vlan=[str(trunk) for trunk in trunkstr] #Генерируем лист из вланов
			list_vlan.remove('del') #Удаляем вспомогательный первый элемент
			print(' {} remove {}'.format(command, ','.join(list_vlan)))
			print('\n')
		else:
			print(' {}'.format(command))
		




input()