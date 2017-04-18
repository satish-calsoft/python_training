import os
import glob

a = raw_input("enter word: ")
os.chdir("C:\Users\Admin\Desktop\cuba files")
for i in glob.glob("*.txt"):
    f = open(i,'r')
    for line in f:
        if a in line:
            print f.name
            break
      
   