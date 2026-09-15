# 7.1 Цикл for


# Задача 1
# for i in range(10):
#     print("Python is awesome!")


# Задача 2
# a = "AAA"
# b = "BBBB"
# t = "TTTTT"
# for i in range(6):
#     print(a)

# for i in range(5):
#     print(b)

# print("E")

# for i in range(9):
#     print(t)

# print("G")


# Задача 3
# text = input()
# num = int(input())

# for i in range(num):
#     print(text)


# Задача 4
# num = int(input())

# for i in range(num):
#     print('*' * 19)


# Задача 5
# name = input()
# for i in range(10):
#     print(i, name)


# Задача 6
# n = int(input())

# for i in range(n + 1):
#     print("Квадрат числа", i, "равен", i * i)


# Задача 7
# n = int(input())

# for i in range(n):
#     print('*' * (n - i))


# Задача 8
m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    population = m * (1 + p / 100) ** i
    print(i + 1, population)

