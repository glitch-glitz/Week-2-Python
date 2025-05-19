# inheritance allows a class called a child or subclass 
# to inherit attributes or methods from another class called parent or superclass



# basic syntax
class Parent: # parent class
    def __init__(self):
        pass
    
    def check(self):
        print("Hello from parent class")

parent1 = Parent()
parent1.check()

class Child(Parent): # child class that gets all the attributes and methods fromParent
    
    def __init__(self):
        pass
    def grow_up(self):
        print("Child is growing")

child = Child()
child.check()
child.grow_up()



class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return(f"My name is {self.name}")
    def walk(self):
        return "This person is walking"

person1 = Person("Kimberly")
print(person1.introduce())
print("Person", person1.walk())

class Student(Person):
    def __init__(self, name):
        #this allowsus to access parent methods
        # in this case we want the student name to be used 
        # as the Person name
        super().__init__(name)
        self.name = name
        pass
    def working(self):
        return(f"{self.name} works at the court")

student1 = Student("Wes")
print(student1.introduce())
print("Student", student1.walk())
print("Student", student1.working())
print("<Student>", student1.introduce())




class Animal:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    def eat(self):
        return (f"{self.name} is eating")

crabs = Animal("crabs", 4)
print("<Animal>", crabs.eat())


class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, age)
        # self.name = name
        self.breed = breed

    # by redifining the methods in the parent class, 
    # we canbe able to override them (polymorhism)

    def eat(self):
        return f"{self.name} is chewing sugar cane"


dog1 = Dog("Ted",  "Mutina", 3)
print("<dog>",dog1.eat())
print("<dog>", dog1.name)
print("<dog>", dog1.breed)



class Car:
    def __init__(self, model, driver ="Wantam"):
        self.model =model
        self.driver =driver
    def drive(self):
        return f"Car of of model {self.model} is being driven by {self.driver}"
    
    def __repr__(self):
         return f"Car Model: {self.model}"
car1 = Car("Benz")
print(car1)
print("<Car>", car1.drive())


class Toyota(Car):
    def __init__(self, model = "Toyota"):
        super().__init__(model)

toyota1 = Toyota()
print("<Toyota>", toyota1.drive())

toyota2= Toyota("Carina")
print("<Toyota>", toyota2.drive())