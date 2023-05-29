
num_calls = int(input("Enter the number of calls: "))

if num_calls <= 100:
    monthly_bill = 200
elif num_calls <= 150:
    monthly_bill = 200 + 0.60 * (num_calls - 100)
elif num_calls <= 200:
    monthly_bill = 200 + 0.60 * 50 + 0.50 * (num_calls - 150)
else:
    monthly_bill = 200 + 0.60 * 50 + 0.50 * 50 + 0.40 * (num_calls - 200)

print("Monthly telephone bill: Rs.", monthly_bill)