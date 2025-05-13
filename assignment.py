"""
create a class Person with 3-4 atrributes and 2 methods (behaviours)
"""

class Person:
    def __init__(self, name, height, hobby):
        self.name = name
        self.height =height
        self.hobby = hobby
    def work(self):
        print(f"{self.name} is a paralegal")
    def workout(self):
        print(f"{self.name} goes to the gym 4-5 days a week")

person1 =(Person("Wes", 6.1, "Chess"))
print(person1.name)
print(person1.height)
person1.work()
person1.workout()