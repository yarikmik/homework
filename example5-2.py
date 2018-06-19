device=input('Enter device name:')
device=device.lower()

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

name_template='''
Enter parametr name {}: '''


#london_str=london_co[device].keys()

name=input(name_template.format(tuple(london_co[device].keys()))) #пихаем в форму список ключей выбранного списка
name=name.lower()
#print('\n' )
print('\n' + '-'* 35)

print(london_co[device].get(name, 'Такого параметра нет'))