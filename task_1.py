# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("Введите размер списка: "))
A = list(range(1, N+1))
print(A)
X = int(input("Введите интерисуемое число: "))
print(A.count(X))