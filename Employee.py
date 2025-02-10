from functions import employee


class Employee:
    def __init__(self,name, position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position)

employee1 = Employee("John","Position",20000)
print(employee1.name,employee1.position,employee1.salary)
employee2 = Employee("John","Position",20000)
employee3 = Employee("John","Position",20000)
employee4 = Employee("John","Position",20000)