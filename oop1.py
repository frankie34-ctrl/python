class Person:
    def __init__(self, name, gender, age, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def speak(self):
        print(self.name,"is speaking")

person1 = Person("John", "Male", 22, "Teacher")
print(person1.name)
person1.speak()

person2 = Person("Mark", "Male", 25, "Teacher")
print(person2.name)
person2.speak()