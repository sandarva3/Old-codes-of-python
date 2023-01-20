#To match the text ignoring whether it is UPPERCASE or lowercase we should use "re.IGNORECASE" or "re.I"
import re
pattern = re.compile(r"Hello")
text = "Hello everyone"
output = pattern.search(text)
print(output.group())

#In this method it is case insensitive
pattern2 = re.compile(r"Hello", re.I)
text2 = "hello everyone"
output2 = pattern2.search(text2)
print(output2.group())