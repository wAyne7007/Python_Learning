# Условный оператор: Выбор из двух


# Задача 1
# passw = input()
# passw2 = input()
# if passw == passw2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')


# Задача 2
# num = int(input())
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# Задача 3 
# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# Задача 4
# num_1 = int(input())
# num_2 = int(input())
# if num_1 < num_2:
#     print(num_1)
# else:
#     print(num_2)


# Задача 5
# num_1, num_2, num_3 = int(input()), int(input()), int (input())
# if (num_2 - num_1) + num_2 == num_3:
#     print('YES')
# else:
#     print('NO')


# Задача 6
# num = int(input())
# if num // 1000 % 10 + num // 1 % 10 == num // 100 % 10 - num // 10 % 10:
#     print('ДА')
# else:
#     print('НЕТ')


# Задача 7 
# a = int(input())
# b = int(input())
# c = int(input())
# if a > 0:
#     a = a
# else:
#     a = 0
# if b > 0:
#     b = b
# else:
#     b = 0
# if c > 0:
#     c = c
# else:
#     c = 0
# print(a + b + c)


# Задача 8 
# age = int(input())
# if 0 <= age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if age >= 60:
#     print('старость')


# Задача 9
a = int(input())
b = int(input())
c = int(input())
d = int(input())
minab = 0
mincd = 0
minabcd = 0
if a < b:
    minab = a
else:
    minab = b
if c < d:
    mincd = c
else:
    mincd = d 
if minab < mincd:
    minabcd = minab
else:
    minabcd = mincd
print(minabcd)


