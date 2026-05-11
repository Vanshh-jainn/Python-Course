# In Python, strings are sequences of characters, and each character has an index. You can access individual characters using indexing and extract substrings using slicing.

# String Indexing
# Each character in a string has a unique index, starting from 0 for the first character and -1 for the last character.

Name = "Vansh"
print(Name[0:4]) # goes from 0 to (2-1) ie 0-1.
print(Name[0:-1]) # Same as[0:4]

# slicing with steps
name = "123456789"
# print(name[0:10:n]) # n here means skip n-1 characters
print(name[0:10:2])
print(name[0:10:3])
print(name[:4])
print(name[1:])

