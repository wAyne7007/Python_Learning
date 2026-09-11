# Условный оператор: 4.3 Вложенные и каскадные условия


# Задача 1
# n = int(input())
# k = int(input())
# if n > k:
#     print("NO")
# elif n < k:
#     print("YES")
# else:
#     print("Don't know")


# Задача 2
# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# Задача 3
# a = int(input())
# b = int(input())
# c = int(input())
# if (a < b < c) or (c < b < a):
#     print(b)
# elif (b < a < c) or (c < a < b):
#     print(a)
# else:
#     print(c)


# Задача 4
# month = int(input())
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print("31")
# elif month == 2:
#     print("28")
# else:
#     print("30")


# Задача 5
# weight = int(input())
# if weight <= 59:
#     print("Легкий вес")
# elif 60 <= weight < 64:
#     print("Первый полусредний вес")
# else:
#     print("Полусредний вес")


# Задача 6
# a = int(input())
# b = int(input())
# c = input()
# if c == "/" and b == 0:
#     print("На ноль делить нельзя!")
# elif c == "*":
#     print(a * b)
# elif c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "/":
#     print(a / b)
# else:
#     print("Неверная операция")


# Задача 7
# a = input()
# b = input()
# if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
#     print('зеленый')
# elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
#     print(a)
# else:
#     print('ошибка цвета')


# Задача 8 
# a = int(input())

# if a == 0:
#     print("зеленый")
# elif 1 <= a <= 10:
#     if a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 11 <= a <= 18:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif 19 <= a <= 28:
#     if a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 29 <= a <= 36:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")


# Задача 9
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 > a2:
    left = a1
else:
    left = a2
if b1 < b2:
    right = b1
else:
    right = b2
if left > right:
    print("пустое множество")
elif left == right:
    print(left)
else:
    print(left, right)
