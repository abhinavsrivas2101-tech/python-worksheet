import numpy as np
import math as mp
# 1
L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)
L.remove(11)
L.remove(13)
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
if 13 in L:
    print("13 is present")
else:
    print("13 not found")
print(len(L))
print(sum(L))
odd_sum = 0
for i in L:
    if i%2!=0:
        odd_sum += i
print(odd_sum)
even_sum = 0
for i in L:
    if i%2==0:
        even_sum += i
print(even_sum)
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(mp.sqrt(n))+1):
        if n%i==0:
            return False
    return True
prime_sum = 0
for i in L:
    if is_prime(i):
        prime_sum += i
print(prime_sum)
L.clear()
print(L)
del L

# 2
lst = [1,2,3,4,5]
total = 0
for i in lst:
    total += i
print(total)

# 3
lst = [1,2,3,4,5]
prod = 1
for i in lst:
    prod *= i
print(prod)

# 4
arr = np.full((3,4,6),'*')
print(arr)

# 5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8] = 8.8
print(D)
D.pop(2)
print(D)
print(6 in D)
print(len(D))
total = 0
for v in D.values():
    total += v
print(total)
D[3] = 7.1
print(D)
D.clear()
print(D)

# 6
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
S1.add(55)
S1.add(66)
print(S1)
S1.remove(10)
S1.remove(30)
print(S1)
print(40 in S1)
print(S1 | S2)
print(S1 & S2)
print(S1 - S2)

# 7
import random
import string
for _ in range(100):
    length = random.randint(6,8)
    s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    print(s)
for n in range(600,801):
    prime = True
    if n<2:
        prime=False
    for i in range(2,int(mp.sqrt(n))+1):
        if n%i==0:
            prime=False
            break
    if prime:
        print(n)
for n in range(100,1001):
    if n%7==0 and n%9==0:
        print(n)

# 8
exam_st_date = (11,12,2025)
print("The examination will start from:", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])

# 9
nums = [5,10,12,15,20,23]
for n in nums:
    if n%5==0:
        print(n)

# 10
num = int(input())
is_even = num%2==0
if is_even:
    print("Even")
else:
    print("Odd")

# 11
s = "Emma is Emma in class"
print(s.count("Emma"))

# 12
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
new_list = [x for x in list1 if x%2!=0] + [x for x in list2 if x%2==0]
print(new_list)

# 13
positions = [(2,3),(4,5),(6,7),(7,8)]
even_x = [pos for pos in positions if pos[0]%2==0]
print(even_x)

# 14
sensor_data = {1:2.3, 2:4.5, 3:1.8, 4:3.6}
ids = [k for k,v in sensor_data.items() if v>3.0]
print(ids)

# 15
commands_received = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed = {"MOVE","TURN_LEFT","STOP"}
not_executed = commands_received - commands_executed
print(not_executed)