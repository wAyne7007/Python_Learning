# 7.2 Цикл for: функция range


# Задача 1
# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     print(i)


# Задача 2
# n = int(input())
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# Задача 3
# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
#         print(i)


# Задача 4
# m = int(input())
# n = int(input()) 

# for i in range(m % 2 - 1 + m, n - 1, -2):
#         print(i)

# Вариант 2
# m = int(input())
# n = int(input())

# if m % 2 == 1:
#     start = m
# else:
#     start = m - 1
# end = n - 1 

# for i in range(start, end, -2):
#     print(i)


# Задача 5
m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)



