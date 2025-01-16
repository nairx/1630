import logging
logging.basicConfig(filename='bank.log',level=logging.INFO,
                    format='%(asctime)s -  %(message)s')

balance=0
for i in range(3):
    am = int(input("Enter Deposit Amount :"))
    logging.info(f"{am} was deposited")
    balance = balance + am
    logging.info(f"The current balance is {balance}")
    print(balance)