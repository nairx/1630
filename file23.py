# def add(*args): #args
#     print(sum(args))

# add(3,7,6)

def add(**kwargs): #keyword args
    sum=0
    for i,j in kwargs.items():
        sum=sum+j
    print(sum)

add(a=3,b=7,c=6,d=3,e=34)