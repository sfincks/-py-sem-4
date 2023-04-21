# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

a = int(input("Введите размер первого ряда: "))
b = int(input("Введите размер второго ряда: "))

first = [random.randint(1, 20) for i in range(a)]
second = [random.randint(1, 20) for i in range(b)]

print(first)
print(second)

mfirst = set(first)
msecond = set(second)

# print(mfirst)
# print(msecond)

array = []
for i in mfirst:
    if i in msecond:
        array.append(i)
print(*array)