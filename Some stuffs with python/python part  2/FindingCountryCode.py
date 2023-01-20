import re
input_string = input("Enter a number :")
pattern = re.compile(r'(\d{3})(\d{10})')
country_code = pattern.search(input_string)
code = country_code.group(1)
code = int(code)
if code == 977:
    print("Your number belong to Nepal")
    print(f" And your phone number is {country_code.group(2)} ")
else:
    print("Your number does not belong to Nepal")
