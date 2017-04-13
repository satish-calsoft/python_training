#!/usr/bin/python
a = input("Enter a number")
b=input("Enter second number")

Operation=raw_input("Choose arithmetic operation you want to perform sch as add,sub,mul,div,mod")


if Operation=="add":
    print "Addition:",a+b
elif Operation=="sub":
    print "Subtraction:",b-a

elif Operation=="mul":
    print "multiplication:",a*b

elif Operation=="div":
    print "Division:",a/b

else:
    print "No such type of Arithmetic operation u have entered"

