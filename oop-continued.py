class Person:
    def __init__(self, name):
# instance attributes
        self.name = name

#instance methods
    def walk(self):
        print(f"{self.name} is walking")

#to capitalize
    def capitalize(self):
        return self.name.capitalize()
# all in caps
    def upper(self):
        return self.name.upper()


person1= Person("calvin Burtler")


print(person1.name)
print(person1.capitalize())
person1.name= "tina Burtler"
person1.walk()
print(person1.capitalize())

person2 = Person("marty Burtler")
print(person2.name)
print(person2.capitalize())
print(person2.name.upper())

simple_strng = "Siticom"
print(simple_strng.upper())

