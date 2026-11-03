
# ==================================================================
# TOPIC: STRING PRACTICE
# ==================================================================

# 214 - Count uppercase letters
text = input("Text: ")
print(sum(ch.isupper() for ch in text))

# 215 - Count lowercase letters
text = input("Text: ")
print(sum(ch.islower() for ch in text))

# 216 - Count spaces in a sentence
text = input("Sentence: ")
print(text.count(" "))

# 217 - Count punctuation marks
text = input("Text: ")
marks = ".,!?:;"
print(sum(ch in marks for ch in text))

# 218 - Remove vowels from a string
text = input("Text: ")
print("".join(ch for ch in text if ch.lower() not in "aeiou"))

# 219 - Replace spaces with hyphens
text = input("Sentence: ")
print(text.replace(" ", "-"))

# 220 - Capitalize each word
text = input("Sentence: ")
print(text.title())

# 221 - Check if string contains a digit
text = input("Text: ")
print(any(ch.isdigit() for ch in text))

# 222 - Check if string is alphanumeric
text = input("Text: ")
print(text.isalnum())

# 223 - Find first occurrence of a character
text = input("Text: ")
ch = input("Character: ")
print(text.find(ch))

# 224 - Find last occurrence of a character
text = input("Text: ")
ch = input("Character: ")
print(text.rfind(ch))

# 225 - Reverse words in a sentence
text = input("Sentence: ")
print(" ".join(text.split()[::-1]))

# 226 - Check two strings are anagrams
a = input("First word: ").lower()
b = input("Second word: ").lower()
print("Anagrams" if sorted(a) == sorted(b) else "Not anagrams")

# 227 - Remove duplicate characters
text = input("Text: ")
result = ""
for ch in text:
    if ch not in result:
        result += ch
print(result)

# 228 - Mask all but last four characters
text = input("Text: ")
print("*" * max(0, len(text) - 4) + text[-4:])

# 229 - Check if text starts with a prefix
text = input("Text: ")
prefix = input("Prefix: ")
print(text.startswith(prefix))

# 230 - Check if text ends with a suffix
text = input("Text: ")
suffix = input("Suffix: ")
print(text.endswith(suffix))

# 231 - Convert sentence to word list
text = input("Sentence: ")
print(text.split())

# 232 - Join input words with comma
words = input("Enter words separated by spaces: ").split()
print(", ".join(words))

# 233 - Print every second character
text = input("Text: ")
print(text[::2])

# 234 - Check whether text is palindrome ignoring case
text = input("Text: ").lower().replace(" ", "")
print("Palindrome" if text == text[::-1] else "Not palindrome")

# 235 - Find the longest word
words = input("Sentence: ").split()
if words:
    print(max(words, key=len))

# 236 - Find the shortest word
words = input("Sentence: ").split()
if words:
    print(min(words, key=len))

# 237 - Swap first and last characters
text = input("Text: ")
if len(text) > 1:
    print(text[-1] + text[1:-1] + text[0])
else:
    print(text)

# 238 - Remove leading and trailing punctuation
text = input("Text: ")
print(text.strip(".,!?;:"))

# 239 - Format a number as a two-digit string
n = int(input("Number: "))
print(f"{n:02d}")

# ==================================================================
# TOPIC: LISTS AND LIST COMPREHENSIONS
# ==================================================================

# 240 - Create a list from user numbers
nums = list(map(int, input("Numbers: ").split()))
print(nums)

# 241 - Find average of list values
nums = [10, 20, 30, 40]
print(sum(nums) / len(nums))

# 242 - Find third largest distinct value
nums = [10, 30, 20, 30, 40]
unique = sorted(set(nums), reverse=True)
if len(unique) >= 3:
    print(unique[2])

# 243 - Separate even and odd list items
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print(evens, odds)

# 244 - Multiply each list value by 10
nums = [1, 2, 3, 4]
print([n * 10 for n in nums])

# 245 - Filter negative numbers
nums = [-4, 3, 0, 8, -1]
print([n for n in nums if n < 0])

# 246 - Find common values in two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print([n for n in a if n in b])

# 247 - Find values only in first list
a = [1, 2, 3, 4]
b = [3, 4, 5]
print([n for n in a if n not in b])

# 248 - Flatten a two-dimensional list
matrix = [[1, 2], [3, 4], [5, 6]]
print([n for row in matrix for n in row])

# 249 - Rotate list left by one
nums = [1, 2, 3, 4, 5]
print(nums[1:] + nums[:1])

# 250 - Rotate list right by one
nums = [1, 2, 3, 4, 5]
print(nums[-1:] + nums[:-1])

# 251 - Remove all occurrences of a value
nums = [2, 1, 2, 3, 2]
print([n for n in nums if n != 2])

# 252 - Replace negative values with zero
nums = [-2, 5, -1, 8]
print([max(n, 0) for n in nums])

# 253 - Count list items greater than 10
nums = [4, 12, 20, 8, 15]
print(sum(n > 10 for n in nums))

# 254 - Create list of multiples of 7
print([n for n in range(1, 101) if n % 7 == 0])

# 255 - Create a list of word lengths
words = ["cat", "python", "book"]
print([len(w) for w in words])

# 256 - Pair names with marks using zip
names = ["Ali", "Sara", "Noor"]
marks = [80, 92, 75]
print(list(zip(names, marks)))

# 257 - Split list into chunks of two
nums = [1, 2, 3, 4, 5, 6]
print([nums[i:i + 2] for i in range(0, len(nums), 2)])

# 258 - Check if list is sorted
nums = [1, 2, 3, 5]
print(nums == sorted(nums))

# 259 - Find index of largest list value
nums = [4, 9, 2, 9, 1]
print(nums.index(max(nums)))

# 260 - Create list of alternating signs
print([n if n % 2 else -n for n in range(1, 8)])

# 261 - Make a list of unique word values
words = ["tea", "coffee", "tea", "juice"]
print(list(dict.fromkeys(words)))

# 262 - Find list median for odd length
nums = [9, 1, 5, 3, 7]
nums.sort()
print(nums[len(nums) // 2])

# 263 - Create a list of numbers divisible by 5
print([n for n in range(1, 51) if n % 5 == 0])

# 264 - Find sum of list values at even indexes
nums = [10, 20, 30, 40, 50]
print(sum(nums[::2]))

# 265 - Create a list of index-value pairs
nums = ["a", "b", "c"]
print([(i, value) for i, value in enumerate(nums)])
