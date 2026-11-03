"""
Basic Python Practice 
● Variables and maths
● if / else
● Loops and patterns
● Strings
● Lists and list comprehensions
● Tuples and sets
● Dictionaries
● Simple functions
"""

#1 – Print hello world
print("Hello, World!")

#2 – Print a name
name = "Ali"
print(name)

#3 – Store age in a variable
age = 20
print("Age:", age)

#4 – Add two numbers
a = 10
b = 5
print(a + b)

#5 – Subtract two numbers
print(a - b)

#6 – Multiply two numbers
print(a * b)

#7 – Divide two numbers
print(a / b)

#8 – Floor division and remainder
print(17 // 5)
print(17 % 5)

#9 – Power of a number
print(2 ** 5)

#10 – Area of rectangle
length = 8
width = 5
print(length * width)

#11 – Area of circle
r = 7
print(3.14 * r * r)

#12 – Perimeter of square
side = 6
print(4 * side)

#13 – Average of three numbers
n1 = 10
n2 = 20
n3 = 30
print((n1 + n2 + n3) / 3)

#14 – Swap two variables
x = 5
y = 10
x, y = y, x
print(x, y)

#15 – Celsius to Fahrenheit
c = 37
f = (c * 9/5) + 32
print(f)

#16 – Check data types
print(type(10))
print(float(3.5))
print(type("hello"))
print(type(True))

#17 – Convert string to integer
num = "25"
print(int(num) + 5)

#18 – Even or odd
n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#19 – Positive, negative or zero
n = -4
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#20 – Largest of two numbers
a = 15
b = 9
if a > b:
    print(a)
else:
    print(b)

#21 – Largest of three numbers
a = 12
b = 45
c = 30
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#22 – Leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#23 – Voting eligibility
age = 19
if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")

#24 – Grade from marks
marks = 85
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

#25 – Pass or fail
marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#26 – Vowel or consonant
ch = "e"
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#27 – Divisible by 5
n = 25
if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#28 – Check number in a range
n = 50
if n >= 1 and n <= 100:
    print("In range")
else:
    print("Out of range")

#29 – Simple calculator
a = 8
b = 2
op = "*"
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)

#30 – Comparison operators
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 3)

#31 – Print 1 to 10
for i in range(1, 11):
    print(i)

#32 – Print 10 to 1
for i in range(10, 0, -1):
    print(i)

#33 – Even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

#34 – Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

#35 – Sum of 1 to 10
total = 0
for i in range(1, 11):
    total = total + i
print(total)

#36 – Factorial of 5
fact = 1
for i in range(1, 6):
    fact = fact * i
print(fact)

#37 – Table of 5
for i in range(1, 11):
    print(5 * i)

#38 – Table of 7 with f-string
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

#39 – Sum of digits
n = 1234
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10
print(total)

#40 – Reverse a number
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)

#41 – Count digits of a number
n = 98765
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print(count)

#42 – Palindrome number
n = 121
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10
if rev == n:
    print("Palindrome")
else:
    print("Not palindrome")

#43 – Prime number check
n = 7
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print(prime)

#44 – Prime numbers up to 30
for n in range(2, 31):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n, end=" ")
print()

#45 – Fibonacci series (10 terms)
a = 0
b = 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

#46 – Power using loop
base = 3
exp = 4
result = 1
for i in range(exp):
    result = result * base
print(result)

#47 – While loop from 1 to 5
i = 1
while i <= 5:
    print(i)
    i = i + 1

#48 – Using break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#49 – Using continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

#50 – Squares of 1 to 10 using loop
for i in range(1, 11):
    print(i * i)

#51 – Star triangle
for i in range(1, 6):
    print("*" * i)

#52 – Number triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#53 – Star square
for i in range(4):
    print("* * * *")

#54 – Pyramid
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

#55 – Factors of 12
n = 12
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

#56 – GCD of two numbers
a = 24
b = 36
while b != 0:
    a, b = b, a % b
print(a)

#57 – Sum of even numbers from 1 to 50
total = 0
for i in range(1, 51):
    if i % 2 == 0:
        total = total + i
print(total)

#58 – Multiples of 3 up to 30
for i in range(3, 31, 3):
    print(i)

#59 – Countdown using while
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Go!")

#60 – Loop through a string
for ch in "python":
    print(ch)

#61 – Length of a string
s = "programming"
print(len(s))

#62 – Uppercase
print(s.upper())

#63 – Lowercase
print("HELLO".lower())

#64 – Title and capitalize
print("hello world".title())
print("hello world".capitalize())

#65 – First and last character
print(s[0])
print(s[-1])

#66 – String slicing
print(s[0:4])
print(s[3:])
print(s[:6])

#67 – Reverse a string
print(s[::-1])

#68 – Palindrome string
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

#69 – Count a character
print(s.count("m"))

#70 – Count vowels
count = 0
for ch in s:
    if ch in "aeiou":
        count = count + 1
print(count)

#71 – Replace in a string
print("I like java".replace("java", "python"))

#72 – Split a sentence
sentence = "python is easy to learn"
print(sentence.split())

#73 – Join words
words = ["python", "is", "fun"]
print(" ".join(words))

#74 – Remove extra spaces
print("   hello   ".strip())

#75 – Find a word in a string
print(sentence.find("easy"))

#76 – startswith and endswith
print(sentence.startswith("python"))
print(sentence.endswith("learn"))

#77 – isdigit and isalpha
print("123".isdigit())
print("abc".isalpha())

#78 – Concatenate strings
first = "Ali"
last = "Khan"
print(first + " " + last)

