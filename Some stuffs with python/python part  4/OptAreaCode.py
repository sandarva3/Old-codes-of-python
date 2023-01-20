import re
text = ("Here is the phone number 9779855050932")
pattern = re.compile(r"(\d{3})?\d{10}")
result = pattern.search(text)
try:
  num = result.group(1)
  num = int(num)
  if num == 977:
    print("The give phonenumber has area code")
  elif num == None:
    print("The given phone number does not have the area code")

except:
    print("The given phone number has no area code")
    
