# Условный оператор: Логические операции


# Задача 1
# x = int(input())
# if -1 < x < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# Задача 2
# x = int(input())
# if -3 >= x or 7 <= x:
#     print('Принадлежит')
# else:
#     # print('Не принадлежит')


# Задача 3
# x = int(input())
# if -30 < x <= -2 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# Задача 4
# num = int(input())
# if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
#     print('YES')
# else:
#     print('NO')


# Задача 5
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("YES")
# else:
#     print("NO")


# Задача 6
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")


# Задача 7
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")


# Задача 8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print("YES")
else:
    print("NO")
