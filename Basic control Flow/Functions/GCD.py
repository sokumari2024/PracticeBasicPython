a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))   
x=min(a,b)
for i in range(x,0,-1):
    if a%i==0 and b%i==0:
        print("The GCD of",a,"and",b,"is",i)
        break

    