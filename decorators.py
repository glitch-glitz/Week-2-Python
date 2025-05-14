"""
->are design patterms that allow us to modify the functionality of a function without necessarily modifying the function code itself
-> it adds the special @ symbol on functions
"""

#how to create decorators
def logger(func):
    #define another innner function
    def inner():
        print("Decorator is running before function")
        #execute the original function
        func()
    return inner

@logger
def check_mic():
    print("Is the mic working")
check_mic()

# the @logger saves us from the process below
decorated_func =logger(check_mic)

#call/execute the inner function

decorated_func()

#another example
def modifier(func):
    def inner(a, b):
        #modify arguement a
        a = a + 5
        #call the original function
        return func(a,b)

    return inner


def validator(func):
    def inner(a, b):
        #check is the args are of type int
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            return "Args must be of type int"
    return inner



#running modifier first will result to an error, but changing the order undoes the error
@validator
@modifier
def calculate(a, b):
    # print(a, b)
    return a + b
@validator
def multiply(x, y):
    return x * y

# print(calculate(3, 3))

print(calculate("Wed", "Thur"))
print(multiply(2, 2))
print(multiply("Y", 4))
