# Are attributes controlled by methods
# this meas how we get the values and store the values
class Car:
    def __init__(self, name, year):
        #attributes using the underscore indicate that 
        # they should only be used or accessed within 
        # the class itself and not outside
        self._name = name 
        self._year = year

    #getter method
    @property
    def name(self):
        return self._name.upper()
    
    @property
    def year(self):
        return self._year

    # setter method
    @name.setter
    def name(self, value):
        # check value is equal to Audi
        if value == "Audi":
            self._name = value
        else:
            # the raise keyword behaves like the retun keyword 
            # where they both sto execution 
            # it also stops execution of the entire program

            raise ValueError("Car name must be Audi")
    
    @year.setter
    def year(self, value):
        #this checks for falsiness
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")

car1 = Car("Audi", 2020)
print(car1.name)
# we should no longer access attriibutes that start with the nderscore
# this pattern falls under encaspulation 
# we shouldn't do this  ---> print(car1._name)

car1.year = 2030


#  car1.year ="Twenty twenty five"

car1.name = "Audi"

print(car1.year)




# scenario

class Voter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter method
    @property
    def age(self):
        return self._age
    
    #setter method
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an Integer")
        if value >= 18:
            self._age = value
        else:
            raise ValueError("Age must 18+")

voter1 = Voter("Jane", 24)
print(voter1._name)
print(voter1._age)