#This is some basic dunder method in python ! 
class dunder:
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
    def __add__(self):
        return dunder(self.no1 + self.no2)
    def __str__(self):
        return f" The result is {self.no1 + self.no2} "
c = dunder(5 ,4)
print(c)

