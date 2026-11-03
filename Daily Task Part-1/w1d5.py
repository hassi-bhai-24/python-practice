# ==================================================================
# TOPIC: TUPLES AND SETS
# ==================================================================

# 266 - Unpack a tuple into variables
person = ("Ali", 20, "CS")
name, age, course = person
print(name, age, course)

# 267 - Create tuple from a list
items = [4, 5, 6]
print(tuple(items))

# 268 - Check value in tuple
values = (10, 20, 30)
print(20 in values)

# 269 - Sort tuple values
values = (8, 2, 5, 1)
print(tuple(sorted(values)))

# 270 - Create a singleton tuple
item = ("Python",)
print(item)

# 271 - Check disjoint sets
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

# 272 - Check superset
a = {1, 2, 3, 4}
b = {2, 3}
print(a.issuperset(b))

# 273 - Remove an item safely from set
items = {1, 2, 3}
items.discard(5)
print(items)

# 274 - Count unique numbers
nums = [1, 2, 2, 3, 4, 4]
print(len(set(nums)))

# 275 - Convert set to sorted list
items = {9, 2, 5, 1}
print(sorted(items))

# 276 - Set intersection from two user lists
a = set(map(int, input("List A: ").split()))
b = set(map(int, input("List B: ").split()))
print(a & b)

# ==================================================================
# TOPIC: DICTIONARIES
# ==================================================================

# 277 - Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Ali", 20, "Lahore"]
print(dict(zip(keys, values)))

# 278 - Get dictionary value with default
student = {"name": "Sara"}
print(student.get("grade", "Not set"))

# 279 - Loop through dictionary values
marks = {"Math": 80, "English": 75}
for mark in marks.values():
    print(mark)

# 280 - Find total of dictionary values
prices = {"pen": 20, "book": 100, "bag": 500}
print(sum(prices.values()))

# 281 - Merge two dictionaries
a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
print(a | b)

# 282 - Invert keys and values
data = {"a": 1, "b": 2}
print({value: key for key, value in data.items()})

# 283 - Group words by first letter
words = ["apple", "ant", "ball", "bat"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)

# 284 - Count letters using a dictionary
text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

# 285 - Remove a dictionary item using pop
student = {"name": "Ali", "age": 20}
age = student.pop("age")
print(age, student)

# 286 - Sort dictionary by key
data = {"c": 3, "a": 1, "b": 2}
print(dict(sorted(data.items())))

# 287 - Sort dictionary by value
data = {"Ali": 70, "Sara": 95, "Noor": 82}
print(sorted(data.items(), key=lambda item: item[1]))

# ==================================================================
# TOPIC: SIMPLE FUNCTIONS
# ==================================================================

# 288 - Function that returns a cube
def cube(n):
    return n ** 3

print(cube(4))

# 289 - Function that checks positive number
def is_positive(n):
    return n > 0

print(is_positive(5))

# 290 - Function that returns largest value
def largest(a, b, c):
    return max(a, b, c)

print(largest(4, 9, 2))

# 291 - Function that converts Celsius
def to_fahrenheit(c):
    return c * 9 / 5 + 32

print(to_fahrenheit(25))

# 292 - Function with two default arguments
def show_person(name="Guest", city="Unknown"):
    print(name, city)

show_person()
show_person("Ali", "Bahawalpur")

# 293 - Function that counts vowels
def count_vowels(text):
    return sum(ch.lower() in "aeiou" for ch in text)

print(count_vowels("Education"))

# 294 - Function that returns factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

# 295 - Function that checks prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

# 296 - Function that returns list average
def average(values):
    return sum(values) / len(values) if values else 0

print(average([4, 8, 12]))

# 297 - Function that counts words
def word_count(sentence):
    return len(sentence.split())

print(word_count("Python is very easy"))

# 298 - Function with keyword argument
def introduce(name, course):
    print(f"{name} studies {course}")

introduce(course="Computer Science", name="Ali")

# 299 - Function returning quotient and remainder
def divide(a, b):
    return a // b, a % b

print(divide(17, 5))

# 300 - Lambda to check even
is_even = lambda n: n % 2 == 0
print(is_even(12))

# 301 - Use map to double values
nums = [1, 2, 3, 4]
print(list(map(lambda n: n * 2, nums)))

# 302 - Use filter to get odd values
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda n: n % 2 != 0, nums)))

# 303 - Recursive countdown
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# 304 - Recursive factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 305 - Recursive sum from 1 to n
def total(n):
    if n <= 0:
        return 0
    return n + total(n - 1)

print(total(5))

# 306 - Function to return initials
def initials(name):
    return "".join(part[0].upper() for part in name.split())

print(initials("Ali Khan"))

# 307 - Function to calculate percentage
def percentage(obtained, total):
    return obtained / total * 100 if total else 0

print(percentage(420, 500))

# 308 - Function to make a simple menu choice
def menu(choice):
    if choice == 1:
        return "Start"
    elif choice == 2:
        return "Settings"
    return "Exit"

print(menu(2))

# ==================================================================
# TOPIC: FILE HANDLING AND PRACTICAL BASICS
# ==================================================================

# 309 - Read text from a file
with open("notes.txt", "r") as file:
    print(file.read())

# 310 - Append a line to a file
with open("notes.txt", "a") as file:
    file.write("\nAnother line")

# 311 - Count lines in a file
with open("notes.txt", "r") as file:
    print(len(file.readlines()))

