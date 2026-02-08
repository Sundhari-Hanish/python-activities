#Python program to record and save customer complaints with time into a file.

import time
customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")
while True:
    print("Enter your Complaint Type:")
    print("1. Product Complaint")
    print("2. Service Complaint")
    c = input("Enter your complaint type (1 or 2): ")
    if c == "1":
        complaint = input("Enter your product complaint: ")
        c_type = "Product Complaint"
        break
    elif c == "2":
        complaint = input("Enter your service complaint: ")
        c_type = "Service Complaint"
        break
    else:
        print("Invalid Complaint type")
        continue
c_time = time.ctime()
customer_details = {
    "Customer Name": customer_name,
    "Customer ID": customer_id,
    "Complaint Type": c_type,
    "Complaint": complaint,
    "Time": c_time
}
with open("customer.log", "a") as file:
    file.write(str(customer_details) + "\n")
print("Complaint has been recorded successfully")
