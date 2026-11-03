"""
Advanced Data Structures
● List comprehensions
● Tuples and sets
● Practice: Data processing exercises
"""

#1 – List comprehension: square numbers
squares = [x*x for x in range(1, 11)]
print(squares)

#2 – List comprehension: even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

#3 – List comprehension: odd numbers
odds = [x for x in range(20) if x % 2 != 0]
print(odds)

#4 – Convert list of strings to uppercase
words = ["apple", "banana", "mango"]
upper_words = [w.upper() for w in words]
print(upper_words)

#5 – Extract first letter of each word
first_letters = [w[0] for w in words]
print(first_letters)

#6 – List of numbers divisible by 3
div3 = [x for x in range(1, 51) if x % 3 == 0]
print(div3)

#7 – Create list of (number, square)
pairs = [(x, x*x) for x in range(1, 11)]
print(pairs)

#8 – Flatten a 2D list into 1 list
matrix = [[1,2], [3,4], [5,6]]
flat = [num for row in matrix for num in row]
print(flat)

#9 – List comprehension with condition + expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)

#10 – Remove vowels from string
text = "programming"
no_vowels = [c for c in text if c not in "aeiou"]
print(no_vowels)

#11 – Generate list of squares only for even numbers
even_squares = [x*x for x in range(20) if x % 2 == 0]
print(even_squares)

#12 – Convert numbers to strings
nums = [1,2,3,4]
as_strings = [str(n) for n in nums]
print(as_strings)

#13 – Reverse each string using list comprehension
rev = [w[::-1] for w in words]
print(rev)

#14 – Extract only digits from a string
txt = "abc123xyz"
digits = [c for c in txt if c.isdigit()]
print(digits)

#15 – Create list of booleans
bools = [x > 5 for x in range(10)]
print(bools)

#16 – Cartesian product using list comprehension
prod = [(x,y) for x in [1,2] for y in [3,4]]
print(prod)

#17 – Convert list of names to title case
names = ["john", "david", "sam"]
titles = [n.title() for n in names]
print(titles)

#18 – Filter only long words
long = [w for w in names if len(w) > 3]
print(long)

#19 – Remove duplicates using list comprehension + set
dups = [1,1,2,2,3,3]
unique = list({x for x in dups})
print(unique)

#20 – List comprehension with enumerate
indexed = [(i, w) for i, w in enumerate(words)]
print(indexed)


#21 – Create a tuple
t1 = (10, 20, 30)
print(t1)

#22 – Tuple indexing
print(t1[1])

#23 – Tuple slicing
print(t1[:2])

#24 – Tuple concatenation
t2 = (40, 50)
print(t1 + t2)

#25 – Tuple repetition
print(t1 * 2)

#26 – Check membership
print(20 in t1)

#27 – Tuple unpacking
a, b, c = t1
print(a, b, c)

#28 – Swap variables using tuple
x, y = 5, 10
x, y = y, x
print(x, y)

#29 – Nested tuple
nested = (1, (2, 3), 4)
print(nested[1][1])

#30 – Convert list to tuple
lst = [1,2,3]
print(tuple(lst))

#31 – Convert tuple to list
print(list(t1))

#32 – Count occurrences in tuple
t3 = (1,2,3,1,1)
print(t3.count(1))

#33 – Find index in tuple
print(t3.index(2))

#34 – Tuple inside loop
for item in t1:
    print(item)

#35 – Tuple of tuples
coords = ((1,2), (3,4))
print(coords)

#36 – Store student record in tuple
student = ("Ali", 22, "CS")
print(student)

#37 – Check if tuple is immutable
try:
    student[0] = "John"
except:
    print("Tuples are immutable")

#38 – Tuple with mixed data types
mix = ("apple", 10, True, 5.6)
print(mix)

#39 – Tuple packing
t = 1, 2, 3
print(t)

#40 – Using tuple as dictionary key
d = {(1,2): "point"}
print(d[(1,2)])



#41 – Create a set
s = {1,2,3,3,3}
print(s)

