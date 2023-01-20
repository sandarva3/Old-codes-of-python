import random
randnumber = random.randint(1, 10)
input1 = int(input("How many times you want to guess the number :"))
for i in range(input1):
    input2 = int(input("Guess the number :"))
    try:
        if input2 > randnumber:
            print("Your guess is higher than correct number")
        elif input2 < randnumber:
            print("Your guess is lower than correct number")
        elif input2 == randnumber:
            print("You guessed correct number ")
            print("Congratulations ")
            break
    except:
        print("Invalid input")

if (i+1) == 1:
    n = "st"
elif (i+1) == 2:
    n = "nd"
elif (i+1) == 3:
    n = "rd"
elif (i+1) == 0:
    n = ""
else:
    n = "th"
if input2 == randnumber:
    print(f"*** You guessed the number in {i+1}{n} guess ***")
elif input2 != randnumber:
    print("You did not guessed the number ")
with open("hiscore.txt", "w") as f:
    f.write("55")
with open("hiscore.txt", "r") as f:
    a = int(f.read())
if a > (i+1):
    with open("hiscore.txt", "w") as f:
        b = i+1
        f.write(str(b))
