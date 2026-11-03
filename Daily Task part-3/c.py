"""
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


# -------- Main Program --------
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

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


# Create object
calc = Calculator()

# Call methods
print("Addition:", calc.add(a, b))
print("Multiplication:", calc.multiply(a, b))


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
def add():
    return 5+2

x2 = add()
print(x2)

def check(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"
n = int(input("Enter num: "))
print(check(n))

s="                            pyhon"
print(s)
try:
  x = int(input("Enter Num: "))
  square = lambda x: x * x
  print(square(x))
except:
  print("Invalid Number")
finally:
  print("bye bye")

class num: 
   def __init__(self):
       self._marks= int(input("Enter Num: "))
s = num()
print("Your Marks:", s._marks)
    
with open("marks.txt", "a") as file:
  file.write(f"Marks: {s._marks}\n")
class Dog:
    def __init__(self, name):
        self.name = "max"
    
    def bark(self):
        return f"{self.name} says Woof!"  """ 
class Dog:
    species = "Canine"  # Class attribute
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def is_pet():
        return True