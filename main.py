from collections import deque
import heapq

# variables/assignments
n, m = 0, "abc"

# increment
n += 1

# null
hi = None

# conditionals
if n > 2:
  n += 1
elif n > 9:
  n -= 1

if ((n > 2 and n > 9) or n > 100):
  n += 88


# looping
# range is not inclusive
for i in range(5):
  print(i) # 01234

# starting value
for i in range(2,6):
  print(i) # 2345

# reversing
for i in range(5,1,-1):
  print(i) # 5432

# lists
list = [12,23]
list.append(1)

list.pop()

list.insert(1,7)

list[0] = 4
print(list[-1]) # last value

# init arr of size n
n = 2

arr = [1] * n # [1,1]

# slicing
arr = [1,2,3,4]
print(arr[1:3]) # [2,3]
print(arr[0:4]) # [1,2,3,4]

# loop through array
for i in range(len(arr)):
  print(arr[i])

# without index
for n in arr:
  print(n)

# enumerate index and value
for i,n in enumerate(arr):
  print(i,n)

# reversing
arr.reverse()

# Sorting
arr.sort()

arr.sort(reverse=True)

# custom sorting string
str_arr = ['hi', 'bye']

str_arr.sort(key=lambda x: len(x))

# list comprehension
arr = [i for i in range(5)] # [0,1,2,3,4]

# deques
queue = deque()
queue.append(1)
queue.append(2)
# [1,2]

queue.popleft
# [2]

queue.appendleft(1)
# [1, 2]

queue.pop()
# [1]

# hash sets
mySet = set()
mySet.add(1)
# check if it exists
print(1 in mySet)

mySet.remove(1)

# list to set
print(set([1,2,3]))

# hashmaps
myMap = {}
myMap["alice"] = 3

print("alice" in myMap)

myMap.pop("alice")

# dict comprehension
myMap = {i: 2*i for i in range(2)}

# looping map
for key in myMap:
  print(key, myMap[key])

for val in myMap.values():
  print(val)

for key, val in myMap.items():
  print(key, val)

# tuples
tup = (1,2)

# can be used as a key for hashmap/set
myMap = {(1,2): 3}

# heaps
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 5)

print(minHeap[0]) # smallest val at 0 index

while len(minHeap):
  print(heapq.heappop(minHeap))

# max heap workaround
# push negative values
# multiply by -1 when popping
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -1)

# max val
print(-1 * maxHeap[0])

while len (maxHeap):
  print(-1 * heapq.heappop(maxHeap))

# build heap from array
arr = [1,2,3]

heapq.heapify(arr)

while arr:
  print(heapq.heappop(arr))


# Find intersection values in a set
set1 = set([1])
set2 = set([1])
common = set1.intersection(set2)