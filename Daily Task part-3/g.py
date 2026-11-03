"""pname=[]
price=[]
class product: 
 def __init__(self,pname,price):
  self.pname=pname
  self.price=price

 #pname=input("Enter the Product name; ")
 #price=int(input("Enter the Price: "))

print("Data has been stored in their respective lists") 
class entryof(product):
 def __init__(self, pname, price, exdate = "1year"):
  super().__init__(pname, price)
  self.exdate = exdate

  #price=int(input("Enter the Price: "))
 def last(self):
  print(self.pname, "has", self.exdate , "of expiry date.",self.price,"$ is its price")
  obj = entryof("book",2020)
  obj.last()


class data_entry:
 def get_data(self):
  self.name = input("Enter you name: ")
  self.age = input("Enter your age: ")
class student(data_entry): 
 def showdata(self):
  super().get_data()
  print("My name is",self.name,"and age is", self.age)
s =student()   
s.showdata()"""


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
class person(BankAccount):
    def __init__(self, name, balance=0):
       super().__init__(name, balance)
obj = person("Ali",20)   
obj.show_balance()   
       