a = "hello"
b = "25"
c = "     sir"

# Change in Case letters-------------------->
print(a.upper())

print(a.capitalize())
print(a.title())

print(a.casefold())
print(a.lower())

# Count of Same------------------------------>
print(a.count("l"))

# Check Starting and Ending------------------->
print(a.startswith("l"))

print(a.endswith("o"))

# Find a Word in a String-------------------->
print(a.find("o"))

# Check Statements---------------------------->
print(b.isdigit())
print(b.isnumeric())
print(a.isdecimal())
print(a.isspace())

# Remove Whitspaces----------------------------->
print(c.strip())

# Split a String--------------------------------->
print(c.split())

# Want to convert small letter to Capital Letter and vice-versa-------------->
print(a.swapcase())

# Reverse a String------------------------------->
e = "jayesh"
e = e[::-1]
print(e)