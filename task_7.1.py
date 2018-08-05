'''
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде:

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
'''


d_keys=['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:', 'Outbound Interface:']



ospf_list=ospf_route.strip().split() #Убираем  возможные невидимые сиволы и разделяем(split) по пробелу

ospf_list.remove('via') # Удаляем ненужный элемент via
ospf_list[2]=ospf_list[2].strip('[]') # Удаляем ненужные символы
ospf_list[3]=ospf_list[3].strip(',')
ospf_list[4]=ospf_list[4].strip(',')
ospf_list[0] = 'OSPF'
ospf_list=list(tuple(ospf_list))

r1 = dict(zip(d_keys, ospf_list)) # Складываем два списка в словарь

print('\n')
print_template = '''{:19}  {}'''
for key in r1:
	print(print_template.format(key, r1[key]))
