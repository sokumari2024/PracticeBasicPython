a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=min(a,b)
list=[]
for i in range(c,0,-1):
    if a%i==0 and b%i==0:
        list.append(i)
print("The 2nd highest GCD of",a,"and",b,"is:",list[1])