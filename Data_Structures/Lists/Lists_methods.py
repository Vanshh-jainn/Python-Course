my_list = [1, 2, 3]
print(my_list)

my_list.append(4) 
print(my_list) # [1, 2, 3, 4]
 
my_list.insert(1, 99) # in insert first type the index you want to insert on then the thing you wanna insert.
print(my_list) # [1, 99, 2, 3, 4]

my_list.remove(99) # here it removes the datatype that you type
print(my_list) # [1, 2, 3, 4]  

my_list.pop() 
print(my_list) # Removes last element -> [1, 99, 3] if left empty or remove the particular index if we type it

my_list.reverse()
print(my_list) # [3, 99, 1]
 
my_list.sort()
print(my_list) # [1, 3, 99]

marks = [45,2,57,44]
extra_marks = [34,56,21,23]
marks.extend(extra_marks)
print(marks)
