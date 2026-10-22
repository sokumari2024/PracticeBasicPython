N=int(input("Enter a number: "))
for i in range(1,N+1):
    if i%4==0:
        print(i,end=" ")
        i=i+4