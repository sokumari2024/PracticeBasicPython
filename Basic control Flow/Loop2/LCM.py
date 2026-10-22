a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=max(a,b)
#fact=1
while True:
    if c%a==0 and c%b==0:
        print("The LCM of",a,"and",b,"is:",c)
        break
    c += 1
