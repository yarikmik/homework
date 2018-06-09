network = input('Enter network number:')
mask = input('Enter mask number: /')

network=network.strip(',').split('.')


network_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_template = '''
Mask:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''



#print('\n' )
print('\n' )
print('\n' + '-'* 30)
#print(network)

print(network_template.format(int(network[0]),int(network[1]),int(network[2]),int(network[3])))









'''
interface = input('Enter interface type and number:')
vlan = input('Enter VLAN number:')
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n' + '-'* 30)
print('interface {}'. format(interface))

print('\n'.join(access_template).format(vlan))
'''