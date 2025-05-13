
# 1. Conditional statements
age = 20

if age > 18:
    print("You are an adult")
else:
    print("You are a child")



score =67

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >=50:
    print("Grade C")
else:
    print("Grade D")


# multiple conditions using ternary operator
age = 90
message = "Kid" if age <= 18 else\
          "Adult" if age < 18 else \
          "Third floor" if age > 30 else\
          "Above 80"

# Python does not support the switch statement 


def grader(score):
    if score < 0 or score > 100:
        print("Invalid score. Score has to be between 100 and 0")
    if score >= 0 and score <= 100: #this checks for truthy
        print("Score legit")
    else:
        return "Invalid score. Score has to be between 100 and 0"

print(grader(score = 1))

# Loops using Loop

colors =["red", "blue", "green"]

for color in colors:
    print(color)


# range -> inbuilt function that generates a sequence of numbers
for i in range(5):
    print(i)

#while loops execut blocks of codes repeatedly as long as the given condition is true
count = 0
while count <5:
    print(count)
    count += 1