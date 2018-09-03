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



for s in sw_conf:
	s=s.strip(' ') # убираем символы пробела и !
	if s=='':		# Пропускаем пустые строки
		continue
	else:
		sw_print.append(s)
		#print(s)

'''
for s in sw_print:
	#for i in ignore:
		if ignore[0] in s:
			continue
		elif ignore[1] in s:
			continue
		elif ignore[2] in s:
			continue
		else:
			print(s)
'''
		
for s in sw_print:
	for i in ignore:
		if i in s:				#проверяем на наличие в строке элемента из фильтра
			sw_print.remove(s)	#удаляем элемент из списка
			print(s + ' >>>remove')			
		else:
			print (s + ' >>> NOT remove')	
			
'''
f=open('config_sw1_cleared.txt', 'w')
f.writelines(sw_print)
f.close	
'''
print('\n' + '-'*35)
for s in sw_print:
	print(s)
input()