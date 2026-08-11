# ============================================================
# PYTHON DSA - COLLECTIONS MODULE CHEAT SHEET
# ============================================================
#
# Main things to remember:
#
# deque       -> Queue / BFS / Sliding Window
# Counter     -> Frequency counting
# defaultdict -> Graphs / Grouping
#
# Also useful:
# namedtuple
# OrderedDict
# ChainMap
#
# And outside collections:
# heapq       -> Heap / Priority Queue
#
# ============================================================


# ============================================================
# 1. DEQUE
# ============================================================
#
# deque = Double Ended Queue
#
# Very useful for:
#   - BFS
#   - Queue
#   - Sliding Window
#   - Adding/removing from both ends
#
# IMPORTANT:
# list.pop(0)  -> O(n)
# deque.popleft() -> O(1)
#
# ============================================================

from collections import deque


# -------------------------
# Basic deque
# -------------------------

q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q)
# deque([10, 20, 30])


# Remove from the LEFT

x = q.popleft()

print(x)
# 10

print(q)
# deque([20, 30])


# Remove from the RIGHT

x = q.pop()

print(x)
# 30


# Add to the LEFT

q.appendleft(5)

print(q)
# deque([5, 20])


# -------------------------
# Create deque directly
# -------------------------

q = deque([1, 2, 3, 4])

print(q)


# -------------------------
# BFS example
# -------------------------

# Imagine this tree:
#
#             1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7
#
# BFS visits:
#
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7


class Node:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


def bfs(root):

    if root is None:
        return

    q = deque([root])

    while q:

        # Remove first node
        node = q.popleft()

        print(node.val)

        # Add children
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


bfs(root)

# Output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7


# ============================================================
# 2. COUNTER
# ============================================================
#
# Counter is used for FREQUENCY COUNTING.
#
# Very useful for:
#   - Arrays
#   - Strings
#   - Anagrams
#   - Duplicates
#   - Top K frequent elements
#
# ============================================================

from collections import Counter


# -------------------------
# Count numbers
# -------------------------

arr = [1, 2, 2, 3, 3, 3, 4]

freq = Counter(arr)

print(freq)

# Counter({
#     3: 3,
#     2: 2,
#     1: 1,
#     4: 1
# })


# Ask how many times something appears

print(freq[3])
# 3

print(freq[2])
# 2


# -------------------------
# Count characters
# -------------------------

s = "banana"

freq = Counter(s)

print(freq)

# Counter({
#     'a': 3,
#     'n': 2,
#     'b': 1
# })


print(freq["a"])
# 3


# -------------------------
# most_common()
# -------------------------

s = "mississippi"

freq = Counter(s)

print(freq.most_common())

# Example:
# [('i', 4), ('s', 4), ('p', 2), ('m', 1)]


print(freq.most_common(2))

# Top 2:
# [('i', 4), ('s', 4)]


# ============================================================
# COUNTER DSA EXAMPLE:
# CHECK IF TWO STRINGS ARE ANAGRAMS
# ============================================================

def is_anagram(s, t):

    return Counter(s) == Counter(t)


print(is_anagram("listen", "silent"))
# True

print(is_anagram("hello", "world"))
# False


# ============================================================
# COUNTER DSA EXAMPLE:
# FIND DUPLICATES
# ============================================================

arr = [1, 2, 3, 2, 4, 3, 5, 3]

freq = Counter(arr)

for num, count in freq.items():

    if count > 1:
        print(num, "appears", count, "times")


# ============================================================
# 3. DEFAULTDICT
# ============================================================
#
# defaultdict is basically a dictionary
# that automatically creates a default value.
#
# VERY useful for:
#   - Graphs
#   - Grouping
#   - Frequency maps
#   - Adjacency lists
#
# ============================================================

from collections import defaultdict


# -------------------------
# Normal dictionary problem
# -------------------------

# This would cause an error:
#
# d = {}
# d["a"].append(10)
#
# Because "a" doesn't exist yet.


# -------------------------
# defaultdict(list)
# -------------------------

d = defaultdict(list)

d["a"].append(10)
d["a"].append(20)

d["b"].append(30)

print(d)

# {
#     'a': [10, 20],
#     'b': [30]
# }


# ============================================================
# DEFAULTDICT FOR GRAPH
# ============================================================
#
# Suppose we have edges:
#
# 1 -- 2
# 1 -- 3
# 2 -- 4
# 3 -- 5
#
# Adjacency list:
#
# 1 -> [2, 3]
# 2 -> [1, 4]
# 3 -> [1, 5]
# 4 -> [2]
# 5 -> [3]
#
# ============================================================

graph = defaultdict(list)


edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 5)
]


for u, v in edges:

    graph[u].append(v)
    graph[v].append(u)


print(graph)


# ============================================================
# GRAPH + BFS
# ============================================================

def graph_bfs(graph, start):

    visited = set()

    q = deque([start])

    visited.add(start)

    while q:

        node = q.popleft()

        print(node)

        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)

                q.append(neighbour)


