x=10
y=5.5
print(x+y)

name="RobotX"
print("Hello, " + name)

is_active=True
print(not is_active)

a, b, c=1, 2, 3
print(a, b, c)

a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

import sys

allowed_name = "Bradley"
name=input("Enter your name: ")
if name != allowed_name:
    print("Unauthorized access")
    sys.exit()
print("Access granted. welcome, " +name + "!")
print("Running secure operations clone...")


x=20
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is 10")
else:
    print("x is less than 10")
    
    
for i in range(5):
        print("Iteration:" , i)
count = 0
while count < 3:
    print("Count:", count)
    count += 1

def greet(name):
    return "Hello,  " + name
print(greet("Elijah"))

robots = ["Atals", "Spot", "ASIMO"]
print(robots[0])
robots.append("CyberDog")
print(robots)
robots.remove("Spot")
print(robots)

