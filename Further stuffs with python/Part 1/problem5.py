# I did not write full code of this, i checked this part after copying code and it didn't worked ... so i didn't understand the code
class vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 =""
        index = 0
        for i in self.vec:
            str1 +=  f" {i}a{index} +"
            index +=1
            return str1[:-1]

v1  = vector([1,2,4,5,6,3])
print(v1)
