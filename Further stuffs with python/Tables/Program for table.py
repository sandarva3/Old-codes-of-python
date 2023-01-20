for i in range(1,21):
    with open(f"This is the table of {i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                print("\n")

