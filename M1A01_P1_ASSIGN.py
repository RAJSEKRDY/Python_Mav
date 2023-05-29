number = int(input("Enter an integer: "))

for i in range(1, number+1):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
