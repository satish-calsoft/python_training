#Nested if 

a = input("Enter a number: ")
#b = input("Enter second number: ")


if a < 200:
   print "Expression value is less than 200"
   if a == 150:
      print "Which is 150"
   elif a == 100:
      print "Which is 100"
   elif a == 50:
      print "Which is 50"
elif a < 50:
   print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"