A = int(input("Enter Number A: "))
B = int(input("Enter Number B: "))
C = input("Enter your operator: ")

match (C):
    case "+":
        print(A,"+",B,"=", " ", A+B, sep="")
    case "-":
        print(A,"-",B,"=", " ", A-B, sep="")
    case "/":
        print(A,"/",B,"=", " ", A/B, sep="")
    case "*":
        print(A,"*",B,"=", " ", A*B, sep="")
