LIST,TUPLES, Dictionary and Multidimensional data structure

# Given List
L = ['/etc/password', 1223, '4KB', 'root', 'directory', '2021-02-20']
# a. Display filename and file size
# Filename is at index 0
# File size is at index 2
print("File Name:", L[0])
print("File Size:", L[2])

# Output:
# File Name: /etc/password
# File Size: 4KB


# b. Display file type and date/time
# File type is second last element
# Date is last element
print("File Type:", L[-2])
print("Date:", L[-1])

# Output:
# File Type: directory
# Date: 2021-02-20


# c. Display last 3 elements
# Using slicing
print("Last 3 elements:", L[-3:])

# Output:
# ['root', 'directory', '2021-02-20']


# d. Display first 2 elements
# Using slicing
print("First 2 elements:", L[:2])

# Output:
# ['/etc/password', 1223]


# e. Type L[7] and read the error message
# Index 7 does not exist, so it causes an error
# Uncomment to see the error
# print(L[7])

# Output:
# IndexError: list index out of range


# Input list
Size = [100, 200, 300, 400, 500]
for var in Size:
    r = str(var) + "GB"
    print(r)

# Output:
# 100GB
# 200GB
# 300GB
# 400GB
# 500GB

# Load Balance List
LB = [0.12, 0.34, 1.34, 4.5, 0.02]
t = 0
for var in LB:
    t = t + var
else:
    print("Sum of LoadBalance result:", t)

# Output:
# Sum of LoadBalance result: 6.32


# Create an empty list
hosts = []
# Display initial size
print("Initial Size:", len(hosts))

# Read 5 hostnames using while loop
c = 0
while c < 5:
    var = input("Enter a hostname: ")
    hosts.append(var)
    c = c + 1
# Display final size
print("Final Size:", len(hosts))
# Display each hostname using for loop
for h in hosts:
    print(h)

# Sample Output:
# Initial Size: 0
# Enter a hostname: server1
# Enter a hostname: server2
# Enter a hostname: server3
# Enter a hostname: server4
# Enter a hostname: server5
# Final Size: 5
# server1
# server2
# server3
# server4
# server5


# ============================================================
# TUPLE ACTIVITY
# ============================================================

# Given Tuple
fnames = ('p1.log', 'p2.log', 'p3.c', 'p4.py', 'p6.c', 'index.html')
count = 0
# Iterate and display with sequence number
for var in fnames:
    count = count + 1
    print(str(count) + "." + var)
else:
    print("Total number of tuple elements:", count)

# Output:
# 1.p1.log
# 2.p2.log
# 3.p3.c
# 4.p4.py
# 5.p6.c
# 6.index.html
# Total number of tuple elements: 6


"""
Dictionary and Multidimensional Data Structures
"""

Q1. Nested Dictionary Structure
Question:
Given the structure below:
a) Determine the structure type
b) Print the value of 'name'

Program:

action_model = {
    'request': {
        'operation': 'DeleteTags',
        'params': [{
            'target': 'Resources[0]',
            'source': 'identifier',
            'name': 'Id'
        }]
    }
}
print("Structure Type: Dictionary containing Dictionary and List")
print("Name value:", action_model['request']['params'][0]['name'])

Output:
Structure Type: Dictionary containing Dictionary and List
Name value: Id


Q2. Cloudwatch Structure
Question:
a) Print structure type  
b) Display Namespace and Threshold  
c) Add new Dimensions value  
d) Modify Unit to 'Minutes'  

Program:

Cloudwatch = {
    'AlarmName': "Web_Server_CPU_Utilization",
    'ComparisonOperator': 'GreaterThanThreshold',
    'EvaluationPeriods': 1,
    'MetricName': 'CPUUtilization',
    'Namespace': 'AWS/EC2',
    'Period': 60,
    'Statistic': 'Average',
    'Threshold': 70.0,
    'ActionsEnabled': False,
    'AlarmDescription': 'Alarm when server CPU exceeds 70%',
    'Dimensions': [
        {'Name': 'InstanceId', 'Value': 'INSTANCE_ID'}
    ],
    'Unit': 'Seconds'
}
print("Structure Type: Dictionary with List of Dictionary")
print("Namespace:", Cloudwatch['Namespace'])
print("Threshold:", Cloudwatch['Threshold'])
Cloudwatch['Dimensions'].append({'Name1': 'InstanceID1', 'Value1': 'InstanceID2'})
Cloudwatch['Unit'] = "Minutes"
print("Updated Cloudwatch Structure:", Cloudwatch)

Output:
Namespace: AWS/EC2
Threshold: 70.0
Unit updated to Minutes


Q3. Access List from Dictionary

Question:
Display list of instances from 'Action' key

Program:

S = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "cloudwatch:Describe*",
            "ec2:Describe*",
            "ec2:RebootInstances",
            "ec2:StopInstances*",
            "ec2:TerminateInstances"
        ],
        "Resource": ["*"]
    }]
}
print(S["Statement"][0]["Action"])

Output:
['cloudwatch:Describe*', 'ec2:Describe*', 'ec2:RebootInstances', 'ec2:StopInstances*', 'ec2:TerminateInstances']


Q4. Named Tuple Structure

Question:
Display the tuple data members

Program:

namedtuple = (
    'ServiceContext',
    ['service_name', 'service_model',
     'service_waiter_model', 'resource_json_definitions']
)
print(namedtuple[0])
print(namedtuple[1])
print(namedtuple[1][0])
print(namedtuple[1][1])
print(namedtuple[1][2])
print(namedtuple[1][3])

Output:
ServiceContext
['service_name', 'service_model', 'service_waiter_model', 'resource_json_definitions']
service_name
service_model
service_waiter_model
resource_json_definitions


Q5. Identifiers Structure

Question:
a) Display identifiers value  
b) Add new identifier entry  

Program:

d = {'resource': {
        'type': 'ResourceName',
        'identifiers': [
            {'target': 'Name1', 'source': 'input'}
        ]
    }
}
print(d['resource']['identifiers'])
d['resource']['identifiers'].append(
    {'target': 'Name2', 'source': 'input'}
)
print(d['resource']['identifiers'])

Output:
[{'target': 'Name1', 'source': 'input'}]
[{'target': 'Name1', 'source': 'input]()
