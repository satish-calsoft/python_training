class stu():
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
        print self.name
        print self.rollnum
        
    def marks(self,eng=0,tel=0,hin=0):            
            self.eng=eng
            self.tel=tel
            self.hin=hin
            print eng
            print tel
            print hin
        
    def total(self):
            print self.name,'total:',self.eng+self.tel+self.hin 

clobj=stu('suseela',78)
clobj.marks(10,20,30)
clobj.total()
            
            
            
        