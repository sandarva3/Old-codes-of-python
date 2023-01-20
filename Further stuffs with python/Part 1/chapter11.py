class number:
    def __init__(self, num):
        self.num = num 
    def __add__(self,num2):
        return self.num + num2.num
    def __str__(self):
        return f" The number is : {self.num} "

n1 = number(5)
n2 = number(5)
sum = n1 + n2
print(sum)
n = number(9)
print(n)



