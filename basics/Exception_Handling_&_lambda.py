# Python program to demonstrate exception handling using try, except, else, and finally.
print('ONE')
print('TWO')
print('THREE')
try:
    print(VAR)
except NameError as eobj:
    print("Exception occurred: " + str(eobj))
else:
    print(VAR + 100)
finally:
    print("Thank You")
print("FOUR")
print("FIVE")
# Output:
# ONE
# TWO
# THREE
# Exception occurred: name 'VAR' is not defined
# Thank You
# FOUR
# FIVE


# Python program to raise a custom exception if a number is less than zero.
v = -5  
try:
    if v < 0:
        raise Exception("Given number is less than zero")
except Exception as eobj:
    print(eobj)
# Output: # Given number is less than zero


# Simple addition using lambda
fx = lambda a1, a2: a1 + a2
fx(10, 20)  
# Output: 30

# Convert string to uppercase using lambda
fx3 = lambda a: a.upper()
fx3("abc")  
# Output: 'ABC'

# Add 100 using lambda
f5 = lambda a: a + 100
f5(10) 
# Output: 110

# Function call with normal function
def f1(a1, a2):
    return a1 + a2
f1(10, 20)   # Output: 30
f1("A", "B") # Output: 'AB'

# Multiple arguments lambda examples (activity)
fx = lambda a1, a2, a3: a1 + a2 * a3
fx(10, 20, 30)
# Output: 610

fy = lambda a1, a2: a1 > a2
fy(1000, 200) 
# Output: True

fz = lambda a1, a2: a1.upper() + a2.lower()
fz("python", "LAMBDAEXPRESSION") 
# Output: 'PYTHONlambdaexpression'


