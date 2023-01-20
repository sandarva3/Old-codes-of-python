amount = int(input("How many numbers you want to sum :"))
a = 0
for i in range(amount+1):
    a[i] = int(input(f"Enter {i} number :"))
    b = a + a[i]
print(f"your total sum is {b} ")
