access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']




mode=input('Enter interface mode (acces/trunk):')
nember=input('Enter interface type and number:')
vlan=input('Enter vlan(s):')

print(access_template(vlan))