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
        if command.endswith('allowed vlan'):
            #for trunk in trunkstr:
            if trunkstr[0] == 'add':
            		list1=[str(trunk) for trunk in trunkstr]
            		print(' {}  add {}'.format(command, ','.join(list1))
	        	#elif trunkstr[0] == 'only':
	        	#	list1=[str(trunk) for trunk in trunkstr]
	        	#	print(' {}  {}'.format(command, ','.join(list1))
	        	#elif trunkstr[0] == 'del':
	        	#	list1=[str(trunk) for trunk in trunkstr]
	        	#	print(' {} remove {}'.format(command, ','.join(list1))
			
		else:
		print(' {}'.format(command))
		