# -*- coding: utf-8 -*-

username = input('Введите имя пользователя:')
password = input('Введите пароль:')


# password_correct = False


while True:
	
	if len(password) < 8:
		print('Пароль слишком короткий\n')
		
	elif username in password:
		print('Пароль содержит имя пользователя\n')
		
	else:
		print('Пароль пользователя {} установлен'.format(username))
		# завершает цикл while
		break
	password=input('Введите пароль еще раз:')
