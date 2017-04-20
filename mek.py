
mek={"who r yu?":['man','coder','animal','human'],'What is first alphabate?':['b','a','c','z'],'how many angles of a triangle?':['Not have any','Two','Three','So Many'],'how many edgs of a square?':['1','2','3','4'],'What is Basic need for humanlife?':['money','water','air','None of These'],'what is python?':['pop','oop','sap','tcp/ip']}
mek_ans={"who r yu?":'a','What is first alphabate?':'b','how many angles of a triangle?':'c','how many edgs of a square?':'d','What is Basic need for humanlife?':'b','what is python?':'b'}
mek_prize_amounts={'who r yu?':1000,'What is first alphabate?':2000,'how many angles of a triangle?':3000,'how many edgs of a square?':4000,'What is Basic need for humanlife?':10000,10:320000}
prize_amount=0
count=0
def fun(i):
                print "a){0}\tb){1}\tc){2}\td){3}".format(mek[i][0],mek[i][1],mek[i][2],mek[i][3])
                ans=raw_input("Select your Answer: ")
                if ans == 'quit':
                                print "Good Bye you earned: {}"
                                exit(0)
                print ans
                if ans == mek_ans[i]:
                                print 'checking'
                                print "right answer"
                                #if mek_prize_amounts.has_key(i):
                                 #               print "you won prize amount {}".format(mek_prize_amounts[i])
                                if count==1:
                                                print "you won: 1000RS"
                                if count==5:
                                                print "you won: 5000RS"
                                if count==6:
                                                print "you won: 32000RS"
                                
                                                
                else:
                                print "wronge answer"
                                print "you loose. . .Try Again"
                                exit(0)

#for count in range(1,len(mek),1):
for i in mek:
                count=count+1
                if i is "who r yu?" or 'What is first alphabate?' or 'how many angles of a triangle?':
                                print count,". ",i
                                if i is "who r yu?":
                                                fun(i)
                                if i is "What is first alphabate?":
                                                fun(i)
                                if i is "how many angles of a triangle?":
                                                fun(i)
                                if i is 'how many edgs of a square?':
                                                fun(i)
                                if i is 'What is Basic need for humanlife?':
                                                fun(i)
                                if i is 'what is python?':
                                                fun(i)


