import pyinputplus as pyip
response = pyip.inputNum("Enter a number :",allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'],blockRegexes=[r"[!@#$]"])

#When using both the allow regex override the block regex