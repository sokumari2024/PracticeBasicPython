N=int(input("Enter a number: "))
for i in range(1, N+1):
    for j in range(1, i+1):
        print("*", end=" ")
    #N= N-1
    print("\n", end="")
    