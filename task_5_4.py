
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_str=tuple(num_list)
num=input('Введите элемен, что бы узнать индекс последнего {}:'.format(num_str))

sum_index=len(num_list) # проверка номера ниндекса последнего элемента (определение количества элементов в списке)
num_list.reverse() # перевернуть лист
index=sum_index-num_list.index(int(num))-1 # вычисление номера индекса последнего

print_template_num=''' Номер последнего  индекса введенного элемента ({}):{} 
'''
print(print_template_num.format(num, index))


word_name=tuple(word_list)
word=input('Введите элемен, что бы узнать индекс последнего {}:'.format(word_name))

sum_index=len(word_list) # определение количества элементов в списке
word_list.reverse() # перевернуть лист
index=sum_index-word_list.index(word)-1 # вычисление номера индекса последнего


print_template_word=''' Номер последнего индекса введенного элемента ({}):{}
'''
print(print_template_word.format(word, index))