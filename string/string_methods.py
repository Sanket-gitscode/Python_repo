# ==========================================
# PYTHON STRING OPERATIONS REFERENCE SHEET
# ==========================================

# 1. Initialization & Basics
s = "LeetCode"
length = len(s)              # 8
first = s[0]                 # 'L'
last = s[-1]                 # 'e' (Negative indexing)

# 2. Advanced Slicing (s[start:stop:step])
substring = s[0:4]           # 'Leet' (Exclusive of stop index)
reversed_s = s[::-1]         # 'edoCteeL' (O(N) Reversal)
every_second = s[::2]        # 'LeCo'

# 3. Checking Content (Returns Boolean)
has_leet = "Leet" in s       # True
is_alpha = s.isalpha()       # True (Letters only)
is_digit = "123".isdigit()   # True (Numbers only)
is_alnum = "a1".isalnum()    # True (Letters & Numbers)

# 4. Searching & Counting
text = "banana"
idx = text.find("an")        # 2 (Returns -1 if not found)
count_a = text.count("a")    # 3
starts = text.startswith("b")# True
ends = text.endswith("na")   # True

# 5. Transformations (Returns a *new* string)
dirty_str = "   hello world   "
clean = dirty_str.strip()    # "hello world"
upper = clean.upper()        # "HELLO WORLD"
lower = clean.lower()        # "hello world"
replaced = clean.replace("world", "python") # "hello python"

# 6. Splitting and Joining (Crucial for Array/String DSA)
csv = "apple,banana,cherry"
fruits_list = csv.split(",") # ['apple', 'banana', 'cherry']

# Splitting by whitespace handles arbitrary spaces automatically
sentence = "Data    Structures    Algorithms"
words = sentence.split()     # ['Data', 'Structures', 'Algorithms']

# Joining elements back together efficiently
rejoined = " -> ".join(words)# "Data -> Structures -> Algorithms"

# 7. ASCII / Character Conversions (Frequent in Hash Map/Frequency array problems)
ascii_code = ord('a')        # 97
character = chr(97)          # 'a'

# Map character 'a'-'z' to index 0-25 for frequency arrays:
char_idx = ord('c') - ord('a') # 2

# 8. High-Performance Interview Pattern
# Anti-pattern: s += char in a loop (Causes O(N^2) time due to immutability)
# Best Practice: Append to list, then join (O(N) time)
result_list = []
for char in ["a", "b", "c"]:
    result_list.append(char)
final_string = "".join(result_list) # "abc"