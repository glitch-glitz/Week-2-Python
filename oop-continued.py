class Person:

#5. class attributes
    species = "Homo Sapien Sapien"

    def __init__(self, name):
# 1. instance attributes
        self.name = name

#2. instance methods  6. add species here
    def walk(self, pace):
        return(f"{self.name} of species {self.species} is walking with the pace {pace}")

#3. to capitalize
    def capitalize(self):
        return self.name.capitalize()
# 4. all in caps
    def upper(self):
        return self.name.upper()


person1= Person("calvin Burtler")


print(person1.name)
print(person1.capitalize())
person1.name= "tina Burtler"
print(person1.walk("fast"))
print(person1.capitalize())
print(person1.species)

person2 = Person("marty Burtler")
print(person2.name)
print(person2.capitalize())
print(person2.name.upper())
print(person2.walk("fast"))

simple_strng = "Siticom"
print(simple_strng.upper())


person3 = Person("Gemma Johson")
print(person3.walk("slow"))





class Car:
    #class attributes
    model = "Audi"

    def __init__(self, color):
        #instance attrbutes
        self.color = color

    def start(self, status):
        return (f"The {self.color} {self.model} has {status}")
        

car1= Car("Green")
print(car1.start("started"))


car2=Car("Purple")
print(car2.color)
print(car2.start("stopped"))

class Driver:
    uniform = "Blue"

    def __init__(self, age):
        self.age = age
        pass



class Customer:
    payment_method="Card"
    currency = "USD"


    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def pay(self, amount):
        return (f"Customer {self.name}, of phone number {self.phone} has paid {amount}{self.currency} via {self.payment_method}")

# 1. class methods
# must provide the @classmethod when ceating or dealing with class methods
    @classmethod
    def example(cls):
        print(f"The currency we use is {cls.currency}")

customer1= Customer("Dave", "079305032")
print(customer1.pay(1000))
customer1.example()
Customer.example()
Customer.pay(customer1, 1000)