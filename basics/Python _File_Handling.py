# Python program to copy the contents of one text file to another file.

F = open("E:\\ab.txt", "r")
W = open("D:\\test1.txt", "w")
s = F.read()
W.write(s)
F.close()
W.close()
# Output: Contents of ab.txt will be copied to test1.txt


# Python program to count the number of words in a text file.
fname = input("Enter a filename: ")
F = open(fname, "r")
count = 0
for line in F:
    words = line.split()
    count += len(words)
print(count)
F.close()
# Output: Enter a filename: ab.txt
#         25


# Python program to copy an image file using binary mode.
F = open("p1.png", "rb")
WH = open("E:\\p2.jpg", "wb")
s = F.read()
WH.write(s)
F.close()
WH.close()
# Output: Image p1.png is copied as p2.jpg.


# Python program to copy data from one file to another using the with statement.
with open("process.log", "r") as FH:
    with open("p1.log", "w") as WH:
        s = FH.read()
        WH.write(s)
#Output: Contents of process.log are copied to p1.log.


