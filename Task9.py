# Напишите программу, которая по заданному номеру четверти показывает
# диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти от 1 до 4: '))
if quarter == 1:
    print ('В этой четверти x > 0 и y > 0')
elif quarter == 2:
    print ('В этой четверти x < 0 и y > 0')
elif quarter == 3:
    print ('В этой четверти x < 0 и y < 0')
elif quarter == 4:
    print ('В этой четверти x > 0 и y < 0')
else:
    print ('Нужно ввести число от 1 до 4')
