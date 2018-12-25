# -*- coding: utf-8 -*-
'''
Задание 11.2

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''



from parse_cdp_neighbors import parse_cdp_neighbors as parse
from draw_network_graph import draw_topology
from open_file import *
#import open_file 


cdp_summ=parse(line1)
cdp_summ.update(parse(line2))
cdp_summ.update(parse(line3))
cdp_summ.update(parse(line4))


cdp_all={}
for key, value in cdp_summ.items():
	for key2, value2 in cdp_summ.items():
		if key!=value2 and value!=key2:
			cdp_all[key]=value

print(cdp_all)
draw_topology(cdp_all)



