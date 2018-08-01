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

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
d_keys=['Protocol','Prefix','AD/Metric','Next-Hop','Last update', 'Outbound Interface']

r1 = dict.fromkeys(d_keys) #создаем словарь с пустыми занчениями

ospf_list=ospf_route.strip().split() #Убираем  возможные невидимые сиволы и разделяем(split) по пробелу

ospf_list.remove('via') # Удаляем ненужный элемент via
ospf_list[2]=ospf_list[2].strip('[]') # Удаляем ненужные символы
ospf_list[2] = 'OSPF'
r1 = {r1:i for i in ospf_list}