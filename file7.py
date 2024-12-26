i=1
while i<=5:
    print("Hello")
    choice = input("Continue (y/n)?")
    i=i+1
    if choice=="y":
        continue
    else:
        break
else:
    print("Program Completed Successfully")