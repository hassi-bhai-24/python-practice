
# ==================================================================
# TOPIC: IF / ELSE PRACTICE
# ==================================================================

# 170 - Check if divisible by 3 and 5
n = int(input("Number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

# 171 - Check whether two numbers are equal
a = int(input("A: "))
b = int(input("B: "))
if a == b:
    print("Equal")
else:
    print("Not equal")

# 172 - Find smallest of two numbers
a = int(input("A: "))
b = int(input("B: "))
print(min(a, b))

# 173 - Check if character is uppercase
ch = input("Character: ")
print("Uppercase" if ch.isupper() else "Not uppercase")

# 174 - Check if character is lowercase
ch = input("Character: ")
print("Lowercase" if ch.islower() else "Not lowercase")

# 175 - Check whether a person can get a discount
age = int(input("Age: "))
if age < 12 or age >= 60:
    print("Discount available")
else:
    print("No discount")

# 176 - Check if a number is within 10 to 50
n = int(input("Number: "))
if 10 <= n <= 50:
    print("Inside range")
else:
    print("Outside range")

# 177 - Classify temperature
temp = float(input("Temperature: "))
if temp < 10:
    print("Cold")
elif temp < 25:
    print("Mild")
else:
    print("Hot")

# 178 - Check pass with two subjects
maths = int(input("Maths marks: "))
english = int(input("English marks: "))
if maths >= 40 and english >= 40:
    print("Pass")
else:
    print("Fail")

# 179 - Classify triangle by sides
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# 180 - Check if a year is a century year
year = int(input("Year: "))
print("Century year" if year % 100 == 0 else "Not a century year")

# 181 - Check if number is a two-digit number
n = int(input("Number: "))
print("Two digits" if 10 <= abs(n) <= 99 else "Not two digits")

# 182 - Check if a letter is a vowel ignoring case
ch = input("Letter: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

# 183 - Simple ATM withdrawal check
balance = 5000
amount = int(input("Withdraw amount: "))
if 0 < amount <= balance:
    print("Withdrawal allowed")
else:
    print("Invalid amount")

# 184 - Calculate electricity bill by units
units = int(input("Units: "))
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10
print("Bill:", bill)

# 185 - Choose a greeting by time
hour = int(input("Hour (0-23): "))
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")

# 186 - Check if a number is between two values
n = int(input("Number: "))
low = int(input("Lower bound: "))
high = int(input("Upper bound: "))
print("Inside" if low <= n <= high else "Outside")

# 187 - Check whether a string is empty
text = input("Enter text: ")
if text == "":
    print("Empty")
else:
    print("Not empty")

# ==================================================================
# TOPIC: LOOPS AND NUMBER PRACTICE
# ==================================================================

# 188 - Print numbers from 1 to user limit
limit = int(input("Limit: "))
for i in range(1, limit + 1):
    print(i)

# 189 - Print multiples of 4
for i in range(4, 41, 4):
    print(i)

# 190 - Sum odd numbers from 1 to 30
total = 0
for i in range(1, 31, 2):
    total += i
print(total)

# 191 - Print multiplication table from input
n = int(input("Number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 192 - Factorial using while loop
n = int(input("Number: "))
result = 1
while n > 1:
    result *= n
    n -= 1
print(result)

# 193 - Print numbers skipping multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# 194 - Stop loop when number is 7
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 195 - Find product of numbers 1 to 5
product = 1
for i in range(1, 6):
    product *= i
print(product)

# 196 - Print cubes from 1 to 10
for i in range(1, 11):
    print(i ** 3)

# 197 - Find sum of digits from input
n = abs(int(input("Number: ")))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

# 198 - Count digits in an integer
n = abs(int(input("Number: ")))
count = 1 if n == 0 else 0
while n > 0:
    count += 1
    n //= 10
print(count)

# 199 - Print a number in reverse
n = int(input("Number: "))
print(str(n)[::-1])

# 200 - Check number palindrome with string
n = input("Number: ")
print("Palindrome" if n == n[::-1] else "Not palindrome")

# 201 - Find all factors of a number
n = int(input("Number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# 202 - Check prime using square root limit
n = int(input("Number: "))
prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
print("Prime" if prime else "Not prime")

# 203 - Print primes from 1 to 50
for n in range(2, 51):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n, end=" ")

# 204 - Print Fibonacci terms from user input
terms = int(input("Number of terms: "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

# 205 - Check Armstrong number (3 digits)
n = int(input("Three-digit number: "))
total = sum(int(d) ** 3 for d in str(n))
print("Armstrong" if total == n else "Not Armstrong")

# 206 - Print all three-digit Armstrong numbers
for n in range(100, 1000):
    if sum(int(d) ** 3 for d in str(n)) == n:
        print(n)

# 207 - Find HCF using loop
a = int(input("A: "))
b = int(input("B: "))
while b:
    a, b = b, a % b
print("HCF:", a)

# 208 - Print a right angle star pattern
for i in range(1, 6):
    print("*" * i)

# 209 - Print inverted star pattern
for i in range(5, 0, -1):
    print("*" * i)

# 210 - Print a number staircase
for i in range(1, 6):
    print(str(i) * i)

# 211 - Print a hollow square
for i in range(5):
    for j in range(5):
        print("*" if i in (0, 4) or j in (0, 4) else " ", end="")
    print()

# 212 - Print a simple diamond pattern
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))
for i in range(3, 0, -1):
    print(" " * (4 - i) + "*" * (2 * i - 1))

# 213 - Find sum of squares from 1 to n
n = int(input("Limit: "))
print(sum(i * i for i in range(1, n + 1)))