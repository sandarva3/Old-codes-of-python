#THIS CODE WILL WORK EVEN IF THERE IS SPACE IN THE WORD. BUT WE CANNOT ENTER THE ENTIRE LETTER OF THE WORD IN SINGLE LINE.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, "_"] 
conversion = []
inputlist = []
length = len(alphabet) 
characters = True
print("Enter '#quit' if all letters in words are completed ")
while characters:
 input1 = input("Enter :")
 if input1 == "#quit":
    characters = False
 elif input1 == " ":
    input1 = "_"
 inputlist.append(input1)
length2 = len(inputlist)
for i in range(length2):
 for j in range (length):
      if alphabet[j] == inputlist[i]:
          conversion.append(number[j])
     

print(conversion)

