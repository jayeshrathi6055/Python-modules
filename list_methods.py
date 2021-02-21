lst = ["name","age","profile"]

# Append in a list
lst.append("email")
print(lst)

# Copy of a list
x = lst.copy()
print(x)

# Extend 1 list to another
lst.extend(x)
print(lst)

# Count a specified value in a list
print(lst.count("age"))

# Index of specified value
print(lst.index("profile"))

# Pop in a list
print(lst.pop())
print(lst)

print(lst.pop(2))
print(lst)

# Insert in a list
lst.insert(2,"profile")
lst.insert(-1,"email")
print(lst)

# Remove any item from a list
lst.remove("email")
print(lst)

# Reverse a list
lst.reverse()
print(lst)

# Sort a list
lst.sort()
print(lst)

# Clear the List
lst.clear()
print(lst)