# ЭКЗАМЕН


# Задача 1
# year = int(input())
# if year % 100 == 0:
#     print("YES")
# else:
#     print("NO")


# Задача 2
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if (y1 + x1 + x2 + y2) % 2 == 0:
#     print("YES")
# else:
#     print("NO") 


# Задача 3
# v = int(input())
# sex = input()
# if 10 <= v <= 15 and sex == "f":
#     print("YES")
# else:
#     print("NO")


# Задача 4
# num = int(input())
# if num == 1:
#     print("I")
# elif num == 2:
#     print("II")
# elif num == 3:
#     print("III")
# elif num == 4:
#     print("IV")
# elif num == 5:
#     print("V")
# elif num == 6:
#     print("VI")
# elif num == 7:
#     print("VII")
# elif num == 8:
#     print("VIII")
# elif num == 9:
#     print("IX")
# elif num == 10:
#     print("X")
# else:
#     print("ошибка")


# Задача 5
# x = int(input())
# if x % 2 != 0:
#     print("YES")
# elif 2 <= x <= 5 and x % 2 == 0:
#     print("NO")
# elif 6 <= x <= 20 and x % 2 == 0:
#     print("YES")
# elif x > 20 and x % 2 == 0:
#     print("NO")


# Задача 6
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 > x2:
#     dist_x = x1 - x2
# else:
#     dist_x = x2 - x1
# if y1 > y2:
#     dist_y = y1 - y2
# else:
#     dist_y = y2 - y1
# if dist_x == dist_y:
#     print("YES")
# else:
#     print("NO")


# Задача 7
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 > x2:
#     dist_x = x1 - x2
# else:
#     dist_x = x2 - x1
# if y1 > y2:
#     dist_y = y1 - y2
# else:
#     dist_y = y2 - y1
# if (dist_x == 2 and dist_y == 1) or (dist_x == 1 and dist_y == 2):
#     print("YES")
# else:
#     print("NO")


# Задача 8
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 > x2:
    dist_x = x1 - x2
else:
    dist_x = x2 - x1
if y1 > y2:
    dist_y = y1 - y2
else:
    dist_y = y2 - y1
if dist_x == dist_y or x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
    