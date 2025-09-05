# 1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# 2
first = input("Enter first name: ")
last = input("Enter last name: ")
print(last + " " + first)

# 3
import math as mp
radius = float(input("Enter radius: "))
area = mp.pi * radius * radius
print(area)

# 4
color_list = ["Red","Green","White","Black"]
print(color_list[0], color_list[-1])

# 5
n = input("Enter a number: ")
result = int(n) + int(n*2) + int(n*3)
print(result)

# 6
values = input("Enter numbers separated by commas: ")
list1 = values.split(",")
tuple1 = tuple(list1)
print(list1)
print(tuple1)

# 7
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print(f)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a + 1
print(a, b)

# 9
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 10
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 11
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = mp.sqrt((x2-x1)**2 + (y2-y1)**2)
print(distance)

# 12
a = float(input("Enter angle1: "))
b = float(input("Enter angle2: "))
c = float(input("Enter angle3: "))
if a + b + c == 180:
    print("Forms a triangle")
else:
    print("Does not form a triangle")

# 13
P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))
CI = P * (1 + R/100)**T - P
print(CI)

# 14
n = int(input("Enter number: "))
if n > 1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 15
N = int(input("Enter N: "))
sum_sq = sum(i**2 for i in range(1, N+1))
print(sum_sq)