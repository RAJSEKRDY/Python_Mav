
number = int(input("Enter an integer: "))

for i in range(1, number+1):
    if i % 5 == 0:
        print("Fuzz")
    else:
        print(i)
