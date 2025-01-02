# import addition
# import addition as add
# from addition import *
from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
print("*** Calculator ***")

def calculator(n1,n2):
    a=addition(n1,n2)
    s=subtraction(n1,n2)
    m=multiplication(n1,n2)
    d=division(n1,n2)
    print(f"{a}-{s}-{m}-{d}")

calculator(10,2)