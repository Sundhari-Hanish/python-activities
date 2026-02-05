"""
Exception Handling
"""

Q1. Using Exception Handling how to handle the below exceptions

A.

DICT = {
    "host01": "host01.example.com",
    "host02": "host02.example.com",
    "host03": "host03.example.com"
}

try:
    for v in DICT.keys():
        print(v, Dict[v])
except NameError as e:
    print("Error:", e)

Output:
Error: name 'Dict' is not defined


B.

try:
    with open("ab.txt") as fobj:
        print(fobj.read())
except FileNotFoundError as e:
    print("Error:", e)

Output:
Error: [Errno 2] No such file or directory: 'ab.txt'



Q2.

def first(x):
    print('Starting first.')
    try:
        second(x)
    except:
        print("Caught at first")
    print("Ending first")
def second(x):
    print('Starting second.')
    try:
        third(x)
    except:
        print("Caught at second")
    print("Ending second")
def third(x):
    print('Starting third.')
    print("Ending third.")
first(2)

Output:
Starting first.
Starting second.
Starting third.
Ending third.
Ending second
Ending first



Q3. Write a program check_args.py that gets two command line arguments and checks that the first
represents a valid int number and that the second represents a valid float number.

Program:

import sys
try:
    a = int(sys.argv[1])
except ValueError:
    print("'" + sys.argv[1] + "' is not a valid first argument, expected an int value")
    sys.exit(1)

try:
    b = float(sys.argv[2])
except ValueError:
    print("'" + sys.argv[2] + "' is not a valid second argument, expected a float value")
    sys.exit(1)

print("Arguments are valid")

Sample Output:
$ python check_args.py 3 help!
'help!' is not a valid second argument, expected a float value

$ python check_args.py I_need_somebody 3.756453
'I_need_somebody' is not a valid first argument, expected an int value


Q4. Write a program that tries to read a file corresponding to the first command-line argument.
Provide useful feedback if the file doesn't exist or anything goes wrong reading the file.

Program:

import sys
try:
    with open(sys.argv[1]) as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist")
except Exception as e:
    print("Error while reading file:", e)

Sample Output:
File does not exist



Q5.If mysqld daemon is not running and database connection is attempted,
trace the error string using Exception handling.

Program:

try:
    import MySQLdb
    db = MySQLdb.connect("localhost", "USERNAME", "PASSWORD", "DBNAME")
    print("Database connection successful")
except Exception as e:
    print("Database connection error:", e)

Output:
Database connection error: (error message from MySQL server)
