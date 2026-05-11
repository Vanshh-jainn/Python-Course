# if condition1:
    # Code to execute if condition1 is True
# elif condition2:
    # Code to execute if condition2 is True
# else:
    # Code to execute if all conditions are False

age = int(input("Enter your age: "))

if (age<18 and age>=0):
    print("You are a minor.")
elif (age == 18):
    print("You just became an adult!")
elif(age<0):
    print("Enter valid age")
else:
    print("You are an adult.")