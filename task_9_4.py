#!/usr/bin/env python3
'''
ДСоздать функцию, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:

Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!', а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Ограничение: Все задания надо выполнять используя только пройденные темы.
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    
    return any(word in command for word in ignore)
'''


ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):

	'''Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет'''
	
	
	return any(word in command for word in ignore)
	


def get_command_dict(filename):

	'''обработка файла, разделение на словарь команд'''
	sw_print=[]
	commands={}
	
	with open(filename) as sw:
		for line in sw:
			line=line.rstrip()
			line=line.rstrip(' ') # убираем символы пробела с права
			if line=='' or '!' in line:		# Пропускаем пустые строки и строки с !
				continue
			elif ignore_command(line, ignore): #пропускаем команды из списка игнора
				continue		
			else:
				sw_print.append(line)
	
	for line in sw_print:
		if line[0] != ' ':
			global_com = line
			commands[global_com]=[]
		elif line.startswith(' '):
			commands[global_com].append(line)
	
	return commands
	
print(get_command_dict('config_sw1.txt'))







