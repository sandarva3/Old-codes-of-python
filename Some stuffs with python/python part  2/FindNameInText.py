def name(text):
    if text == "sandarva paudel":
        return True
    else:
        return False
message = input("Enter a text :")
message = message.lower()
for i in range(len(message)):
    chunk = message[i:i+15]
    if name(chunk) == True:
        print(f"Name is found: {chunk}")
        print("Done")



