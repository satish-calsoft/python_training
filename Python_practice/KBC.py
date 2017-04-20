import random
dict1 ={"Which of these sounds would you associate with the heart ?":"D",
        "Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series' ":"C",
        "In 2013, where did the natural calamity known as Himalayan tsunami occur?":"A",
        "Which film is this song from ?--Lungi dance":"B",
        "In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me' ?":"C",
        "Who is the only leader to be elected Prime Minister of Pakistan three times ?":"D",
        "The black widow, which eats the male counterpart after mating, as a female species of which animal ?":"C",
        "Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products ?":"B",
        "In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place ?":"A",
        "Which of these persons has not walked on the Moon ?":"B",
        "Who was the chairman of the Indian Calendar Reform Committee that initiated the adoption of Saka calendar as the Indian national Calendar ?":"A",
        "'The Phrase 100 crore Club', often mentioned in Indian media nowadays, refers to which one of the following ? ":"D",
        "The 'sasural' of which of these international sports person from India is in Pakistan ? " : "B",
        "Which team retained the ashes Trophy in 2013 ? ":"D",
        "With Which of these cards would you associate the phrase 'Aam Aadmi ka Adhikaar'?" :"C",
        "Which of these words or phrases was famously used in many of his dialogues by actor Pran? ":"B"
        
        
        
        
        }
dict2 ={"Which of these sounds would you associate with the heart ?":"[A]Tring Tring,[B]Tap Tap,[C]Click Click,[D]Dhak Dhak",
        "Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series' ":"[A]Tipu Sultan,[B]Chandragupta Maurya,[C]Maharana Pratap,[D]Ashoka",
        "In 2013, where did the natural calamity known as Himalayan tsunami occur?":"[A]Uttrakhand,[B]Arunachal Pradesh,[C]Jammu and Kashmir,[D]Sikkim",
        "Which film is this song from ?--Lungi dance":"[A]Mere Dad Ki Maruti,[B]Chennai Express,[C]Ghanchakkar,[D]Race 2",
        "In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me' ?":"[A]Surpanakha,[B]Khara,[C]Maricha,[D]Dushana",
        "Who is the only leader to be elected Prime Minister of Pakistan three times ?":"[A]Syed Yousaf Raza Gillani,[B]Benazir Bhutto,[C]Liaqat Ali Khan,[D]Nawaz Sharif",
        "The black widow, which eats the male counterpart after mating, as a female species of which animal ?":"[A]Sloth,[B]Ant,[C]Spider,[D]Termite",
        "Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products ?":"[A]Mobile Phone,[B]Computer Mouse,[C]Bluetooth Mouse,[D]Digital camera",
        "In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place ?":"[A]Diamond Harbour,[B]Darjeeling,[C]Murshidabad,[D]Dhaka",
        "Which of these persons has not walked on the Moon ?":"[A]Charles Duke,[B]James A Lovell,[C]Alan Bean,[D]Pete Conrad",
        "Who was the chairman of the Indian Calendar Reform Committee that initiated the adoption of Saka calendar as the Indian national Calendar ?":"[A] Meghnad Saha,[B],Subrahmanyan Chandrasekhar,[C] Prabodh Chandra Sengupta,[D] Vainu Bappu",
        "'The Phrase 100 crore Club', often mentioned in Indian media nowadays, refers to which one of the following ? ":"[A] Viewership of an IPL match,[B] Election expenditure,[C] Population of countries,[D] Films box office collections",
        "The 'sasural' of which of these international sports person from India is in Pakistan ? " : "[A] Saina Nehwal,[B] Saina Mirza,[C] Anisa Sayyed,[D] Anjum Chopra",
        "Which team retained the ashes Trophy in 2013 ? ":"[A] Australia,[B] South Africa,[C] West Indies,[D] England",
        "With Which of these cards would you associate the phrase 'Aam Aadmi ka Adhikaar'?" :"[A] PAN Card,[B] Voter ID Card,[C] AADHAR Card,[D] Ration Card",
        "Which of these words or phrases was famously used in many of his dialogues by actor Pran? ":"[A] Khamosh,[B] Barkhurdaar,[C] Jaani,[D] Babu Moshai"
        }