# 312 - Handle division by zero with try-except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 313 - Convert input safely to integer
text = input("Enter an integer: ")
try:
    number = int(text)
    print(number)
except ValueError:
    print("Invalid integer")

# 314 - Generate a random number
import random
print(random.randint(1, 100))

# 315 - Pick a random item
import random
items = ["red", "blue", "green"]
print(random.choice(items))

# 316 - Shuffle a list
import random
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

# 317 - Get current time
from datetime import datetime
print(datetime.now().strftime("%H:%M:%S"))

# 318 - Create a basic calculator function
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/" and b != 0:
        return a / b
    return "Invalid operation"

print(calculator(8, 2, "*"))

# 319 - Make a simple shopping total
prices = [120, 250, 80]
print("Total:", sum(prices))

# 320 - Make a simple student record
student = {"name": "Ali", "marks": 88}
print(f"{student['name']} scored {student['marks']} marks")

# 321 - Make a basic to-do list
tasks = ["Study Python", "Practice loops"]
for index, task in enumerate(tasks, 1):
    print(index, task)

# 322 - Make a simple contact dictionary
contacts = {"Ali": "03001234567", "Sara": "03007654321"}
name = input("Name: ")
print(contacts.get(name, "Contact not found"))

# 323 - Make a simple score counter
score = 0
score += 10
score += 5
score -= 3
print("Score:", score)

# 324 - Make a simple login check
saved_username = "student"
saved_password = "python123"
username = input("Username: ")
password = input("Password: ")
if username == saved_username and password == saved_password:
    print("Login successful")
else:
    print("Login failed")

# 325 - Make a simple currency calculation
amount = float(input("Amount: "))
rate = float(input("Rate: "))
print("Converted amount:", amount * rate)

# 326 - Make a simple monthly budget balance
income = float(input("Monthly income: "))
expenses = float(input("Monthly expenses: "))
print("Remaining:", income - expenses)

# 327 - Make a simple loan installment estimate
amount = float(input("Loan amount: "))
months = int(input("Months: "))
if months > 0:
    print("Monthly installment:", amount / months)

# 328 - Make a basic unit converter menu
choice = input("Convert km to m (k) or kg to g (w): ")
value = float(input("Value: "))
if choice == "k":
    print(value * 1000)
elif choice == "w":
    print(value * 1000)
else:
    print("Unknown choice")

# 329 - Make a simple password generator
import random
import string
chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(8))
print(password)

# 330 - Make a simple number guessing game
secret = 7
guess = int(input("Guess (1-10): "))
if guess == secret:
    print("Correct!")
else:
    print("Try again")

# 331 - Make a simple word guessing game
word = "python"
guess = input("Guess the word: ").lower()
print("Correct!" if guess == word else "Wrong guess")

# 332 - Make a simple attendance percentage
present = int(input("Days present: "))
total = int(input("Total days: "))
if total > 0:
    print("Attendance:", present / total * 100, "%")

# 333 - Make a simple BMI calculation
weight = float(input("Weight kg: "))
height = float(input("Height m: "))
if height > 0:
    print("BMI:", weight / height ** 2)

# 334 - Make a simple age group classifier
age = int(input("Age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# 335 - Make a simple multiplication quiz
import random
a = random.randint(1, 10)
b = random.randint(1, 10)
answer = int(input(f"{a} x {b} = "))
print("Correct" if answer == a * b else "Incorrect")

# 336 - Make a simple list-based queue
queue = []
queue.append("A")
queue.append("B")
print(queue.pop(0))
print(queue)

# 337 - Make a simple list-based stack
stack = []
stack.append("A")
stack.append("B")
print(stack.pop())
print(stack)

# 338 - Make a simple CSV-like row
name = "Ali"
age = 20
city = "Bahawalpur"
print(f"{name},{age},{city}")

# 339 - Make a simple JSON dictionary display
import json
data = {"name": "Ali", "age": 20}
print(json.dumps(data, indent=2))

# 340 - Make a simple inventory quantity check
stock = {"pen": 12, "book": 5}
item = input("Item: ").lower()
print("Quantity:", stock.get(item, 0))

# 341 - Make a simple word frequency report
sentence = input("Sentence: ").lower()
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)

# 342 - Make a simple calculator with repeat loop
while True:
    text = input("Type quit to stop: ")
    if text.lower() == "quit":
        break
    print("You typed:", text)

# ==================================================================
# TOPIC: MORE BEGINNER PRACTICE
# ==================================================================

# 343 - Check if a number is perfect
n = int(input("Number: "))
total = sum(i for i in range(1, n) if n % i == 0)
print("Perfect" if total == n else "Not perfect")

# 344 - Check if a number is abundant
n = int(input("Number: "))
total = sum(i for i in range(1, n) if n % i == 0)
print("Abundant" if total > n else "Not abundant")

# 345 - Check if number is deficient
n = int(input("Number: "))
total = sum(i for i in range(1, n) if n % i == 0)
print("Deficient" if total < n else "Not deficient")

# 346 - Convert integer to binary
n = int(input("Number: "))
print(bin(n)[2:])

# 347 - Convert binary to integer
binary = input("Binary: ")
print(int(binary, 2))

# 348 - Convert decimal to hexadecimal
n = int(input("Number: "))
print(hex(n)[2:])

# 349 - Find the most common list item
items = ["a", "b", "a", "c", "a", "b"]
print(max(set(items), key=items.count))

# 350 - Create a multiplication grid
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()