#Things are tested with only words but it can be tested with any number or character.
import re
#Caret Sign : ^
pattern = re.compile(r"^hello") #adding ^ sign at beginning of pattern begins that text must start with the following word, if not then it will return None
text = "hello world"
text2 = "python hello world"
result = pattern.search(text)
print("")
print(result)
result = pattern.search(text2)
print(result)

#Dollar sign 
pattern2 = re.compile(r"hello$")#adding $ sign at the end of the pattern means that the text must ends with the following word, if not then it will return None
text3 = "something said hello"
text4 = "hello something said"
result = pattern2.search(text3)
print(result)
result = pattern2.search(text4)
print(result)

#Both 
pattern3 = re.compile(r"^\d+$")
text5 = "234524352435"
result = pattern3.search(text5)
print(result)
print("")
