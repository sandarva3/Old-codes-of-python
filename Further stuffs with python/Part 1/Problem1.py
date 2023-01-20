class c2vec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f" {self.icap}i + {self.jcap}j "

class c3vec(c2vec):
    def __init__(self,i,j,k):
      super().__init__(i,j)
      self.kcap = k
    
    def __str__(self):
        return f" {self.icap}i + {self.jcap}j + {self.kcap}k "

v2d = c2vec(1, 2)
v3d= c3vec(3, 4, 5)
print(v2d)
print(v3d)