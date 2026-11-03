"""
w2Day 1: Modules & Standard Library
● import statement
● random module (games)
● datetime module (timestamps)
● Practice: Rock, Paper, Scissors vs computer
"""
# 1 
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print(generate_password(16))


import random

otp = random.randint(100000, 999999)
print("Your OTP:", otp)


import random
names = ["Ali", "Sara", "Hassan", "John"]
random.shuffle(names)
print(names)


import random
print("Dice rolled:", random.randint(1, 6))



import random

ticket = random.sample(range(1, 50), 6)
print("Your ticket:", ticket)


import random

color = "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))
print(color)


import random
students = ["Ali", "Zara", "Sami", "Huda"]
print("Selected:", random.choice(students))

import random
print(random.choice(["Heads", "Tails"]))



import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(f"{a} + {b} = ?")

import random

players = ["Ali", "Zara", "Sami", "Huda", "Hamza", "Mina"]
random.shuffle(players)
team1 = players[:3]
team2 = players[3:]
print("Team 1:", team1)
print("Team 2:", team2)



import random

emojis = ["😀", "😎", "🔥", "🎉", "❤️", "🚀"]
print(random.choice(emojis))


import random
winners = random.sample(range(100), 3)
print("Winners:", winners)


from datetime import datetime

print(datetime.now())



from datetime import datetime

birth = datetime(2003, 5, 11)
today = datetime.now()
age = today.year - birth.year
print("Age:", age)


from datetime import datetime

event = datetime(2026, 1, 1)
today = datetime.now()
left = event - today
print("Days left:", left.days)


from datetime import datetime, timedelta

future = datetime.now() + timedelta(hours=5)
print(future)




import datetime

year = 2028
print(datetime.date(year, 1, 1).year % 4 == 0)


import datetime

year = 2028
print(datetime.date(year, 1, 1).year % 4 == 0)



from datetime import datetime
print("Week number:", datetime.now().isocalendar().week)



from datetime import datetime
print(datetime.timestamp(datetime.now()))


from datetime import datetime

timestamp = 1700000000
print(datetime.fromtimestamp(timestamp))



from datetime import datetime, timedelta

print(datetime.now() + timedelta(minutes=30))



from datetime import datetime

d1 = datetime(2023, 5, 1)
d2 = datetime(2024, 5, 1)

print("d2 is later:", d2 > d1)


from datetime import datetime

today = datetime.now()
start = datetime(today.year, 1, 1)
print("Days passed:", (today - start).days)



import math
print(math.sqrt(25))



import math as m
print(m.pi)



from math import sin, cos
print(sin(1), cos(1))



from math import *
print(log(10))



def hello():
    print("Hello from module!")


def area_circle(r):
    import math
    return math.pi * r * r

print(area_circle(5))

import datetime as dt
print(dt.datetime.now())



try:
    import json as json
except ImportError:
    import json

print(json.dumps({"speed": 100}))



import datetime as dt
print(dt.datetime.now())



module_name = "math"
math_mod = __import__(module_name)
print(math_mod.sqrt(49))


import os
print(os.getcwd())


import sys
print(sys.path)


import random
print(random.sample(range(1, 100), 5))


import statistics
print(statistics.mean([2, 4, 6, 8]))






#practice 
import random

ops = ["rock", "paper", "scissors"]
win = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
ps = cs = 0

print("🎮 Rock, Paper, Scissors (type 'exit' to quit)\n")

while True:
    p = input("rock/paper/scissors: ").lower()
    if p == "exit": break
    if p not in ops: print("Invalid!\n"); continue

    c = random.choice(ops)
    print("Computer:", c)

    if p == c: print("Tie!\n")
    elif win[p] == c: ps += 1; print("You win!\n")
    else: cs += 1; print("Computer wins!\n")

print(f"\nFinal Score → You: {ps} | Computer: {cs}")

