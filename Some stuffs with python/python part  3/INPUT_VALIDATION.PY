while True:
    try:
        age = int(input("Enter your age :"))
        if age < 1:
            print("Please enter your valid age")
        if age >= 1:
            print(f"your age is {age} ")
            break
    except:
        print("Please enter number")
    