def game():
    print("Guess any number between 1 to 10")
    ask2 = input("Have you guessed, Enter 'y' after guessing :")
    if ask2 == "y":
        print("Now, add 10 to that number")
        ask3 = input("Did you add ? Enter 'y' After doing so, :")
        if ask3 == "y":
            print("Now subtract 6 ")
            ask4 = input("Enter 'y' after you doint it :")
            if ask4 == "y":
                print(
                    "Now, subtract the original number that you guessed on this number ")
                ask5 = input("Enter 'y' after doing so :")
                if ask5 == "y":
                    print("The number you have now is 4")


print("lets play a game")

ask = input("Enter 'y' if you want to and 'n' if you don't : ")
if ask == "y":
    game()
    while True:
        input1 = input("Do you want to play the game again ? Enter 'y' for yes and 'n' for no :")
        if input1 == 'y':
            game()
        elif input1 == 'n':
            print("Hope you enjoyed the game")
            break
elif ask == "n":
   print(":(...You should've played it !")
   print("Bye !")
elif ask != 'y' or ask!= 'n': 
   print("Invalid input")
   while True:
    input1 = input("Enter 'y' if you want to and 'n' if you don't : ")
    if input1 == 'y':
        game()
    else:
        print("Bye")
        break

