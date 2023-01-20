import re
pattern = re.compile("(.*)")
text = "This is the text. \ncan this match this line? \
    Will this be able to match this line too?"
output = pattern.search(text)
print(output.group())

#By using this method we can match the new line of text
print("*********************")
pattern2 = re.compile(".*", re.DOTALL)
output2 = pattern2.search(text)
print(output2.group())