# Built0-in function/Standard library functions


y= max(67, 43, 89, 90, 23)
print("The maximum value is", y)

x = min(67, 43, 89, 90, 23)
print("The minimum value is", x)


# User-defined Functions
def name():
    print("Frankie")

name() #Calling Function
print()

def multiply():
    x = 10
    y = 2
    print(x * y)
multiply()

#parameter and argument
def add(a, b):
    print(a + b)
add(2, 7)
add(10, 7)

def employee(name, gender, position,salary, age):
    print(name, gender, position, salary, age)
employee("John", "Male", "CEO", "350000", "25")


#student
def student(Fullname, age, course, gender):
    print(Fullname, age, course, gender)
student(Fullname="Joseph", age=25, course="Python", gender="Male")
student(Fullname="Cynthia", age=24, course="MIT", gender="female")
student(Fullname="Brian", age=23, course="CyberSecurity", gender="Male")
student(Fullname="Jane", age=22, course="Web developing", gender="female")
student(Fullname="John", age=21, course="DataScience", gender="Male")
