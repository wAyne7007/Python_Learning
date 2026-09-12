# 2.5 Целочисленная арифметика. Часть 2


# Задача 1
# b_1 = int(input())
# q = int(input())
# n = int(input())
# b_n = b_1 * q ** (n - 1)
# print(b_n)


# Задача 2
# sm = int(input())
# m = (sm // 100)
# print(m)


# Задача 3
# skolnik = int(input())
# manda = int(input())
# sk_m = manda // skolnik
# korzina = manda % skolnik
# print(sk_m, korzina, sep='\n')


# Задача 4
# n = int(input()) #Население вселенной
# v = (n + 1) // 2 #Выжившие
# print(v)


# Задача 5
# m = int(input()) # Минуты
# min = m % 60
# ch = m // 60
# print(m, 'мин - это', ch, 'час', min, 'минут.')

# Задача 6
# mesto = int(input())
# kupe = (mesto - 1) // 4 + 1
# print(kupe)


# Задача 7 (я манал эту арифметику)
# n = int(input())
# tri = n % 10
# dva = (n % 100) // 10
# odin = n // 100
# sum = tri + dva + odin
# proizv = tri * dva * odin
# print('Сумма цифр =', sum)
# print('Произведение цифр =', proizv,)

# Задача 8
# n = int(input())
# a = n // 100
# b = (n % 100) // 10
# c = n % 10
# print(n)
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# Задача 9
n = int(input())
d_1 = n // 1000 % 10
d_2 = n // 100 % 10
d_3 = n // 10 % 10
d_4 = n // 1 % 10
print('Цифра в позиции тысяч равна', d_1)
print('Цифра в позиции сотен равна', d_2)
print('Цифра в позиции десятков равна', d_3)
print('Цифра в позиции единиц равна', d_4)


# ЭКЗАМЕН


# Задача 1
# print("*****************")
# print("*               *")
# print("*               *")
# print("*****************")

# Задача 2
# a = int(input())
# b = int(input())
# kvsum = (a + b) ** 2
# sumkv = a**2 + b**2
# print("Квадрат суммы", a, "и", b, "равен", kvsum)
# print("Сумма квадратов", a, "и", b, "равна", sumkv)

# Задача 3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# n = a**b + c**d
# print(n)

# Задача 4
# n = int(input())
# print(n * 123)
