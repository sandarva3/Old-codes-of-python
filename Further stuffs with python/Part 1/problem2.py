class animals:
    animal =  "Tiger"
class species(animals):
    species = "Bengal Tiger" 
class tiger(animals):
    @staticmethod
    def roar():
        print("Roar Roar")
    
t = tiger()
t.roar()
