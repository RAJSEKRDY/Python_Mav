
log = input("Enter transaction log: ")
transactions = log.split()

balance = 0

for transaction in transactions:
    if transaction[0] == 'D':
        balance += int(transaction[2:])
    elif transaction[0] == 'W':
        balance -= int(transaction[2:])

print("Net amount:", balance)