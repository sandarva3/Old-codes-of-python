import re
text = "hahahahahaha"
#Greedy matching : By default python will be greedy matching, meaning that it will match the longest version of the text
pattern = re.compile(r"(ha){3,5}")
#Non-Greedy matching: We have to make the code non-greedy by adding ? in the code , it will match the shortest version of the text 
pattern1 = re.compile(r"(ha){3,5}?")
result1 = pattern.search(text)
result2 = pattern1.search(text)
print(result1.group())
print(result2.group())

