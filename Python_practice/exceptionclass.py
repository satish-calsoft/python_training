class Networkerror(IndexError):
    def __init__(self):
        
        IndexError.__init__(self,"index out")
        