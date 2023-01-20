import re
a = re.compile(r".at")

b = a.findall("This is the string at the table fat mat and hat datt okat datthatt ")
print(b)