#79 – Repeat a string
print("ha" * 3)

#80 – f-string
name = "Sara"
age = 21
print(f"My name is {name} and I am {age} years old")

#81 – Create a list
fruits = ["apple", "banana", "mango"]
print(fruits)

#82 – Access list items
print(fruits[0])
print(fruits[-1])

#83 – List slicing
nums = [10, 20, 30, 40, 50]
print(nums[1:4])

#84 – Append to list
fruits.append("orange")
print(fruits)

#85 – Insert into list
fruits.insert(1, "grapes")
print(fruits)

#86 – Remove from list
fruits.remove("banana")
print(fruits)

#87 – Pop from list
fruits.pop()
print(fruits)

#88 – Sort a list
nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)

#89 – Reverse a list
nums.reverse()
print(nums)

#90 – Length of list
print(len(nums))

#91 – Sum, max and min
print(sum(nums))
print(max(nums))
print(min(nums))

#92 – Count in list
data = [1, 2, 2, 3, 2]
print(data.count(2))

#93 – Index of an item
print(data.index(3))

#94 – Join two lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)

#95 – Loop through list
for f in fruits:
    print(f)

#96 – Check item in list
print("apple" in fruits)

#97 – Sum of list using loop
nums = [4, 8, 15, 16, 23, 42]
total = 0
for n in nums:
    total = total + n
print(total)

#98 – Largest number using loop
big = nums[0]
for n in nums:
    if n > big:
        big = n
print(big)

#99 – Count even and odd numbers
even = 0
odd = 0
for n in nums:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(even, odd)

#100 – Square each number
for n in nums:
    print(n * n)

#101 – Remove duplicates from list
data = [1, 2, 2, 3, 3, 4]
new = []
for d in data:
    if d not in new:
        new.append(d)
print(new)

#102 – Second largest number
nums = [10, 40, 30, 20]
nums.sort()
print(nums[-2])

#103 – Copy a list
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)

#104 – List of lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print(matrix[1][0])

#105 – Sort in descending order
nums = [3, 8, 1, 9]
nums.sort(reverse=True)
print(nums)

#106 – List comprehension: squares
squares = [x * x for x in range(1, 11)]
print(squares)

#107 – List comprehension: even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

#108 – List comprehension: uppercase words
words = ["apple", "banana", "mango"]
print([w.upper() for w in words])

#109 – List comprehension: length of words
print([len(w) for w in words])

#110 – List comprehension: numbers greater than 10
nums = [5, 12, 18, 3, 25]
print([x for x in nums if x > 10])

#111 – List comprehension: (number, square) pairs
print([(x, x * x) for x in range(1, 6)])

#112 – List comprehension: digits from a string
txt = "abc123xyz"
print([c for c in txt if c.isdigit()])

#113 – List comprehension: even or odd labels
print(["even" if x % 2 == 0 else "odd" for x in range(6)])

#114 – List comprehension: first letters
print([w[0] for w in words])

#115 – List comprehension: convert to strings
print([str(x) for x in [1, 2, 3]])

#116 – Create a tuple
t = (10, 20, 30, 40)
print(t)

#117 – Tuple indexing
print(t[0])
print(t[-1])

#118 – Tuple slicing
print(t[1:3])

#119 – Join two tuples
print(t + (50, 60))

#120 – Count in tuple
t2 = (1, 2, 3, 1, 1)
print(t2.count(1))

#121 – Index in tuple
print(t2.index(3))

#122 – Tuple unpacking
a, b, c, d = t
print(a, b, c, d)

#123 – Tuple to list and back
lst = list(t)
lst.append(50)
print(tuple(lst))

#124 – Tuples cannot be changed
try:
    t[0] = 99
except:
    print("Tuples are immutable")

#125 – Loop through a tuple
for item in t:
    print(item)

#126 – Create a set
s = {1, 2, 3, 3, 3}
print(s)

#127 – Add to a set
s.add(4)
print(s)

#128 – Remove from a set
s.remove(2)
print(s)

#129 – Union of sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

#130 – Intersection of sets
print(a & b)

#131 – Difference of sets
print(a - b)

#132 – Unique items from a list
data = [1, 1, 2, 2, 3]
print(set(data))

#133 – Unique characters in a string
print(set("banana"))

#134 – Check item in a set
print(3 in a)

#135 – Subset check
print({1, 2}.issubset(a))

#136 – Create a dictionary
student = {"name": "Ali", "age": 20, "course": "CS"}
print(student)

#137 – Access dictionary values
print(student["name"])
print(student.get("age"))

#138 – Add a new key
student["city"] = "Bahawalpur"
print(student)

#139 – Update a value
student["age"] = 21
print(student)

#140 – Delete a key
del student["course"]
print(student)

#141 – Loop through keys and values
for key in student:
    print(key, student[key])

#142 – Dictionary items, keys, values
print(student.keys())
print(student.values())
print(student.items())

#143 – Check if key exists
print("name" in student)

#144 – Count words using dictionary
sentence = "this is a simple simple test"
counts = {}
for w in sentence.split():
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
print(counts)

#145 – Dictionary comprehension
d = {x: x * x for x in range(1, 6)}
print(d)

#146 – Simple function
def greet():
    print("Hello!")

greet()

#147 – Function with return
def add(a, b):
    return a + b

print(add(5, 3))

#148 – Function to check even or odd
def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(10))

#149 – Function with default argument
def welcome(name="friend"):
    print("Welcome", name)

welcome()
welcome("Ali")

#150 – Lambda function
square = lambda x: x * x
print(square(6))