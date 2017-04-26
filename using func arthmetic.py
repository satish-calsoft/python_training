#!/usr/bin/python

def add(*x):
   radd=0
   """This function multiplies two numbers"""
   for i in x:
      radd=radd+i
   return radd

def sub(*x):
   """This function divides two numbers"""
   rsub=0
   for i in x:
      rsub=i-rsub
   return rsub
def mul(*x):
   rmul=1
   """This function multiplies two numbers"""
   for i in x:
      rmul=rmul*i
   return rmul

def div(x, y):
   """This function divides two numbers"""
   return x / y
def square(x):
   """This Function squares the number"""
   return x*x
def cube(x):
   """This Function cubes the given number"""
   return x*x*x
def inv(x):
   """This Function calculates inverse the given number"""
   return x**(-1)

def power(x,y):
   
   """This functions multiplies with the power value"""
   return x**y
def tenx(x):
   """This function multiplies 10 with the power of x value"""
   return 10**x

def factorial(x):
   rf=1
   for i in range(1,x+1):
      if i <=x:
         rf = rf * i
   return rf
def cuberoot(x):
   return x**(3**-1)
def ythroot(x,y):
   return x**(y**-1)


I1 = input("Enter first number: ")
I2 = input("Enter second number: ")

print "Addition:",add(I1,I2)

print "Subtraction: ",sub(I1,I2)

print "Multiplication: ",mul(I1,I2)

print "Division: ",div(I1,I2)

print "Square: ",square(I1)
print "Cube: ",cube(I1)
print "Power: ",power(I1,I2)
print "xth power of 10:",tenx(I1)
print "Factorial:",factorial(I1)
print "Inverse:",inv(I1)
print "Cuberoot of x: ",cuberoot(I1)
print "ythroot of x: ",ythroot(I1,I2)
