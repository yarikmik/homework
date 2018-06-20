access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']




template_all  = [access_template, trunk_template]

mode=input('Enter interface mode (access/trunk):')
interface=input('Enter interface type and number:')

mode=mode.startswith('trunk') # проверка на совпадение, переменной присваивается true или false


vlan=input('Enter vlan(s):')


print('\n' + '-'* 35)

print('interface {}'. format(interface))
print('\n')
print('\n'.join(template_all[int(mode)]).format(vlan)) #true или false переводим в численное значение 
print('\n')
#print('\n'.join(trunk_template).format(vlan))