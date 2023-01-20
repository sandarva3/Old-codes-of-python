import re
text = "haha"
text3 = "hahahahaha"
text4 = "hahahahahahahahahahahahahahaha"
#This pattern will only match the text that is only repeated 2 times
pattern1 = re.compile(r"(ha){2}")
#This pattern will only match the text that is repeated from 2 to 5 times
pattern2 = re.compile(r"(ha){2,5}")
#This pattern will match the text that is repeated from at least 2 to any number of times
pattern3 = re.compile(r"(ha){2,}")
result1 = pattern1.search(text)
result2 = pattern2.search(text3)
result3 = pattern3.search(text4)
print(result1.group())
print(result2.group())
print(result3.group())
