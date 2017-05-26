name=raw_input("enter name:")
rollnum=input("enter rollnum:")
eng=input("enter english marks:")
tel=input("enter telugu marks:")
hin=input("enter hindi marks:")
class stu():
    def __init__(self,name,rollnum):        
        self.name=name
        self.rollnum=rollnum
        print self.name
        print self.rollnum
        
    def marks(self,eng,tel,hin):        
        self.eng=eng
        self.tel=tel
        self.hin=hin
        print eng
        print tel
        print hin
        
    def total(self):
            print self.name,'total:',self.eng+self.tel+self.hin 

clobj=stu(name,rollnum)
clobj.marks(eng,tel,hin)
clobj.total()

import sqlite3 
conn=sqlite3.connect('test1.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE stud8(name,rollnum,eng,tel,hin,total)''')
cur.execute("INSERT INTO stud8 VALUES (?,?,?,?,?,?)", (name,rollnum,eng,tel,hin,eng+hin+tel))
conn.commit()
conn.close()
##import pdb;pdb.set_trace()
##cur.execute('SELECT * FROM stu4')