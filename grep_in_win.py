import os

def grep(file_name):
    with open(file_name) as textfile:
        filelines = textfile.readlines()
        for line in filelines:
            if instring in line:
                print '>>>{} \n{}'.format(file_name, line)


def grep_dir(file_name):
    for dir, tmp1, tmp2 in os.walk(file_name):
        for files in os.listdir(dir):
            filepath = os.path.join(dir, files)
            if os.path.isfile(filepath):
                grep(filepath)


infile = raw_input('Enter file name or directory path: ')
instring = raw_input('Enter the string to search: ')

if os.path.isdir(infile):
    grep_dir(infile)
else:
    grep(infile)