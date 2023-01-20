import re
text = ("Here is the string Superwoman ")
a = re.compile(r"Super(wo)?man")
b = a.search(text)
print(b.group())