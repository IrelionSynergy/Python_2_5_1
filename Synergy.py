print('Введите число:')
number = int(input())

if number > 0: 
    if number % 2 == 0:
        print('Положительное четное число')
    else:
        print('Положительное нечетное число')
elif number < 0:
    if number % 2 == 0:
        print('Отрицательное четное число')
    else:
        print('Отрицательное нечетное число')

else:
    print('Нулевое число')