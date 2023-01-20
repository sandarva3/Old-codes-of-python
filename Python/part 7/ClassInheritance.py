class Mamal:
    def kangaroo(self):
        print("kangaroo can run very fast")
    def anothermamal(self):
        print("Is there any mamal that can run as fast as kangaroo ?")
   # def __init__(self):
   #     a = "this is the initializer in class Mamal"
   #     return a
class Insects(Mamal):
    def dragonfly(self):
        print("Dragonfly can fly.")
    def anotherinsect(self):
        print("Can kangaroo fly ?")
b = Mamal()
b.anothermamal()
c = Insects()
c.anothermamal()



