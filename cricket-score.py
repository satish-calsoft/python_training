class cricket():
    def __init__(self,name,country):
        self.name=name
        self.country=country
        print self.name,"from:",self.country
    
    def score(self,runs,catches,wickets):
        self.runs = runs
        self.wickets = wickets
        self.catches = catches
        print "runs: ",self.runs,",catches: ",self.catches,",wickets: ",self.wickets

x = cricket("Gambir", "India")
x.score(97, 80, 2)
y = cricket("sehwag", "India")
y.score(319, 99, 13)