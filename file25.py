print("*** Calculator ***")

def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def calculator(n1,n2):
    a=addition(n1,n2)
    s=subtraction(n1,n2)
    m=multiplication(n1,n2)
    d=division(n1,n2)
    print(f"{a}-{s}-{m}-{d}")

calculator(10,2)