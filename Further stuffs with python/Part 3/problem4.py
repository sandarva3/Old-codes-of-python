a = int(input("Enter any number :"))
b =int(input("enter divinding number :"))
try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")