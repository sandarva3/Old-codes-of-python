a = int(input("Enter a number :"))
table = [i*a for i in range(1,11)]
print(str(table))

with open("Multiplication table.txt", "w") as f:
    f.write(str(table))
