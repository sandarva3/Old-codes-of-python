import re
#input_string = ("Enter the text here : Batmobile")
pattern = re.compile(r"Bat(man|mobile|car)")
result = pattern.search("Enter the text here : Batman")
print(result.group())