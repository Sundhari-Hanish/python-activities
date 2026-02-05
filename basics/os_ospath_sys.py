os, os.path and sys modules

Q1. Using os module display the list of all environment variables and the total number of variables.

import os
e_vars = os.environ
for k, v in e_vars.items():
    print(k, "=", v)
print("Total environment variables:", len(e_vars))

Output:
(PATH=/usr/bin:...)
Total environment variables: <count>


Q2. Using os module display the login name and login directory path.

import os
print("Login Name:", os.getlogin())
print("Home Directory:", os.path.expanduser("~"))

Output:
Login Name: user
Home Directory: /home/user


Q3. How to test whether the environment variable DB is existing or not?

import os
if "DB" in os.environ:
    print("DB environment variable exists")
else:
    print("DB environment variable does not exist")

Output:
DB environment variable does not exist


Q4. Using os.uname(), display kernel name, version.

import os
u = os.uname()
print("Kernel Name:", u.sysname)
print("Kernel Version:", u.release)

Output:
Kernel Name: Linux
Kernel Version: 5.x.x


Q5. Write a python script:

a. Display your current working directory.  
b. Change it to /etc directory  
c. Copy the list of all filenames into local variable  
d. Write all the files into an external file.  
e. Display the total no.of files under /etc directory.

import os
print("Current Directory:", os.getcwd())
os.chdir("/etc")
print("Changed Directory:", os.getcwd())
files = os.listdir(".")
with open("etc_files.txt", "w") as f:
    for file in files:
        f.write(file + "\n")
print("Total number of files:", len(files))

Output:
Current Directory: /home/user
Changed Directory: /etc
Total number of files: <count>


Q6. Write a python script:

a. Test an input file is existing or not.  
[ Use Command line arguments to take input. ]  
b. Before testing the file existence, perform the following validation.  
i) Input file and script file must be different.  
ii) command line argument is not an empty argument.  
iii) command line argument should not take more than one input file.

import sys
import os
if len(sys.argv) != 2:
    print("Provide exactly one input file")
    sys.exit(1)
input_file = sys.argv[1]
if not input_file:
    print("Empty argument provided")
    sys.exit(1)
if input_file == sys.argv[0]:
    print("Input file and script file must be different")
    sys.exit(1)
if os.path.exists(input_file):
    print("File exists")
else:
    print("File does not exist")

Output:
File exists


Q7. Write a python script:
a. create a new directory under your login path.  
b. validate whether the input directory is existing or not.  
c. if directory exists, display attributes using ls -ld  
d. if directory doesn’t exist, create it  
e. copy list of .sh files into new directory  
f. change to new directory  
g. give execute permission to all users  
h. execute all .sh files and redirect output to /var/log/Test1.log

import os
dir_name = os.path.expanduser("~/TestDir")
if os.path.exists(dir_name):
    os.system("ls -ld " + dir_name)
else:
    os.mkdir(dir_name)
os.system("cp *.sh " + dir_name)
os.chdir(dir_name)
os.system("chmod 777 *.sh")
os.system("./*.sh > /var/log/Test1.log")

Output:
Directory created / validated successfully


Q8. Write a python script:

a. read input file using command line argument  
b. test whether file exists  
c. check whether regular file or directory  
d. display file or directory details

import sys
import os
file = sys.argv[1]
if os.path.exists(file):
    stat = os.stat(file)
    if os.path.isfile(file):
        print("Regular File")
        print(stat)
        print("Inode:", stat.st_ino)
    elif os.path.isdir(file):
        print("Directory File")
        print(stat)
        print("Block Size:", stat.st_blksize)
    else:
        print("Not a regular file or directory")
else:
    print("File does not exist")

Output:
Regular File
Inode: <number>


Q9. Write a python script to copy webcam pictures every 5 minutes into hourly and daily directories.

import time
import os
base_dir = "/var/www/webcam"
os.makedirs(base_dir, exist_ok=True)
while True:
    day = time.strftime("%Y-%m-%d")
    hour = time.strftime("%H")
    path = os.path.join(base_dir, day, hour)
    os.makedirs(path, exist_ok=True)
    os.system("cp /tmp/webcam.jpg " + path)
    time.sleep(300)

Output:
Script runs in background


Q10. Predict the output

a.
import os.path
os.path.ismount("/")

Output:
True


b.
import os.path
os.path.basename("/etc/passwd")

Output:
passwd


c. How to test "bs4" module is exist or not?
Program:

import sys
if "bs4" in sys.modules:
    print("bs4 module exists")
else:
    print("bs4 module not loaded")


d. How to add external file into sys.path and test module loading?

import sys
sys.path.append("/home/userA/Project")
import AB
print("AB module loaded")

Output:
AB module loaded

