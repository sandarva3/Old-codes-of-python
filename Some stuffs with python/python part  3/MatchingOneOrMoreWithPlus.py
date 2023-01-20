import re
import re
pattern = re.compile(r"bat(wo)+man")
print("")
text = ("This is the text and here is the batman and this will return none because while using + sign the character/s must appear once.")
text2 = ("This is text and here is the batwoman")
text3 = ("This is the text and here is the batwowowowoman")
result1 = pattern.search(text)
result2 = pattern.search(text2)
result3 = pattern.search(text3)
if result1 == None:
    print(text)
print(result2.group())
print(result3.group())
