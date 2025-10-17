

def fib(n):
    b=1
    a=0
    
    if(n==1):
        print(a)
    elif(n==2):
        print(a)
        print(b)
    else:
        print(a)
        print(b)

        
        for i in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c



n=int(input("enter a number"))
fib(n)
            
            
