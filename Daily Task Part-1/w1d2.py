

# ==================================================================
# TOPIC: INPUT AND SIMPLE CALCULATIONS
# ==================================================================

# 151 - Input and print a user name
name = input("Enter your name: ")
print("Hello", name)

# 152 - Input two numbers and add them
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)

# 153 - Multiply two input numbers
a = int(input("First number: "))
b = int(input("Second number: "))
print("Product:", a * b)

# 154 - Divide safely
a = float(input("Number: "))
b = float(input("Divide by: "))
if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")

# 155 - Calculate rectangle area from input
length = float(input("Length: "))
width = float(input("Width: "))
print("Area:", length * width)

# 156 - Calculate triangle area
base = float(input("Base: "))
height = float(input("Height: "))
print("Area:", base * height / 2)

# 157 - Calculate circle circumference
r = float(input("Radius: "))
print("Circumference:", 2 * 3.14 * r)

# 158 - Convert kilometers to meters
km = float(input("Kilometers: "))
print("Meters:", km * 1000)

# 159 - Convert kilograms to grams
kg = float(input("Kilograms: "))
print("Grams:", kg * 1000)

# 160 - Convert hours to minutes
hours = float(input("Hours: "))
print("Minutes:", hours * 60)

# 161 - Convert minutes to seconds
minutes = int(input("Minutes: "))
print("Seconds:", minutes * 60)

# 162 - Calculate total price with tax
price = float(input("Price: "))
tax = float(input("Tax percent: "))
print("Total:", price + price * tax / 100)

# 163 - Calculate discount price
price = float(input("Price: "))
discount = float(input("Discount percent: "))
print("Final price:", price - price * discount / 100)

# 164 - Convert Fahrenheit to Celsius
f = float(input("Fahrenheit: "))
print("Celsius:", (f - 32) * 5 / 9)

# 165 - Calculate age next year
age = int(input("Your age: "))
print("Next year:", age + 1)

# 166 - Calculate average of input marks
a = float(input("Mark 1: "))
b = float(input("Mark 2: "))
c = float(input("Mark 3: "))
print("Average:", (a + b + c) / 3)

# 167 - Calculate square root
n = float(input("Number: "))
print("Square root:", n ** 0.5)

# 168 - Calculate cube of a number
n = int(input("Number: "))
print("Cube:", n ** 3)

# 169 - Calculate remainder from input
a = int(input("Number: "))
b = int(input("Divisor: "))
if b != 0:
    print("Remainder:", a % b)


