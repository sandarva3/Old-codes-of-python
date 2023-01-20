print("Do you want to enter file name and search for that file ?")
s = input("Enter Yes/No")
s = s.lower()
if s == "yes":
   r = input("enter how many files do you want to search :")
   r = int(r)
   for i in range(1,r):
    x[i] = input("Enter the name of first file :")
    def file(i):
