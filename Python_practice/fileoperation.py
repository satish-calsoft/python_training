file1 = raw_input("Enter a filename to create for the data:")
file2 = raw_input("Enter a filename to create for the copy operation")

fopen1 = open(file1,"w")

str1 = raw_input("Enter text to copy::")


fopen1.write(str1)
fopen1.close()

f3 = open(file1,"r")
f4 = open(file2,"r+")

str2 = f3.readlines()
print type(str2)

for i in str2:
    f4.write(i)
f3.close()
f4.close()