for i in range(1,21):
    
    if(i==11):
        break
    print(i)   # cancels the execution of thiss loop when it will hit 11.

for i in range(1,21):
    if i==11:
        continue # The continue statement skips the rest of the code in the current iteration and moves to the next iteration.
    print(i)

#The pass statement is a placeholder that does nothing. It is used when syntax requires a statement but no action is needed.

for i in range(5):
    if i == 3:
        pass  # Do nothing
    print(i)  # Output: 0, 1, 2, 3, 4