def fib(n):
    a,b=10,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print fib(5)
##################
def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

n = int(raw_input("please, enter a number "))
for fib in fibs():
  if n == fib:
    print "your number is a Fibonacci number!"
    break
  if fib > n:
    print "your number is not a Fibonacci number!"
    break
#####################
def fibo(m):
    a,b = 0,1
    for i in xrange(m):
        print a
        a,b = b, a+b

num = input("enter no: ")
for i in fibo(num):
    print "i = ", i
