import re
input_string = input("Enter a text here :")
phoneregex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneregex.search(input_string)
if mo == None:
    print("phone number is not found ! ")
else:
    print(f"Phone number found: {mo.group()}")
