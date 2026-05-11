name = "vansh jain" # Strings are immutable
# name[0] = "R" # No i can not do that

print(len(name)) # "len" funtion is used to find the length of the string.

#------- Note -------> in string methods the original string wont be affected but the new copy of string will be formed.
#changing case
print(name.upper()) # Make everything upper
print(name.lower()) # Make everything lower
print(name.title()) # first letter of every word capital
print(name.capitalize()) # first letter of first word capital

# removing whitespace
Name = "   Hello world   "
print(Name.strip()) #removes all left and right spaces and empty lines too..
print(Name.rstrip())#rstrip means right strip which will only remove the right lines and right part
print(Name.lstrip())#lstrip means left strip which will only remove the left lines and left part.

#Finding and Replace
S = "Python is fun"
print(S.find("is")) # gives the starting index of that word.
print(S.replace("fun","awesome"))

#splitting and joining
fruits = "Apple,Bananas,Mango"
print(fruits.split(",")) #this will split the string using defined character and make a lis out of it
print(",".join(['Apple', 'Bananas', 'Mango'])) # this is the way to convert a list to a string.

#checking string properties
text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False
