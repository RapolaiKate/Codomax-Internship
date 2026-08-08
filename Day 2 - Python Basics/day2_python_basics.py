# ==================================================
# Variables
# ==================================================

print(" === Variables ===")

name = "Kate"
age = 25
country = "South Africa"
City = "Johannesburg"
course = "Data Science"
experience = 2

print(name)
print(age)
print(country)
print(City)
print(course)
print(experience)

# ===================================================
# Data Types
# ===================================================

print(" === Data Types ===")

name = "Kate"                            # String (str)
age = 25                                 # Integer (int)
height = 1.65                            # Float (float)
is_student = True                        # Boolean (bool)
fruits = ["Apple", "Mango", "Banana"]    # List (list)
person = {"name": "Kate", "age": 25}     # Dictionery (dict)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(fruits))
print(type(person))

# ===================================================
# Operators
# ===================================================

print(" === Operators === ")

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Division:", a / b)
print("Multiplication:", a * b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# ====================================================
# Loops
# ====================================================

print(" === Loops === ")

print(" For Loop:")
for i in range(1, 6):
    print(i)

print("While Loop:")    
count = 1
while count <= 5:
    print(count)
    count += 1

# ====================================================   
# Functions
# ====================================================

print(" === Functions === ")

def greet(name):
    print("Hello,", name)

greet("Kate")

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)

# ======================================================
# Simple Python Program
# ======================================================

print(" === Simple Python Program === ")

name = input("Enter your name: ")
age = input("Enter your age: ")

print("\nWelcome!")
print("Name:", name)
print("Age:", age)
print("Thank you for learning Data Science with Codomax!")

# =======================================================
