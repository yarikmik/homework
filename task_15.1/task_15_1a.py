# -*- coding: utf-8 -*-
'''
Задание 15.1a

Напишите регулярное выражение, которое отобразит строки
с интерфейсами 0/1 и 0/3 из вывода sh ip int br.

Проверьте регулярное выражение, используя скрипт, который был создан в задании 15.1,
и файл sh_ip_int_br.txt.

В этом файле нужно написать только регулярное выражение.

'''

regex = 'Fa\S+(0/1|3)'
print regex