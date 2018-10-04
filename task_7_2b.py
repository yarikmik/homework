# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.

7.2b
вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.

Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
'''
sw=open('config_sw1.txt', 'r')
sw_conf=sw.read().strip().split('\n')
sw.close()
ignore = ['duplex', 'alias', 'Current configuration']
sw_print=[]

# При попытке удалять записи из уже существующего списка почему то некоторые строки не считаются, 
# проще переписывать отсортированные строки в новый список
"""
# блок очищает от пустых строк и лишних пробелов
for s in sw_conf:
	s=s.strip(' ') # убираем символы пробела
	if s=='':		# Пропускаем пустые строки
		continue
	else:
		sw_print.append(s)
		#print(s)
""" 

# блок сравнивающий множества из слов строки и списка фильтра(ignore), проблема в том, что третий элемент фильтра состоит из двух слов
for s in sw_conf:
		if not (set(ignore) & set(s.split())): # Проверка , что множество ignore пересекается со множеством s
			#del sw_print[sw_print.index(s)]
			sw_print.append(s)





sw_print = [ line + '\n' for line in sw_print ]


'''
for s in sw_print:
	print(s)
print('\n' + '-'*35)

for s in sw_conf:
	for i in ignore:
		if i in s:				#проверяем на наличие в строке элемента из фильтра
			sw_conf.remove(s)	#удаляем элемент из списка

f=open('config_sw1_cleared.txt', 'w')
f.writelines(sw_conf)
f.close	

print('\n' + '-'*35)
for s in sw_conf:
	print(s)

input()
			
'''


f=open('config_sw1_cleared.txt', 'w')
f.writelines(sw_print)
f.close	

print('\n' + '-'*35)
for s in sw_print:
	print(s)

input()
