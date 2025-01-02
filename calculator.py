import addition as a
import subtraction as b
import multiplication as c 
import division as d 

def calculator(n1,n2):
    add = a.addition(n1,n2)
    sub = b.subtraction(n1,n2)
    multi = c.multiplication(n1,n2)
    div = d.division(n1,n2)
    print(add,sub,multi,div)

