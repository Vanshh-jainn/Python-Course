# we use "#" to use comments in python.

'''This is 
the multiple
line comment'''

"""
This is 
the multiple
line comment
"""
# both single quote and double quote works for multi line comment.


# Escape sequences are used to include special characters in strings.
# Common escape sequences:
# \n: Newline
# \t: Tab
# \\: Backslash
# \": Double quote
# \': Single quote

print("Hello\nWorld")
print("This is a Tab \tcharacter")


#print statment
print("harry jain","vansh jain") #here see after using "," in between the output as a space as by default.
print("harry jain","vansh jain", sep=",") #but we can have anything by setting the value of seperator by using "sep" funtoion.

print( )
print("dont want a new line in both prints")
print("still there is a new line")
print()
#the cure is
#use end funtion to end the line with anything and its by defailt is "\n".
print("dont want a new line in both prints",end=" ")
print("by using end funtion there is no new line")



"""--------Note--------"""
#to print multiple line in single print statement we can also use triple quotes instead of \n.
print('''this is a multiple
      line print statement that 
also put the spaces as it is''')
print("""this is a multiple
      line print statement""")
