class employee:
    salary = 500
    increment = 2
    
    @property
    def afterinc(self):
        return self.salary * self.increment
    
    @afterinc.setter
    def afterinc(self,afterinc):
        self.increment = afterinc / self.salary

e = employee()
print("The salary is :", e.salary)
print("The increment value is :", e.increment)
print("The salary after increment is : ", e.afterinc)
e.afterinc = 5000
print(f" The increment value for salary {e.afterinc} is {e.increment} ")

    