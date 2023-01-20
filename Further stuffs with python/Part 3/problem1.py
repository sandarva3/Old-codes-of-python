#BOTH PROGRAM GIVES SAME OUTPUT.(ONLY RUN ONE AT A TIME )
#This is the code that i write after watching youtube 
def file(file): 
 try:
  with open(file, "r") as f:
    a = f.read()
 except Exception:
    print(f"sorry the file '{file}' is missing ")
 else:
   print(f"{file} is found ")
file("hiscore.txt")
file("sample.txt")
file("sample2.txt")

#This is the code written by me before watching from youtube...
def file1(): 
 try:
  with open("hiscore.txt", "r") as f:
    a = f.read()
 except Exception as e:
    print("sorry the file is missing ")
 else:
   print("file 1 is found ")
def file2(): 
 try: 
  with open("automatetheboringstuffbookpractice.py", "r") as f:
    a = f.read()
 except Exception as e:
    print("sorry the file 2 is missing ")
 else:
    print("file 2 is found")
def file3():    
 try:   
  with open("sample2.txt", "r") as f:
    a = f.read()
 except Exception as e:
    print("sorry the file 3 is missing ")
 else:
       print("file 3 is found")
file1()
file2()
file3()

   