dict3 ={"Which of these sounds would you associate with the heart ?":"[A]Tring Tring,[D]Dhak Dhak",
        "Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series' ":"[A]Tipu Sultan,[C]Maharana Pratap",
        "In 2013, where did the natural calamity known as Himalayan tsunami occur?":"[A]Uttrakhand,[D]Sikkim",
        "Which film is this song from ?--Lungi dance":"[B]Chennai Express,[C]Ghanchakkar",
        "In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me' ?":"[A]Surpanakha,[C]Marichaa",
        "Who is the only leader to be elected Prime Minister of Pakistan three times ?":"[C]Liaqat Ali Khan,[D]Nawaz Sharif",
        "The black widow, which eats the male counterpart after mating, as a female species of which animal ?":"[C]Spider,[D]Termite",
        "Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products ?":"[B]Computer Mouse,[D]Digital camera",
        "In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place ?":"[A]Diamond Harbour,[C]Murshidabad",
        "Which of these persons has not walked on the Moon ?":"[A]Charles Duke,[B]James A Lovell",
        "Who was the chairman of the Indian Calendar Reform Committee that initiated the adoption of Saka calendar as the Indian national Calendar ?":"[A] Meghnad Saha,[B],Subrahmanyan Chandrasekhar",
        "'The Phrase 100 crore Club', often mentioned in Indian media nowadays, refers to which one of the following ? ":",[C] Population of countries,[D] Films box office collections",
        "The 'sasural' of which of these international sports person from India is in Pakistan ? " : "[B] Saina Mirza,[C] Anisa Sayyed",
        "Which team retained the ashes Trophy in 2013 ? ":"[A] Australia,[D] England",
        "With Which of these cards would you associate the phrase 'Aam Aadmi ka Adhikaar'?" :"[B] Voter ID Card,[C] AADHAR Card",
        "Which of these words or phrases was famously used in many of his dialogues by actor Pran? ":"[A] Khamosh,[B] Barkhurdaar"
        }




money = {15:10000000,14:5000000,13:2500000,12:1250000,11:640000,10:320000,
         9:160000,8:80000,7:40000,6:20000,5:10000,4:5000,3:3000,2:2000,1:1000,0:0}
val = 1
val1 = 0

choice = ["50-50","swap"]

print "Welcome to KBC"
str1 = raw_input("Please enter your Name::")
print "Welcome %s...Lets play the GAME....." %str1


for i in random.sample(dict2.keys(),15):
    

    str1 = dict2[i]
    str1 = str1.split(",")
    print val,":",i
    val = val+1
    
    while 1:
        
        opt = []
        #The below for loop is for printing the options
        for f  in range(len(str1)) :
            print str1[f]
        
        #The below list opt is for to compare the result with available options
        for j in str1 :
            opt.append(j[1])
        opt.append("1")
        opt.append("2")
        
        k = raw_input("\nSelect your Answer or Press 1 to Quit or Press 2 for Choice::")
        k = k.upper()
            
        if k not in opt:
            
            print "Select only from below options or Press 1 to Quit or Press 2 for Choice::"

            #below elif for Choices(50-50,swap)
        elif k == '2':
                print "Select one choice "
                
                if  len(choice) != 0:
                    
                    for it1 in choice:
                        print it1
                        
                    while 1:
                        choice2 =raw_input("Enter your choice or q to quit::")
                        if choice2 == "q" or choice2 =="Q":
                            break
                        if choice2 not in choice:
                            print "Select correct choice:"
                            
                        if choice2 == "50-50":
                            choice.remove("50-50")
                            str1 = dict3[i]
                            str1 = str1.split(",")
                            print val-1,":",i
                
                            break
                            
                        elif choice2 =="swap":
                            choice.remove("swap")
                            i = "Which of these words or phrases was famously used in many of his dialogues by actor Pran? "
                            str1 = dict2[i]
                            str1 = str1.split(",")
                            print val-1,":",i
                               
                            break
                        
                else:
                    print "You have no choices"
        else:
            break
    
    #The below if for Quit
    if k =='1':
        break
        
    
    #The below if and else is for each Question correct or wrong
    
    if k == dict1[i]:
        val1 = val1+1
        print "Correct and you have earned amount of %d" %money[val1]
        
        if val1 == 5 or val1 == 10 :
            print "You have entered check point"  
    else :
        print "Wrong answer and please SMS the answer to SATISH VARMA"
        break

# Money comaprison
        
if val1 > 5 and val1 < 10 and k != '1':
    val1 = 5
    print "Congrats! You have earned a money of %d" %money[val1]
elif val1 >10 and val1 < 15 and k != '1':
    val1 = 10
    print "Congrats! You have earned a money of %d" %money[val1]
elif k == '1':
    print "Congrats! You have earned a money of %d" %money[val1]
else:
    print "Congrats! You have earned a money of %d" %money[val1]


    
