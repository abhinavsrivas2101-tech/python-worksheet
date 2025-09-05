import numpy as np
import math as mp
# 1
def diff_17(n):
    if n>17:
        return 2*abs(n-17)
    else:
        return 17-n
print(diff_17(20))
print(diff_17(10))

# 2
def test_range(n):
    if 100<=n<=1000 or n==2000:
        return True
    else:
        return False
print(test_range(500))
print(test_range(50))

# 3
def reverse_string(s):
    return s[::-1]
print(reverse_string("robot"))

# 4
def count_letters(s):
    upper=0
    lower=0
    for c in s:
        if c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
    return {"uppercase":upper,"lowercase":lower}
print(count_letters("RobotRobot"))

# 5
def distinct_list(lst):
    new_lst=[]
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
print(distinct_list([1,2,2,3,3,4,5]))

# 6
def even_numbers(lst):
    return [i for i in lst if i%2==0]
print(even_numbers([1,2,3,4,5,6,7,8,9]))

# 7
def robot():
    def move():
        print("Robot is moving")
    move()
robot()

# 8
def student(name, age, course):
    student.name=name
    student.age=age
    student.course=course
student("Abhi",20,"Python")
print(student.name, student.age, student.course)

# 9
def move_robot(x,y,direction):
    if direction=="up":
        y+=1
    elif direction=="down":
        y-=1
    elif direction=="left":
        x-=1
    elif direction=="right":
        x+=1
    return (x,y)
print(move_robot(0,0,"up"))

# 10
def classify_temperature(temp):
    if temp<15:
        return "Cold"
    elif 15<=temp<=30:
        return "Moderate"
    else:
        return "Hot"
print(classify_temperature(10))
print(classify_temperature(25))
print(classify_temperature(35))

# 11
def is_goal_reached(path):
    x=0
    y=0
    for move in path:
        if move=="up":
            y+=1
        elif move=="down":
            y-=1
        elif move=="left":
            x-=1
        elif move=="right":
            x+=1
    return (x,y)==(2,0)
print(is_goal_reached(["up","right","right","down"]))
print(is_goal_reached(["up","up","right"]))

# 12
class Student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def add_class(self,student_class):
        self.student_class=student_class
    def display(self):
        print("ID:",self.student_id)
        print("Name:",self.student_name)
        print("Class:",self.student_class)
s=Student(1,"Abhi")
s.add_class("10th")
s.display()

# 13
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("Abhi",20)
student2=Student("Ravi",21)
print(student1.name, student1.age)
print(student2.name, student2.age)

# 14
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return mp.pi*self.radius*self.radius
    def perimeter(self):
        return 2*mp.pi*self.radius
c=Circle(5)
print(c.area())
print(c.perimeter())

# 15
class MyString:
    def get_String(self):
        self.s=input()
    def print_String(self):
        print(self.s.upper())
m=MyString()
m.get_String()
m.print_String()

# 16
class Robot:
    def __init__(self,name,task,battery_level):
        self.name=name
        self.task=task
        self.battery_level=battery_level
    def perform_task(self):
        print(self.name,"is performing",self.task)
        self.battery_level-=10
    def recharge(self):
        self.battery_level=100
    def status(self):
        print("Name:",self.name)
        print("Task:",self.task)
        print("Battery:",self.battery_level)
r=Robot("Robo1","Cleaning",100)
r.status()
r.perform_task()
r.status()
r.recharge()
r.status()