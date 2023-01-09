# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def postive_fib(num):     
    positive_list = [1,1]     
    for i in range(num-2):         
       positive_list.append(positive_list[-2]+positive_list[-1])     
    return positive_list

def negative_fib(num):     
    negative_list = [1,0]     
    for i in range(num-1):         
       negative_list.insert(0,negative_list[1]-negative_list[0])     
    return negative_list

print(negative_fib(8) + postive_fib(8))
