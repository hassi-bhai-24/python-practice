number = [1,2,3,4,5]
odd = [x for x in number if x%2!=0]
print(odd)
my_dict = {"a": 1, "b": 2, "c": 3}
items_view = my_dict.items() # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# It is commonly used for iterating through a dictionary:
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
    nums = [10, 20, 30, 20,1,]
result = nums.remove(1)
print(result)      # None
print(nums)        # [10, 30, 20]
def add(a, b):
    return a+b  # send result back

result = add(5, 3)
print(result)
"""def test():
    print("Before return")
    
    print("After return")   # this will NOT run
    return "no"
print(test())
def x():
    print("Hello")
    return "l"
x = input("enter greetings ")
print(x)
user_input =[]
def greet():
    print("Hello")
    return "WelCome"

user_input = input("Enter greetings: ")

print(greet())"""
#Create a list of 5 fruits. Add one more fruit, remove the second fruit, and print the final list.
f= ["a","b","c","d","e"]
f.append("f")
f.remove("b")
print(f)
#Create a tuple of 4 colors. Try printing the last color. Try changing the first color (see what happens)
t=("a","b","c","d")
print(t[2])
#t[0]="n"
print(t)
#Create a set with numbers [1, 2, 2, 3, 3, 4]. Add 5. Remove 2. Print the final set.
numbers = [1, 2, 2, 3, 3, 4]
numbers.append(5)
numbers.remove(2)
print(numbers)
#Convert the list [1, 2, 2, 3, 3, 4] into a set to remove duplicates.
list = [1, 2, 2, 3, 3, 4]
set = set(list)
print(set)
numbers = [1, 2, 2, 3, 3, 4]
tuple = tuple(numbers)
print(tuple)
colors = ("red", "green", "red", "blue")
set1 = set(colors)
print(set1)
colors = ("red", "green", "red", "blue")
list = list(colors)
print(list)