graph_bfs(graph, 1)

# Output:
#
# 1
# 2
# 3
# 4
# 5


# ============================================================
# DEFAULTDICT FOR GROUPING
# ============================================================

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "B"),
    ("Emma", "A")
]


groups = defaultdict(list)


for name, grade in students:

    groups[grade].append(name)


print(groups)

# {
#     'A': ['Alice', 'Charlie', 'Emma'],
#     'B': ['Bob', 'David']
# }


# ============================================================
# 4. DEFAULTDICT(int)
# ============================================================
#
# You can make the default value an integer.
#
# This is useful for counting.
#
# ============================================================

freq = defaultdict(int)

arr = [1, 2, 2, 3, 3, 3]

for num in arr:

    freq[num] += 1


print(freq)

# {
#     1: 1,
#     2: 2,
#     3: 3
# }


# ============================================================
# 5. NAMEDTUPLE
# ============================================================
#
# Less important for DSA.
#
# It allows you to create tuple-like objects
# with named fields.
#
# ============================================================

from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


p = Point(10, 20)

print(p.x)
# 10

print(p.y)
# 20


# ============================================================
# 6. ORDEREDDICT
# ============================================================
#
# Older Python code often uses OrderedDict.
#
# Modern Python dictionaries already preserve insertion order,
# so you usually DON'T need this for DSA.
#
# Just know that it exists.
#
# ============================================================

from collections import OrderedDict


d = OrderedDict()

d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d)


# ============================================================
# 7. CHAINMAP
# ============================================================
#
# Combines multiple dictionaries.
#
# NOT important for beginner DSA.
#
# ============================================================

from collections import ChainMap


d1 = {"a": 1}
d2 = {"b": 2}

combined = ChainMap(d1, d2)

print(combined["a"])
# 1

print(combined["b"])
# 2


# ============================================================
# 8. HEAPQ
# ============================================================
#
# IMPORTANT FOR DSA
#
# heapq is NOT part of collections,
# but learn it alongside collections.
#
# It gives you a MIN HEAP.
#
# Very useful for:
#   - Priority Queue
#   - Dijkstra
#   - Top K problems
#   - Scheduling
#   - Merge K sorted lists
#   - Greedy algorithms
#
# ============================================================

import heapq


# -------------------------
# Create empty heap
# -------------------------

heap = []


# Add elements

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)


print(heap)


# Remove smallest element

x = heapq.heappop(heap)

print(x)
# 1


x = heapq.heappop(heap)

print(x)
# 2


# ============================================================
# HEAP EXAMPLE
# FIND K SMALLEST ELEMENTS
# ============================================================

arr = [10, 3, 7, 1, 8, 2, 5]

heap = []

for num in arr:

    heapq.heappush(heap, num)


k = 3

for i in range(k):

    print(heapq.heappop(heap))


# Output:
#
# 1
# 2
# 3


# ============================================================
# 9. STACK
# ============================================================
#
# You DON'T need collections for a normal stack.
#
# Python list works perfectly.
#
# ============================================================

stack = []


# Push

stack.append(10)
stack.append(20)
stack.append(30)


# Pop

print(stack.pop())
# 30

print(stack.pop())
# 20


# Stack:
#
#     30  <- top
#     20
#     10
#
# LIFO
# Last In, First Out


# ============================================================
# 10. QUEUE
# ============================================================
#
# For a queue, use deque.
#
# FIFO:
# First In, First Out
#
# ============================================================

q = deque()


q.append(10)
q.append(20)
q.append(30)


print(q.popleft())
# 10

print(q.popleft())
# 20


# Queue:
#
# 10 -> 20 -> 30
# ^
# first out


# ============================================================
# QUICK DSA CHEAT SHEET
# ============================================================

"""
DATA STRUCTURE       PYTHON TOOL

Array                list

Hash Map             dict

Hash Set             set

Stack                list

Queue                deque

BFS                  deque

Frequency Map        Counter / dict

Graph                defaultdict(list)

Priority Queue       heapq

Min Heap             heapq

Tree BFS             deque

Top K                 heapq / Counter

Sliding Window       deque

Grouping             defaultdict(list)
"""


# ============================================================
# MOST IMPORTANT IMPORTS TO REMEMBER
# ============================================================

from collections import deque
from collections import Counter
from collections import defaultdict

import heapq


# You can also combine the collections imports:

from collections import deque, Counter, defaultdict


# ============================================================
# FINAL MEMORY TRICK
# ============================================================

"""
deque
-----
Think: QUEUE

Used for:
BFS
Queue
Sliding Window


Counter
-------
Think: COUNT

Used for:
Frequency
Anagrams
Duplicates
Top K


defaultdict
-----------
Think: DICTIONARY WITHOUT INITIALIZATION

Used for:
Graphs
Grouping
Adjacency Lists


heapq
-----
Think: SMALLEST / PRIORITY

Used for:
Priority Queue
Dijkstra
Top K
Greedy
"""


# ============================================================
# END
# ============================================================
