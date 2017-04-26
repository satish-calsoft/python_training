d1={"What is the output of this expression, 3*1**3?":'a. 27\tb.9\nc.3\td 1',
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
    "Which of the following cannot be a variable?":"b"}

d3={"What is the output of this expression, 3*1**3?":'a. 27\t c.3',
    "Which one of the following have the highest precedence in the expression?":"b.Addition\td.Parenthesis",
    "How many except statements can a try-except block have?":"c.more than one\t d.more than zero",
    "When will the else part of try-except-else be executed?":"b.when exception occurs\t c.when no exception occurs",
    "Which of these in not a core datatype?":"c.tuples\td.classes",
    "Given a function that does not return any value, What value is thrown by itby default when executed in shell.":"b.bool\t d.None",
    "What is the return type of function id ?":"a.int\tb.float",
    "What error occurs when you execute?\n apple = mango":"b.NameError\t c.ValueError",
    "In order to store values in terms of key and value we use what core datatype.":"b.tuple\t d.Dictionary",
    "What is the return value of trunc() ?":"a.int\tb.bool",
    " Is Python case sensitive when dealing with identifiers?":"a.Yes\t b.No",
    "What is the maximum possible length of an identifier?":"c.79\t d.None",
    "Which of the following is not a keyword?":"a.eval\t c.nonlocal",
    "All keywords in Python are in?":"c.Capitalized\t d.None",
    "Which of the following cannot be a variable?":"a.__init__\t b.in"}

rupees=[0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,12500000,2500000,5000000,10000000]

j=0
count=1
c1=1
for key in d1:
    
    i=j+1
    print "Ques:",key
    print  d1[key]
    Continue=raw_input("Would you like to Continue or Quit. Press Y for continue and N for Quit: ")
    if Continue=='Y':
        lifeline=raw_input("Would you like to use lifeline or continue to choose your option. Press 'Y' for lifeline and 'N' to proceed further: ")
        
        if lifeline=='Y' and c1<2:
            print c1
            print "You are using 50-50 lifeline and here are the options"
            for key1 in d3:
                if key==key1:
                    print d3[key1]
                    ChooseOption=raw_input("Enter your option: ")
                    if ChooseOption=='a' or 'b' or 'c' or 'd':
                        if ChooseOption==d2[key]:
                            print "Right Answer.\nCongrats!!! You won", rupees[i]
                            j=j+1
                            count+=1
                            print count
            c1+=1
            print 'c1',c1
                
            

        else:
            ChooseOption=raw_input("Enter your option: ")
            if ChooseOption=='a' or 'b' or 'c' or 'd':
                if ChooseOption==d2[key]:
                    print "Right Answer.\nCongrats!!! You won", rupees[i]
                    j=j+1
                    count+=1
                    print count
            
                else:
                    print "Sorry, you choosed wrong Answer"
                    if count<=5:
                        print "You Won", rupees[0]
                
                    elif count==6 or count<=10:
                        print "You Won", rupees[5]
                    elif count==11 or count<=len(rupees):
                        print "You Won", rupees[10]
                    
                    break
            else:
                ChooseOption=raw_input("You choosed invalid option.Please choose from options ('a' or 'b' or 'c' or 'd'): ")
                continue
    elif Continue=='N':
        print "You are quit and you won",rupees[i-1]
        break
    else:
        Continue=raw_input("You choosed invalid option. Press Y for continue and N for Quit: ")
        

            
        
