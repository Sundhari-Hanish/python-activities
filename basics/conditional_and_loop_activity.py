# 1. Read a business enquiry number and test if it is above 5000
enquiry_no = int(input("Enter business enquiry number: "))

if enquiry_no > 5000:
    print("Enquiry number is above 5000")
else:
    print("Enquiry number is 5000 or below")

# Output:
# Enter business enquiry number: 6500
# Enquiry number is above 5000



# 2. Read database name and assign port number
db_name = input("Enter database name: ")

if db_name.lower() == "oracle":
    port = 1234
else:
    port = 5545

print("Assigned port number:", port)

# Output:
# Enter database name: oracle
# Assigned port number: 1234



# 3. Check if special character exists in given string
s = "450-item:50$,city~city2"
ch = input("Enter a special character to check if it exists in nthe string: ")
if ch in s:
    print("Special character exists in the string")
else:
    print("Special character does not exist in the string")

# Output:
# Enter a special character to check: $
# Special character exists in the string

#---------------------------------------
# Nested Conditional Statement Activity
#---------------------------------------
enquiry_no = int(input("Enter business enquiry number: "))
if enquiry_no >= 501 and enquiry_no <= 599:
    quotation_no = int(input("Enter quotation number: "))
    if quotation_no >= 200 and quotation_no <= 300:
        customer = input("Enter customer name: ")
        if customer == "Klabs" or customer == "Oracle":
            print("Valid Details")
            print("Enquiry Number:", enquiry_no)
            print("Quotation Number:", quotation_no)
        else:
            print("Customer name not matched")
    else:
        print("Invalid quotation number")
else:
    print("Invalid enquiry number")

# Output:
# Enter business enquiry number: 550
# Enter quotation number: 250
# Enter customer name: Oracle
# Valid Details
# Enquiry Number: 550
# Quotation Number: 250


#------------------------------------------------
# Looping Statement Activity (PIN verification)
#------------------------------------------------
pin = 01234
count = 0
max_attempts = 3
while count < max_attempts:
    p = int(input("Enter PIN: "))
    count = count + 1
    if p == pin:
        print("Success! PIN matched at attempt {}.".format(count))
        break
else:
    print("Sorry, PIN is blocked after {} attempts.".format(max_attempts))

# Output:
# Enter PIN: 1111
# Enter PIN: 2222
# Enter PIN: 1234
# Success! PIN matched at attempt 3.


