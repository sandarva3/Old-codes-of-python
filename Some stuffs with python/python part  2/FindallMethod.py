#Difference between two different methods
import re
text = "Here is the phone numbers : 123-123-1234 and 111-222-3333"
pattern = re.compile(r"\d{3}-\d{3}-\d{4}") #Has no groups
#search method:
search_method = pattern.search(text)
print("")
print(f"This is from search method : {search_method.group()}")

#Findall method:

findall_method = pattern.findall(text)
print(f"This is from findall method : {findall_method}")

#If there are groups in the actual text then findall method will return list of tuples 
pattern2 = re.compile(r"(\d{3})-(\d{3})-(\d{4})") #has groups
findall_method = pattern2.findall(text)
print(findall_method)
