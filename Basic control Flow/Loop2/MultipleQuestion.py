N=int(input("Enter a number: "))

for i in range(1, N+1):
    for j in range(1, 11):
        #print( i,"*",j,":",i*j, end="\n ") 
        print( i*j, end=" ") 

    print("\n", end="") 