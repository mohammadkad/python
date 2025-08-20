# 1404-05-29
# Mohammad Kadkhodaei
# ---

# Basic Syntax
# zip(iterable1, iterable2, iterable3, ...)

'''
The zip() version is:
- More readable
- More efficient
- Less error-prone: No risk of index mismatches
'''
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

'''
Key Points about zip()
- Stops at shortest iterable: If the input lists have different lengths, zip() stops when the shortest list is exhausted.
- Returns iterator: zip() returns an iterator, which is memory-efficient.
- Convert to list: You can convert the result to a list if needed:
'''
paired_list = list(zip(names, ages))
