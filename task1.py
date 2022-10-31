# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

numbers = [i for i in range(randint(1,10))]
print(numbers)
summa = 0
for i in range(1, len(numbers), 2):
        summa += numbers[i]
print(f'Сумма нечетных элементов: {summa}')
