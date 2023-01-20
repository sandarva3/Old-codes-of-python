import re
with open("text.txt") as f:
    read_file = f.read()
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
search_text = pattern.search(read_file)
if search_text == None:
    print("Phone number not found")
else:
    print(f" Phone number found : {search_text.group()} ")
