# ATM Cash Dispenser
print("=== ATM Cash Dispenser ===\n")
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter withdraw amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing {amount} units for {name}:")
    remaing = amount
    idx = 1
    while idx <=6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx ==3: vlue = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            



