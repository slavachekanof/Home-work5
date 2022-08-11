#Чеканов Вячеслав Александрович
#Домашнее задание №5
#Easy
list1 = [-1, 2, 3, 4, 5, 6, 7, -4]
list2 = [i ** 2 for i in list1]
print(list2)

fruits_list_1 = ['дыня', 'яблоко', 'мандарин', 'манго', 'груша', 'апельсин', 'нектарин']
fruits_list_2 = ['банан', 'киви', 'яблоко', 'лимон', 'груша', 'ананас', 'мандарин', 'мангустин', 'дыня']

fruits_list_3 = [i for i in fruits_list_1 if i in fruits_list_2]
print(fruits_list_3)


list3 = [1, 2, 3, 4, 5, 6, 7, 8, -4, -5, -3, 12, 27]
list4 = [i for i in list3 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(list4)