# Activity 2: Comments, Data Types, Variables, and Strings

# -------------------------------
# Python Comments
# -------------------------------
# This is a single-line comment in Python
# Python does not support multi-line comments like /* */
# Multi-line comments are written using multiple # symbols

# -------------------------------
# Python Fundamental Data Types
# -------------------------------
a = 5
b = 4.5
c = 3 + 4j

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))

# -------------------------------
# Variable demonstration
# -------------------------------
count = 5
print("Count value:", count)

count = "Hello"
print("Count value after reassignment:", count)

# -------------------------------
# String as a collection of characters
# -------------------------------
s = "welcome"
print("Character at index 3:", s[3])
print("Character at index -4:", s[-4])

# -------------------------------
# String length and slicing
# -------------------------------
s2 = "sample python programming"
print("Length of string:", len(s2))
print("Slice from index 5 to 15:", s2[5:15])
print("Last 3 characters:", s2[-3:])

# -------------------------------
# String indexing and slicing activity
# -------------------------------
s1 = "root:x:bin:bash"

# Display 3rd index character
print("3rd index character:", s1[3])

# Display last index character
print("Last index character:", s1[-1])

# Display last 4 characters
print("Last 4 characters:", s1[-4:])

# Display first 4 characters
print("First 4 characters:", s1[:4])

