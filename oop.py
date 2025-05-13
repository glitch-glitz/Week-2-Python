# Object Oriented \programming


""" Four main principles of OOP
1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism 

-> Mainly involves use of classes and objects
->Usually has methods and properties(atributes)

"""

# class -> blueprint of how objects are created and how they behave

# Attributes -> name, class, grade, reg no
# Behaviours -> read, playing, partying, rebellious

# syntax 
class Student:

    #should always be present when creating classes in python
    #it always takes self as its 1st parameter
    #this method is always automatically called when a new instance is created
    def __init__(self, name, age):
        #instance attributes
        self.name = name
        self.age = age
#we use methods to define behaviours
#it always takes self as the first param
    def read(self):
        print(f"{self.name} is reading about oop")
#creating an instance of the student class
student1 = Student("Vic", 20)

print((student1.name))
print((student1.age))
student1.read()

student2 =Student("Edna", 23)

print((student2.name))
print((student2.age))
student2.read()

student3 ={
    "name": "Brian",
    "age":25
}



