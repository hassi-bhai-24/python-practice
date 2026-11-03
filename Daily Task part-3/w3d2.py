"""
Day 2: Methods & Attributes
● Instance methods vs class attributes
● Practice: Add deposit(), withdraw() to BankAccount

Class Properties
Properties are variables that belong to a class. They store data for each object created from the class.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)



class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)



class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)



class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)



class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
class book :
 madeof= ""
 def __init__(self,name ,year):
  self.name=name
  self.year=year
b = book("notice",2013)
print(b.name,b.year)
b.year=2025
print(b.year)
book.madeof="paper"
print(b.madeof)

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)



class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)



class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)



class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)



class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")
my_playlist =  Playlist("Favourites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

#practice Question
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
acc = BankAccount(name)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)

    elif choice == "3":
        acc.show_balance()

    elif choice == "4":
        print("Thank you for using the bank system")
        break

    else:
        print("Invalid choice, try again")
#ended
#rough practice
class customer:
  def __init__(self,Cname):
    self.Cname= Cname
  def greet(self):
    print( "welcome to our online shop " +  self.Cname )
name= input("Enter your name: ") 
c1=customer(name)  
c1.greet()
a = int(input("Enter Num"))
b = int(input("Enter Num"))
class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
  def divide(self,a,b):
    return a/b
  def remainder(self,a,b):
    return a%b
calc = Calculator()
print("Addition:  ", calc.add(a, b))
print("Multiplication:  ", calc.multiply(a, b))
print("Division:  ", calc.divide(a, b))
print("remainder:  ", calc.remainder(a, b))

