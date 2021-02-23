data = {"name":"your name" , "age":"your age"}

# Copy the data
a = data.copy()
print(a)

# Use of fromkeys()
key = ["name"]
value = "skillf"
b = data.fromkeys(key,value)
print(b)

# Want to get a value of a key
print(data.get("age"))

# Want all items present in dict
print(data.items())

# Want all keys
print(data.keys())

# Want all values
print(data.values())

# Want to do update in a dictionary
data.update({"profile":"photo"})
print(data)

# Want to delete last item
data.popitem()
print(data)

# Want to delete specific Key-value pair
data.pop("age")
print(data)

# Want to set key-value pair
data.setdefault("age",20)
print(data)

# Clear the data present in dictionary
data.clear()
print(data)