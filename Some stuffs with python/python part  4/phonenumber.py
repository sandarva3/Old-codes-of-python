def phonenumber(text):
    if len(text) == 12:
        if text[3] and text[7] == "-":
            if text[0:2].isdecimal() == True and text[4:6].isdecimal() == True and text[8:11].isdecimal() == True:
                return True
            else:
                return False

        else:
            return False

    else:
        return False


message = input("Enter text :")
for i in range (len(message)):
    chunk = message[i:i+12]
    if phonenumber(chunk) == True:
        print(f"The phone number is {chunk} ")
        
print("Done")
