"""
Day 2: File Handling (I/O)
● open(), read(), write(), close()
● with statement (context manager)
● Practice: Make to-do list persistent with file storage
"""

# PROGRAM 1: Write to a file
f = open('greet.txt', 'w')
f.write('Hello, File Handling World!\n')
f.close()

# PROGRAM 2: Read a file
try:
    f = open('greet.txt', 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Run program 1 first.")

# PROGRAM 3: Append to a file
f = open('greet.txt', 'a')
f.write('This line was appended.\n')
f.close()

# PROGRAM 4: Read updated file
f = open('greet.txt', 'r')
print(f.read())
f.close()

# PROGRAM 5: Write using with
with open('write.txt', 'w') as f:
    f.write("The with statement ensures auto close.\n")

# PROGRAM 6: Read using with
with open('write.txt', 'r') as f:
    print(f.read())

# PROGRAM 7: Write & read line by line
with open('multiline.txt', 'w') as f:
    f.write("First line.\nSecond line.\nThird line.\n")

with open('multiline.txt', 'r') as f:
    for line in f:
        print(line.strip())

# PROGRAM 8: Read first line only
with open('multiline.txt', 'r') as f:
    print(f.readline())

# PROGRAM 9: Read all lines as list
with open('multiline.txt', 'r') as f:
    print(f.readlines())

# PROGRAM 10: Write list of strings
with open('fruits.txt', 'w') as f:
    f.writelines(["Apple\n", "Banana\n", "Cherry\n"])

# PROGRAM 11: Count lines
count = 0
with open('fruits.txt', 'r') as f:
    for _ in f:
        count += 1
print(count)

# PROGRAM 12: Count characters
with open('fruits.txt', 'r') as f:
    print(len(f.read()))

# PROGRAM 13: Ignore empty lines
with open('mixed.txt', 'w') as f:
    f.write("Line1\n\nLine2\n \nLine3")

with open('mixed.txt', 'r') as f:
    for line in f:
        if line.strip():
            print(line.strip())

# PROGRAM 14: Uppercase to new file
with open('greet.txt', 'r') as f:
    data = f.read().upper()
with open('P14_uppercase.txt', 'w') as f:
    f.write(data)

# PROGRAM 15: Append user line
with open('user_log.txt', 'a') as f:
    f.write("User added this line.\n")

# PROGRAM 16: Catch file not found
try:
    open('no_file.txt', 'r')
except FileNotFoundError:
    print("File not found!")

# PROGRAM 17: Write numbers
with open('numbers.txt', 'w') as f:
    for n in [10,20,30,40,50]:
        f.write(str(n)+"\n")

# PROGRAM 18: Sum numbers
total = 0
with open('numbers.txt', 'r') as f:
    for line in f:
        total += int(line)
print(total)

# PROGRAM 19: Copy file content
with open('greet.txt', 'r') as f:
    x = f.read()
with open('copy.txt', 'w') as f:
    f.write(x)

# PROGRAM 20: CSV read column
with open('data.csv', 'w') as f:
    f.write("Name,Age,City\nAlice,25,NY\nBob,30,LA\nCharlie,22,SF")

with open('data.csv', 'r') as f:
    f.readline()
    for line in f:
        print(line.split(',')[0])

# PROGRAM 21: Count word 'the'
with open('multiline.txt', 'r') as f:
    words = f.read().lower().split()
print(words.count("the"))

# PROGRAM 22: Prepend text
with open('write.txt', 'r') as f:
    old = f.read()
with open('write.txt', 'w') as f:
    f.write("*** NEW HEADER ***\n" + old)

# PROGRAM 23: Read binary
with open('greet.txt', 'rb') as f:
    print(f.read())

# PROGRAM 24: Read first 10 chars
with open('greet.txt', 'r') as f:
    print(f.read(10))

# PROGRAM 25: Create empty file
open('empty.txt', 'w').close()

# PROGRAM 26: Read lines starting with 'This'
with open('greet.txt', 'r') as f:
    for x in f:
        if x.startswith("This"):
            print(x)

# PROGRAM 27: Write dictionary
with open('dict.txt', 'w') as f:
    f.write("name: Leo\nsport: Football\nage: 38\n")

# PROGRAM 28: Read dictionary back
d = {}
with open('dict.txt', 'r') as f:
    for x in f:
        k,v = x.strip().split(":")
        d[k] = v
print(d)

# PROGRAM 29: Filter word
with open('multiline.txt', 'r') as f, open('P29_filtered.txt', 'w') as out:
    for line in f:
        if "line" in line.lower():
            out.write(line)

# PROGRAM 30: Encoding write
with open('latin.txt', 'w', encoding='latin-1') as f:
    f.write("Special char: é")

# PROGRAM 31: Encoding read
with open('latin.txt', 'r', encoding='latin-1') as f:
    print(f.read())

# PROGRAM 32: File counter
try:
    c = int(open('counter.txt').read())
except:
    c = 0
open('counter.txt','w').write(str(c+1))

# PROGRAM 33: Read last line
with open('multiline.txt', 'r') as f:
    print(f.readlines()[-1])

# PROGRAM 34: Simple log
import datetime
with open('app_log.txt','a') as f:
    f.write(str(datetime.datetime.now()) + " Logged\n")

# PROGRAM 35: Read line 2
with open('multiline.txt', 'r') as f:
    print(f.readlines()[1].strip())

# PROGRAM 36: Replace word
with open('multiline.txt', 'r') as f:
    data = f.read().replace("First", "Alpha")
open('P36_replaced.txt','w').write(data)

# PROGRAM 37: Check closed
f = open('check.txt','w')
print(f.closed)
f.close()
print(f.closed)

# PROGRAM 38: Readable?
"""
with open('read_check.txt','r') as f:
    print(f.readable())

"""

# PROGRAM 39: Writable?
with open('write_check.txt','w') as f:
    print(f.writable())

# PROGRAM 40: Write poem
with open('poem.txt','w') as f:
    f.write("The file is open wide...\n")

# PROGRAM 41: Strip whitespace while reading
with open('multiline.txt','r') as f:
    for x in f:
        print(x.strip())

# PROGRAM 42: Reverse content
with open('greet.txt','r') as f:
    txt = f.read()[::-1]
open('P42_reversed.txt','w').write(txt)

# PROGRAM 43: tell() file pointer
with open('greet.txt','r') as f:
    print(f.tell())
    f.read(5)
    print(f.tell())

# PROGRAM 44: seek() position
with open('greet.txt','r') as f:
    f.seek(7)
    print(f.read())

# PROGRAM 45: Write numbers with list comprehension
with open('range.txt','w') as f:
    f.writelines([str(n)+"\n" for n in range(1,6)])

# PROGRAM 46: Double numbers
out = []
with open('numbers.txt','r') as f:
    for line in f:
        out.append(str(int(line)*2)+"\n")
open('P46_doubled.txt','w').writelines(out)

# PROGRAM 47: r+ mode
open('rplus.txt','w').write("0123456789\n")
with open('rplus.txt','r+') as f:
    f.read()
    f.write("---END---")

# PROGRAM 48: Write multiple user lines
lines = ["First line","Second line","Last line"]
with open('multi_input.txt','w') as f:
    for x in lines:
        f.write(x+"\n")

# PROGRAM 49: Count unique words
with open('multiline.txt','r') as f:
    words = f.read().lower().split()
print(len(set(words)))

# PROGRAM 50: Reverse line order
with open('multiline.txt','r') as f:
    lines = f.readlines()
open('P50_rev_order.txt','w').writelines(lines[::-1])


#practice 
FILE = "tasks.txt"

# Load tasks
def load():
    try:
        return open(FILE).read().splitlines()
    except:
        return []

# Save tasks
def save(tasks):
    open(FILE, "w").write("\n".join(tasks))

tasks = load()

def add():
    tasks.append(input("Task: "))
    save(tasks)
    print("Added!")

def show():
    if not tasks:
        print("No tasks.")
    else:
        [print(f"{i+1}. {t}") for i, t in enumerate(tasks)]

def done():
    show()
    if tasks:
        n = int(input("Number: ")) - 1
        if 0 <= n < len(tasks):
            print(f"Done: {tasks.pop(n)}")
            save(tasks)

while True:
    print("\n1.Add  2.Show  3.Done  4.Exit")
    c = input("Choice: ")

    if c == "1":   add()
    elif c == "2": show()
    elif c == "3": done()
    elif c == "4": break
    else: print("Invalid!")
