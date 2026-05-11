# match value:
#     case pattern1:
#         # Code to execute if value matches pattern1
#     case pattern2:
#         # Code to execute if value matches pattern2
#     case _:
#         # Default case (if no patterns match)


a = int(input("Enter number between 1 - 10: "))
if(a<=10 and a>=1):
    match a:
        case 1:
            print("You clicked the lucky number 1!")
        case 3:
            print("You clicked the lucky number 3!")
        case _:
            print("Lmao you missed the lucky number")
else:
    print("Enter a valid number")