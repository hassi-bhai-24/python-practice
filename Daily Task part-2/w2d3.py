"""
Day 3: Error Handling
● try/except blocks
● Specific exception types.
● Practice: Add error handling to previous projects
"""



# 1 Divide by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# 2 Invalid integer input
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number!")

# 3 File not found
try:
    f = open("notfound.txt")
except FileNotFoundError:
    print("File does not exist.")

# 4 Index out of range
try:
    lst = [1,2,3]
    print(lst[5])
except IndexError:
    print("Index does not exist.")

# 5 Key not found
try:
    d = {"a":1}
    print(d["b"])
except KeyError:
    print("Key not found.")

# 6 Type error
try:
    print("a" + 5)
except TypeError:
    print("Wrong data type!")

# 7 Float conversion error
try:
    x = float("hello")
except ValueError:
    print("Cannot convert to float.")

# 8 Multiple errors
try:
    print(10 / int("hello"))
except (ZeroDivisionError, ValueError):
    print("Error occurred.")

# 9 Generic except
try:
    a = 10 / 0
except:
    print("Some error occurred.")

# 10 Try / Except / Finally
try:
    print(5/0)
except:
    print("Error")
finally:
    print("Program ended.")

# 11 Wrong file mode
try:
    f = open("sample.txt", "x")
except FileExistsError:
    print("File already exists.")

# 12 Import error
"""try:
    import mywrongmodule
except ModuleNotFoundError:
    print("Module not found.")
"""
# 13 Name error
try:
    print(a)
except NameError:
    print("Variable not defined.")

# 14 Directory opened as file
try:
    open("/")
except PermissionError:
    print("This is a directory, not a file.")

# 15 Writing to read-only file
try:
    f = open("readonly.txt","r")
    f.write("hello")
except IOError:
    print("Cannot write to file.")

# 16 Negative index out of range
try:
    lst = [1,2]
    print(lst[-5])
except IndexError:
    print("Index out of range.")

# 17 Dictionary get (no error)
d = {"a":10}
print(d.get("b","Key missing"))

# 18 Math domain error
import math
try:
    print(math.sqrt(-1))
except ValueError:
    print("Invalid value for sqrt.")

# 19 Convert letters to int
try:
    n = int("abc")
except ValueError:
    print("Cannot convert text to number.")

# 20 Remove item not in list
try:
    lst = [1,2,3]
    lst.remove(5)
except ValueError:
    print("Item not in list.")

# 21 Undefined function
"""try:
    hello()
except NameError:
    print("Function does not exist.")
"""
# 22 Add number + string
try:
    print(5 + "5")
except TypeError:
    print("Cannot add number and string.")

# 23 Wrong argument type
try:
    print(len(10))
except TypeError:
    print("Length not valid for numbers.")

# 24 Tuple modification error
try:
    t = (1,2,3)
    t[0] = 9
except TypeError:
    print("Tuples are immutable.")

# 25 Set indexing
try:
    s = {1,2,3}
    print(s[0])
except TypeError:
    print("Sets cannot be indexed.")

#practice
a=20
b=0
try:
    c=a/b
    print(c)
except:
 print("0 is not valid for divide ")

a = int(input("Enter your First Number: "))
b = int(input("Enter your Second Number: "))
try:
   x = a/b
   print(x)
except:
   print("You cannot divide your number with zero")
else:
   print("thanks for visit")




def add_num():
    try:
        a = int(input("Enter your First Number: "))
        b = int(input("Enter your Second Number: "))
        print("Result:", a+b)
    except:
        print("just number, nothing else")
    else:
        print("thanks for your vist") 




        
def sub_num():
    try:
       a = int(input("Enter your First Number: "))
       b = int(input("Enter your Second Number: "))
       print("Result:", a-b)
    except:
       print("just number, nothing else")
    else:
       print("Thanks for your vist") 





def Multip_num():
    try:
       a = int(input("Enter your First Number: "))
       b = int(input("Enter your Second Number: "))
       print("Result:", a*b)
    except:
       print("just number, nothing else")
    else:
       print("Thanks for your vist")
       






def Divid_num():
    try:
       a = int(input("Enter your First Number: "))
       b = int(input("Enter your Second Number: "))
       print("Result:", a/b)
    except ZeroDivisionError :
       print("You cannot Divide your num by zero")
    except: 
       print("Just Number, Nothing else")
    else:
       print("Thanks for your vist") 











def menu():
    print("*****WELCOME*****")
    print("Just Click the Number of Function you want to Perform")
    while True :
        print("1.Addition ")
        print("2.Multiplication")
        print("3.Subtraction")
        print("4.Division")
        print("5.Exit")
     
        choice = input("Enter your choice:  ")
      
        if choice == "1" :
             add_num()
        elif choice == "2":
             Multip_num()
        elif choice=="3":
             sub_num()
        elif choice=="4":
             Divid_num()
        elif choice =="5":     
             print("Exiting the Program")
             break;
        else:
         print("Invalid Choice")
menu()


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

# practice 
import random

ops = ["rock", "paper", "scissors"]
win = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
ps = cs = 0

print("🎮 Rock, Paper, Scissors (type 'exit' to quit)\n")

while True:
    try:
        p = input("rock/paper/scissors: ").lower()
    except Exception:
        print("Invalid option")
        continue

    if p == "exit":
        break

    if p not in ops:
        print("Please enter rock, paper, or scissors!")
        continue

    c = random.choice(ops)
    print("Computer:", c)

    try:
        if p == c:
            print("Tie!\n")
        elif win[p] == c:
            ps += 1
            print("You win!\n")
        else:
            cs += 1
            print("Computer wins!\n")
    except Exception:
        print("Unexpected error")

print(f"\nFinal Score → You: {ps} | Computer: {cs}")

