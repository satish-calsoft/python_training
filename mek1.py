person=raw_input("Enter your Name: ")
print "Hi",person,"\n","Welcome to meelo evaru kotiswarudu"
d1={"What is the output of this expression, 3*1**3?":'a.27\tb.9\nc.3\td 1',
    "Which one of the following have the highest precedence in the expression?":"a.Exponential\t\t b.Addition\nc.Multiplication\td.Parenthesis",
    "How many except statements can a try-except block have?":"a.zero\tb.one\nc.more than one\td.more than zero",
    "When will the else part of try-except-else be executed?":"a.always\tb.when exception occurs\nc.when no exception occurs\td.None",
    "Which of these in not a core datatype?":"a.lists\t\tb.dictionary\nc.tuples\td.classes",
    "Given a function that does not return any value, What value is thrown by itby default when executed in shell.":"a.int\tb.bool\nc.void\td.None",
    "What is the return type of function id ?":"a.int\tb.float\nc.bool\td.dict",
    "What error occurs when you execute?\n apple = mango":"a.SyntaxError\tb.NameError\nc.ValueError\td.TypeError",
    "In order to store values in terms of key and value we use what core datatype.":"a.List\tb.tuple\nc.Class\td.Dictionary",
    "What is the return value of trunc() ?":"a.int\tb.bool\nc.float\td.None",
    " Is Python case sensitive when dealing with identifiers?":"a.Yes\tb.No\nc.Sometimes only\td. None",
    "What is the maximum possible length of an identifier?":"a.31\tb.63\nc.79\td.None",
    "Which of the following is not a keyword?":"a.eval\tb.Assert\nc.nonlocal\td.pass",
    "All keywords in Python are in?":"a.Uppercase\tb.Lowercase\nc.Capitalized\td.None",
    "Which of the following cannot be a variable?":"a.__init__\tb.in\nc.it\td.on"}
    
 
d2={"What is the output of this expression, 3*1**3?":'c',
    "Which one of the following have the highest precedence in the expression?":"d",
    "How many except statements can a try-except block have?":"d",
    "When will the else part of try-except-else be executed?":"c",
    "Which of these in not a core datatype?":"d",
     "Given a function that does not return any value, What value is thrown by itby default when executed in shell.":"d",
    "What is the return type of function id ?":"a",
    "What error occurs when you execute?\n apple = mango":"b",
    "In order to store values in terms of key and value we use what core datatype.":"d",
    "What is the return value of trunc() ?":"a",
    " Is Python case sensitive when dealing with identifiers?":"a",
    "What is the maximum possible length of an identifier?":"d",
    "Which of the following is not a keyword?":"a",
    "All keywords in Python are in?":"d",
    "Which of the following cannot be a variable?":"b" }


    
cash=[0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,6400000,1250000,2500000,5000000,10000000]
j = 0
count = 0
for i in d1:
    
    k=j+1        
    print i
    print d1[i]
           
        
    
    YN= raw_input("Do You want to Continue Or Quit Press Y or N:")
    if YN=='Y':
         ans=raw_input("your answer")
         if ans=='a'or'b'or'c'or'd':
             if d2[i]==ans:
                 print "Correct Answer"
                 print "you won",cash[k]
                 j=j+1
                 count=count+1
                 
                 
             else:
                print "Sorry wrong answer,Better luck next time"
                if count<=5:
                    print "Sorry you did not won anything"
                elif count>5<=10:
                    print "You won 10000rs"
                elif count>10<=15:
                    print "You won 320000rs"
                               
                    
                break
            
        
         else:
             print "Invalid Input\nPlease choose options from a b c d"
             ans=raw_input("your answer")

    elif YN=='N':
        print "You won", cash[j]
        break
             
                        
    else:
        print "You entered invalid input,Please Choose Y or N"
        YN= raw_input("Do You want to Continue Or Quit Press Y or N:")
        
        
        
   
   
          
                 
   

 
