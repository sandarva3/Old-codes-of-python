import re
pattern = re.compile(r"bat(wo)*man")
text = ("This is the text and here is the batman")
text2 = ("This is text and here is the batwoman")
text3 = ("This is the text and here is the batwowowowoman")
result1 = pattern.search(text)
result2 = pattern.search(text2)
result3 = pattern.search(text3)
print(result1.group())
print(result2.group())
print(result3.group())
print("all three will work")