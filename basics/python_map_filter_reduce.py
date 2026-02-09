# Convert all names to uppercase using map()
def fx(a):
    return a.upper()
names = ['kumar', 'tom', 'karthik', 'ediip']
result = list(map(fx, names))
print(result)
# Output:['KUMAR', 'TOM', 'KARTHIK', 'EDIIP']


# Add .mp3 extension to file names using map()
def fx(a1):
    return a1 + ".mp3"
files = ['a', 'b', 'c']
result = list(map(fx, files))
print(result)
#Output: ['a.mp3', 'b.mp3', 'c.mp3']


# Using map() with lambda
names = ['kumar', 'tom', 'karthik', 'ediip']
print(list(map(lambda var: var.upper(), names)))
files = ['a', 'b', 'c']
print(list(map(lambda a: a + ".mp3", files)))
# ['KUMAR', 'TOM', 'KARTHIK', 'EDIIP']
# ['a.mp3', 'b.mp3', 'c.mp3']


# Filter expenses between 4000 and 7000
ep_cost = [1000,2000,3000,4000,5000,6000,7000,8000,9000]
filtered_cost = list(filter(lambda x: 4000 <= x <= 7000, ep_cost))
print(filtered_cost)
# [4000, 5000, 6000, 7000]


# Filter names starting with a vowel
names = ['karthi', 'Visha', 'theeba', 'edipp', 'U.JOKIM', 'Iseq']
def test_vowels(x):
    return x[0].lower() in 'aeiou'
filtered_names = list(filter(test_vowels, names))
print(filtered_names)
# ['edipp', 'U.JOKIM', 'Iseq']


# Calculate total salary using reduce()
from functools import reduce
L = ['kumar,1000','arun,2000','vijay,3000','tom,4000','zion,5000']

total_salary = reduce(
    lambda a, b: int(a) + int(b),
    [var.split(",")[1] for var in L]
)
print(total_salary)
# Output: 15000




