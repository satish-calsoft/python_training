class student():
    
    def __init__(self,rollno,name,ph_no = None):
        self.rollno = rollno
        self.name = name
        self.ph_no = ph_no
        
        
    def marks(self,eng=0,math=0):
        
        self.eng = eng
        self.math = math
    
    @staticmethod
    
    def sai():
        print cls.rollno
        print "sai"
    
    def total(self):
        
        return self.eng+self.math
   
    def mobile(self):
        if self.ph_no:
            return "mobile no is %d"%self.ph_no
        else:
            return "has no mobile number"

class school(student):
    
    pass

student1 = student(1,"sai")
student2 = student(2,"krishna",9676083138)

student1.marks(10,20)
student2.marks(30,40)

t1 = student1.total()

t2 = student2.total()
m1 = student1.mobile()
m2 = student2.mobile()


#below is the satatic method
student.sai()
student.marks(50,60)
        
        
print "student %s has total marks of %d and " %(student1.name,t1),m1
print "student %s has total marks of %d and " %(student2.name,t2),m2
        
        
        
        
        
