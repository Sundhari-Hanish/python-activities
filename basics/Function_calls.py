# Python program to demonstrate a simple function call using time.sleep()
import time
def f1():
    print("This is f1 block")
    time.sleep(3)
    print("Exit from f1 block")

print("This is main section-1")
f1()
time.sleep(2)
print("This is main section-2")
print("Exit from main section")
#Output:This is main section-1
#       This is f1 block
#       Exit from f1 block
#       This is main section-2
#       Exit from main section


#NESTED FUNCTION CALLS
# program to demonstrate simple function calls.
def fs():
    print("File system details")
    print("File system Information")
    print("Exit from fs block")
def ps():
    print("Process block")
    print("Process ctrl block struct")
    print("Exit from ps block")
print("---Main section---")
fs()
print("----back to main section---")
ps()
print("---exit from main section---")
# Output: ---Main section---
#         File system details
#         File system Information
#         Exit from fs block
#         ----back to main section---
#         Process block
#         Process ctrl block struct
#         Exit from ps block
#         ---exit from main section---


#program to demonstrate nested function calls.
def fs():
    print("File system details")
    print("File system Information")
    ps()
    print("Exit from fs block")

def ps():
    print("Process block")
    print("Process ctrl block struct")
    print("Exit from ps block")

print("---Main section---")
fs()
print("---exit from main section---")
# Output:---Main section---
#        File system details
#        File system Information
#        Process block
#        Process ctrl block struct
#        Exit from ps block
#        Exit from fs block
#        ---exit from main section---


# Program using functions upload() and download() to read file details and display them.
def upload():
    fname = input("Enter a filename: ")
    findex = input("Enter a file index number: ")
    fowner = input("Enter a file owner/user name: ")
    fperm = input("Enter {} file permission: ".format(fname))
    download(fname, findex, fowner, fperm)
    print("Exit from upload block")
def download(a1, a2, a3, a4):
    print("""
File name        : {}
------------------------
File index       : {}
------------------------
File owner       : {}
------------------------
File permission  : {}
------------------------
""".format(a1, a2, a3, a4))
upload()
# Output:
# Enter a filename: data.txt
# Enter a file index number: 101
# Enter a file owner/user name: admin
# Enter data.txt file permission: rw-r--r--

# File name        : data.txt
# ------------------------
# File index       : 101
# ------------------------
# File owner       : admin
# ------------------------
# File permission  : rw-r--r--
# ------------------------
# Exit from upload block


# Python program to demonstrate function call with required arguments.
def f1(a1, a2):
    print(a1, type(a1))
    print(a2, type(a2))
f1(10, 20)
f1(100, 3.433)
f1('', [])
#Output:
# 10 <class 'int'>
# 20 <class 'int'>
# 100 <class 'int'>
# 3.433 <class 'float'>
#  <class 'str'>
# [] <class 'list'>


# Program to demonstrate default arguments in a function.
def f2(a1=100, a2=200):
    print(a1, a2)

f2()
f2("userA")
f2("userA", "/bin/bash")
# Output:
# 100 200
# userA 200
# userA /bin/bash


# Python program to demonstrate the use of global variables in function calls.
def f1():
    global v1, v2, v3
    v1 = "ABC"
    v2 = "200"
    v3 = "300"
    v4 = "400"
    v5 = "500"
    print(v1, v2, v3, v4, v5)
f1()
print("Main section: {}".format(v1))
def f2():
    print("From f2 function: {}".format(v1))
f2()
# Output:
# ABC 200 300 400 500
# Main section: ABC
# From f2 function: ABC




