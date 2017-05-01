

q=['1.what has been e currency of Greece sine 2002?','\n2.Which among these is an Island country ?','\n3.What do the five rings of the Olympics represent?','\n4.Which of these actress is married to a professional golfer?','\n5.Which of these is not a work of Kalidas?','\n6.Which of these world champions is a parent of twins?','\n7.Which of these names means ‘lightning’?','\n8.Which of these names means ‘gold-like’?','\n9.Which of these is the name for a kind of shot in badminton ? ','\n10.Which of these cannot be the same for two different persons ?','\n11.Which of these is the title of a film directed by Rohit Shetty ? ','\n12.Which of these Chief Minister of an Indian State is an IIT Graduate ? ','\n13.How many bones does an elephant’s trunk have ?','\n14.What does a Kilo equal to, as in kilometre or kilogram ? ','\n15.Who is the first woman to become CEO of the soft drink giant PepsiCo ?']
op=['(A) Euro\t (B) peso \n(C) Drachma\t (D) Lira','(A) Yemen\t (B) Maldives \n(C) Oman\t (D) Peru','(A) Five games\t\t (B) Five languages \n(C) Five continents \t (D) Five oceans','(A) Chitrangada Singh\t (B) Celina Jaitly \n(C) Esha Deol\t\t (D) Ayesha Takia','(A) Raghuvamsham\t (B) Meghadutam \n(C) Vikramorvasiyam\t (D) Kadambari','(A) Sushil Kumar\t (B) M. C. Mary Kom \n(C) Vishwanathan Anand\t (D) Gagan Narang','(A) Saumaya\t (B) Damani\n(C) Shreya\t (D) Mahima','(A) Sonakshi\t (B) Sonam \n (C) Sumita \t (D) Sanjana','(A) Bounce\t (B) Yorker \n(C) Drop \t (D) Bout','(A) Fingerprints\t (B) Skin Colour \n(C) Blood Group \t (D) Eye Colour','(A) Devgan Vaani \t (B) Shetty Salah \n(C) Chal Chopra \t (D) Bol Bachchan','(A) Manohar Parrikar \t (B) Okram Ibobi Singh.\n(C) Kiran Kumar Reddy \t (D) Omar Abdullah','(A) 5\t\t (B) 1 \n(C) 10\t (D) 0','(A) 10 \t\t (B) 100 \n (C) 10000 \t (D) 1000','(A) Virginia Rometty \t (B) Indra Nooyi \n(C) Ursula Burns \t (D) Meg Whitman']
a=['A','B','C','A','D','B','B','B','C','A','D','A','D','D','B']
amt=[1000,2000,3000,5000,10000,20000,40000,800000,160000,320000,640000,1250000,250000,5000000,100000000]


print (" WELCOME TO KAUN BANEGA CROREPATI GAME \n".rjust(60))

for i in range(len(q)):
                print q[i]
                print op[i]
                if i<5:
                                s=raw_input("\n Please select answer option (A/B/C/D):")
                
                                
                                if s==a[i] or s==a[i].upper() or s==a[i].lower(): 
                                                print " \n Yes your correct answer you won rupees:",amt[i]
                                else:
                                                print "\n Sorry Your answer is wrong you can leave the Game and you Won 0 rupees"
                                                break                                       
                elif 4<i:
                                u=raw_input("\n Do you want to continue or not (y/n) :")
                                
                                if u=='yes'or u=='y'or u=='YES'or u=='Y':
                                                s=raw_input("\n Please select answer option (A/B/C/D):")
                                elif u=='no' or u=='n' or u=='NO' or u=='N':
                                                if (i<4):
                                                                print ("\n Please quit the game you Won 0 rupees")
                                                                break 
                                                elif 4<i<9 or 10<i<14:
                                                                print "\n Please quit the game you Won:", amt[i-1]
                                                                break               
                                else:
                                                s=raw_input("\n You entered wrong please do you want to continue or (y/n):")
                                                s=raw_input("\n Please select answer option (A/B/C/D):")
                                                
                                                
                                if s==a[i] or s==a[i].upper() or s==a[i].lower(): 
                                                print " \n Yes your answer is correct you reached safe level and you WON rupees: ",amt[i]  
                                                
                                elif i==5 or i==6 or i==7 or i==8:
                                                amt[i]=amt[4]
                                                print "\n Sorry your answer is wrong this level finally you won rupees as: ",amt[i]
                                                print "\n you can leave the Game"
                                                break
                                
                                elif i==10 or i==11 or i==12 or i==13:
                                                amt[i]=amt[9]
                                                print "\n Sorry for this level finally you won rupees as: ",amt[i]
                                                print "\n You can leave the Game"
                                                break  
                                else:
                                                print "\n Sorry Your answer is wrong you can leave the Game and you Won 0 rupees"
                                                break                        
                
                        
                
            


        
        
        
        
        
        
        
    

