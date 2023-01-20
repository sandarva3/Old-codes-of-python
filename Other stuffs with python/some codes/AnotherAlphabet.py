#THIS CODE WILL WORK IF THERE IS NO SPACE IN THE WORD. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, "_"] 
conversion = []
inputlist = ["_"]
length = len(alphabet) 
#characters = True
#print("Enter '#quit' if all letters in words are completed ")
#while characters:
input1 = input("Enter :")
length2 = len(input1)
   #characters = False
#if input1 == " ":
 #  input1 = "_"
#inputlist.append(input1)
for i in range(length2):
    if (" " in input1):
        input1[i]= "_"
        input1 + input1[i]
    for j in range (length):
      if alphabet[j] == input1[i]:
          conversion.append(number[j])
print(conversion)

