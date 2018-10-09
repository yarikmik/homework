"""
Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:

считывались только строки, в которых указаны MAC-адреса
каждая строка, где есть MAC-адрес, должна обрабатываться таким образом, чтобы на стандартный поток вывода была выведена таблица вида:
 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7010   Gi0/2
 300    a2ab.c5a0.2000   Gi0/3
 100    0a1b.1c80.7300   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.5000   Gi0/6
 300    0a1b.5c80.9010   Gi0/7
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

file=open('CAM_table.txt', 'r')
Cam_conf=file.read().strip().split('\n')
file.close()
Cam_print=[]


for line in Cam_conf: # Модуль удаляет пустые строки
	if not (len(line)>0):
		del Cam_conf[Cam_conf.index(line)]

for line in Cam_conf:
	line = line.split()
	if line[0].isdigit():
		Cam_print.append(line)
		

Cam_print=sorted(Cam_print) 

for line in Cam_print:
		
	Vlan, Mac, Type, Ports = line
	print('{:10}{:20}{:30}'.format(Vlan, Mac, Ports))