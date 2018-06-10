network = input('Enter network number:')
mask = input('Enter mask number: /')
mask=int(mask)
network=network.strip(',').split('.')


network_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_template = '''
Mask:
/{mask}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

# создание полной маски
mask_full= "255.255.255.255"
mask_full=mask_full.strip(',').split('.')

'''
In [11]: mask_full
Out[11]: ['255', '255', '255', '255']
'''
# преобразование маски в бинарный вид
mask_bin_str= '{:b}{:b}{:b}{:b}'.format(int(mask_full[0]),int(mask_full[1]),int(mask_full[2]),int(mask_full[3]))

'''
In [13]: mask_bin_str
Out[13]: '11111111111111111111111111111111'

'''

# преборазование маски
mask_bin_0=mask_bin_str[:mask]+'0'*(32-mask)
#In [9]: msk_bin_0
#Out[9]: '11111111111111111111111100000000'

# преобразование адреса в бинарный вид
network=



#print('\n' )
print('\n' )
print('\n' + '-'* 35)
#print(network)

print(network_template.format(int(network[0]),int(network[1]),int(network[2]),int(network[3])))

print(mask_template.format(int(mask_bin_0[0:8],2),int(mask_bin_0[8:16],2),int(mask_bin_0[16:24],2),int(mask_bin_0[24:32],2), mask=mask))








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