'''
Задача такая же, как и задании 9.4. Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл. В нём есть разделы с большей вложенностью, например, разделы:

interface Ethernet0/3.100
router bgp 100
Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности. При этом, не привязываясь к конкретным разделам. Она должна быть универсальной,
 и сработать, если это будут другие разделы.

Если уровня вложенности два:

то команды верхнего уровня будут ключами словаря,
а команды подуровней - списками
Если уровня вложенности три:

самый вложенный уровень должен быть списком,
а остальные - словарями.
На примере interface Ethernet0/3.100

{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}
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
	second_commands={}
	third_commands={}
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
		elif line[0] == ' ' and line[1] != ' ':
			second_level = line
			commands[global_com].append(second_level)
		elif line[0] == ' ' and line[1] == ' ':
			third_level = line
			
			commands[global_com]={second_level:[third_level]}
			
			
			
	return commands
	
print  (get_command_dict('config_r1.txt'))


Print_template = '''

{}

Применяемые к интерфейсу команды:
{:>10}
'''

'''
for key, value in get_command_dict('config_r1.txt').items(): #вывод на принт в удобном формате
	
	print (Print_template.format(key, '\n'.join(value)))
	print('\n' + '-'* 35)
'''



