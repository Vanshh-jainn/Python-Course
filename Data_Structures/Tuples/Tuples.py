# Tuples are ordered but immutable collections (cannot change after creation).

a = (2, 4, 2, 4, 6)
print(a)
print(a[1]) # 1 here is index number which will print 4.

# imp case to create tuple with single element we type
single = (3,)
print(single)


'''Why Use Tuples?
Faster than lists (since they are immutable)
Used as dictionary keys (since they are hashable)
Safe from unintended modifications'''