courses = ["MIT","CyberSecurity","DataScience"]
print(courses)
#Accessing an element
print(courses[2])


#Looping through an array
for a in courses:
    print("course is",a)

#Adding a new element into array
courses.append("laravel")
print(courses)

#Deleting an element from an array
courses.remove("CyberSecurity")
print(courses)