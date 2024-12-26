print("*** HDFC Bank ***")
balance=0
while True:
    print("1. Deposit")
    print("2. withdraw")
    print("3. Exit")
    ch=input("Enter your choice:")
    if ch=="1":
        amount = int(input("Enter Amount: "))
        balance=balance+amount
        print("Current balance is ",balance)
    elif ch=="2":
        amount = int(input("Enter Amount: "))
        if balance < amount:
            print("Insufficient Fund")
        else:
            balance = balance - amount
        print("Current balance is ",balance)
    else:
        break