#42 – Add element to set
s.add(4)
print(s)

#43 – Remove element
s.remove(2)
print(s)

#44 – Discard element (no error)
s.discard(10)
print(s)

#45 – Union of sets
a = {1,2,3}
b = {3,4,5}
print(a | b)

#46 – Intersection
print(a & b)

#47 – Difference
print(a - b)

#48 – Symmetric difference
print(a ^ b)

#49 – Check membership
print(3 in a)

#50 – Convert list to set to remove duplicates
l = [1,1,2,2,3]
print(set(l))

#51 – Set comprehension
sq = {x*x for x in range(6)}
print(sq)

#52 – Frozen set (immutable set)
fs = frozenset([1,2,3])
print(fs)

#53 – Checking subset
print({1,2}.issubset(a))

#54 – Checking superset
print(a.issuperset({1}))

#55 – Find unique characters in string
chars = set("banana")
print(chars)

#56 – Loop through set
for item in a:
    print(item)

#57 – Remove duplicates from sentence
sentence = "python python is great great"
unique_words = set(sentence.split())
print(unique_words)




#58 – Count words in sentence
s = "this is a simple simple test"
counts = {w: s.split().count(w) for w in set(s.split())}
print(counts)

#59 – Filter numbers > 10
nums = [5, 12, 18, 3, 25]
filtered = [x for x in nums if x > 10]
print(filtered)

#60 – Extract emails from list
data = ["hello", "abc@gmail.com", "nope", "test@yahoo.com"]
emails = [x for x in data if "@" in x]
print(emails)

#61 – Create dict of (num: square)
d = {x: x*x for x in range(1, 11)}
print(d)

#62 – Remove stopwords from string
sentence = "this is a python course"
stop = {"is", "a"}
clean = [w for w in sentence.split() if w not in stop]
print(clean)

#63 – Count vowels in string
text = "programming"
vowels = [c for c in text if c in "aeiou"]
print(len(vowels))

#64 – Numbers from list that appear only once
data = [1,2,2,3,4,4,5]
unique_once = [x for x in data if data.count(x) == 1]
print(unique_once)

#65 – Convert sentence into (word, length) pairs
sentence = "python programming is fun"
print( [(w, len(w)) for w in sentence.split()])

#rough practice 
alp = [1,2,3,4]
r=[x*x for x in alp]
print(r)
alpha = [1,2,3,4,5,6,7,8,9,10]
even=[x for x in alpha if x%2==0]
print(even)
zlpha = [1,2,3,4,5,6,7,8,9,10]
div3=[x for x in zlpha if x%3==0]
print(div3)

print([x*x for x in range(1,21)])
print([x for x in range(1,25) if x%3==0])
list1=[3,6,9,12,15,18,21,24]
print([x for x in list1 if x%2==0])
list2 =["apple", "banana", "kiwi"]
print([f.upper() for f in list2])
list3 =["Ali", "Sara", "Ahsan", "Bilal"]
result =[name for name in list3 if name.startswith("A")]
print(result)
txt = "this is a book"
result = [word[0] for word in txt.split()]
print(result)
print([x for x in range(1,101) if x%3 and x%5 ==0 ])
list4= [0, 20, 30, 40]
print([x for x in list4 if 	(x * 9/5) + 32 == 0 ])
list4 = [0, 20, 30, 40]
result = [x for x in list4 if (x * 9/5) + 32 == 0]
print(result)
celsius = [0, 20, 30, 40]

fahrenheit = [round((c * 9/5) + 32, 1) for c in celsius]

print(fahrenheit)


fahrenheit = [ round((f * 9/5) + 32, 1) for f in range(1,101) ]
celsius = [c for c in range(1,101)]
combined= [(c,f) for c,f in zip(celsius,fahrenheit) ]
print(combined)


list5= [-5, 3, -1, 10, -20, 8]
r = [x for x in list5 if x >= 0 ]
print(r)



list6= [1,2,3,4]
ans = {x:x**2 for x in list6}
print(ans)