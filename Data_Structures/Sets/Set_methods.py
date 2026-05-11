s = {12, 45, 55, 34, 67}
print(s)


# Key set methods

my_set = {1, 2, 3, 4}

my_set.add(5)        # {1, 2, 3, 4, 5}
print(my_set)

my_set.remove(2)     # {1, 3, 4, 5}
print(my_set)

my_set.discard(10)   # No error if element not found
print(my_set)

my_set.pop()         # Removes random element
print(my_set)

# Set Operations:
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))   # {1, 2}