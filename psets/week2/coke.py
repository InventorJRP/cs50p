due = 50

while due > 0:
    print("Amount due:", due)

    while True:
        amount = int((input("insert coins: ")))
        if amount == 5 or amount == 10 or amount == 25:
            due -= amount
            break
        else:
            print("Invalid! only insert 5, 10, or 25")

if due < 0:
    print("Change owed:", abs(due))
else:
    print("Amount due:", due)

#Working build