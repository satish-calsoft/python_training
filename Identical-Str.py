a= raw_input("enter first string: ")
b= raw_input("enter second string: ")
if len(a) == len(b):
  #  print "len is equal"
    count = 0
    for i in list(a):
        if i in list(b):
            count += 1
    if count == len(a):
        print "Identical String"
    else:
        print "UnIdentical String"
else:
    print "length of two strings are not equal"