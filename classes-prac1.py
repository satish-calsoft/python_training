class abc():
    def __init__(self,a,b):
        a= a
        self.b= b
        
        print a,self.b
    var=1
    def func(self):
        print "class method"
        print self.b
obj = abc(2,3)

print obj.func()
print "#################"
class stu():
    def __init__(self,name,branch,blog):
        self.name = name
        self.branch = branch
        self.blog = blog
        print self.name,self.branch,self.blog
    def marks(self,python = 0,eng = 0,tel = 0):
        self.python = python
        self.eng = eng
        self.tel = tel
        print "marks:",self.python,self.eng,self.tel
    def total(self):
        print self.python+self.eng+self.tel
#obj1 = stu()
x = stu("robo", "mech", 2)
x.marks(77,88,99)
y = stu("raja","cse",1)

y.marks(45,56,43)
x.total()   