# 6.3 Модуль math


# Задача 1
# from math import pi
# r = float(input())
# s = pi * (r ** 2)
# c = 2 * pi * r
# print(s, c, sep='\n')


# Задача 2
# from math import floor, ceil
# x = float(input())
# x1 = floor(x)
# x2 = ceil(x)
# print(x1 + x2)


# Задача 3
# from math import sqrt, pow
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# p = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
# print(p)


# Задача 4
# from math import radians, sin, cos, tan, pi
# x = radians(float(input()))
# res = sin(x) + cos(x) + (tan(x) ** 2)
# print(res)


# Задача 5
# from math import tan, pi, pow
# n = int(input())
# a = float(input())
# s = (n * pow(a, 2)) / (4 * tan(pi/n))
# print(s)


# Задача 6
# from math import sqrt, pow
# a = float(input())
# b = float(input())
# arif = (a + b) / 2
# geo = sqrt(a * b)
# garm = (2 * (a * b)) / (a + b)
# kvadr = sqrt((pow(a, 2) + pow(b, 2)) / 2)
# print(arif, geo, garm, kvadr, sep ='\n')


# Задача 7
from math import sqrt, pow
a = float(input())
b = float(input())
c = float(input())
x1 = 0
x2 = 0
Di = (b ** 2) - (4 * a * c)
if Di < 0:
    print("Нет корней")
elif Di == 0:
    x1 = -(b / (2 * a))
    print(x1)
elif Di > 0:
    x1 = (-b - sqrt(Di)) / (2 * a)
    x2 = (-b + sqrt(Di)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')



    
