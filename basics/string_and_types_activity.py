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

# =====================================================
# Activities from Course PDF (Exact Logic)
# =====================================================

# -------------------------------
# p2.py : Sum of numbers in list
# -------------------------------
numbers = [16, 50, 300, 5, 40, 110]
total = 0

for v in numbers:
    total = total + v

print("Sum of numbers:{}".format(total))


# -------------------------------
# p3.py : Membership operator
# -------------------------------
hosts = ['host01', 'host02', 'host03', 'host04', 'host05']

if ("host03" in hosts):
    print("host03 is exists")
else:
    print("Sorry host03 is not exists")


# -------------------------------
# p5.py : List operations
# -------------------------------
osnames = ["unix", "linux", "aix", "winx", "SunOS"]

print(osnames[0])
print(osnames[1])

osnames[1] = "ORACLELINUX"
print(osnames[1])

print(osnames)


# -------------------------------
# p6.py : Tuple operations
# -------------------------------
servers = (
    "host01.example.com",
    "host02.example.com",
    "host03.example.com",
    "host04.example.com",
    "host05.example.com"
)

print(servers[0])
print(servers[1])
print(servers)


# -------------------------------
# p9.py : String split
# -------------------------------
s1 = "root:bin:x:bash,userA:usr:bin:ksh,userB:usr:bin:sh"
print(s1.split(","))


# -------------------------------
# p10.py : List slicing & tuple
# -------------------------------
L1 = ["Line1\n","Line2\n","Line3\n","Line4\n","Line5\n","Line6\n","Line7\n","Line8\n"]

print(L1[:5])

L1.insert(2, "LineXYZ\n")

print(L1[-5:])

T = tuple(L1)
print("T belongs to:{}".format(type(T)))
print("L1 belongs to:{}".format(type(L1)))


# -------------------------------
# Output-based questions
# -------------------------------

# list = ['a','b','c','d','e']
# list[10:] -> [](empty array will be returned)

# for var in ["mon","tue","wed","thu","fri"]:
#     if(var == "wed"):
#         continue
#     else:
#         print(var)

# Output:
# mon
# tue
# thu
# fri

# ("Test2.log" not in Logfiles) -> NOT-FOUND

# weekdays.count('mon') -> 3


