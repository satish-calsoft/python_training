class scoreboard():
    
    
    def __init__(self):
        
        pass
    
    def player_score(self):
        
        self.name = raw_input("Enter player name::")
        self.fours = input("Enter no.of 4's::")
        self.sixes = input("Enter no.of 6's::")
        self.other_run = input("Enter runs")
        
        self.total = (self.fours*4) + (self.sixes*6) + self.other_run
        
        self.fileop()
        
        #return self.total,self.fours,self.sixes,self.other_run
    
    def total_score(self):
        
        pass 
    
    def fileop(self):
        
        st1 = self.name+","+str(self.fours)+","+str(self.sixes)+","+str(self.other_run)+","+str(self.total)+"\n"
        
        print st1
        f1 = open("data.csv","a+")
        f1.writelines(st1)
        f1.close()
        
        


obj1 = scoreboard()
obj1.player_score()






    

    
    

