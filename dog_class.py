class Dogs:
    """ Dog Class
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name.title()} is sitting")
        
    def roll(self):
        print(f"{self.name.title()} is now rolling over")
        
        
        
dogone = Dogs("saeed",30) 
dogone.sit()