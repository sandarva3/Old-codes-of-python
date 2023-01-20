import re
text = "Here is the text and is there are many vowels letters present in this text"
pattern = re.compile(r"[aeiou]") # This character class will return the vowels letters from the text
pattern2 = re.compile(r"[^aeiou]") # This character class will return the letters(including spaces) except vowels letter-that's because of ^ sign(it will return negative of what's in class)

print(pattern.findall(text))
print("")
print(pattern2.findall(text))