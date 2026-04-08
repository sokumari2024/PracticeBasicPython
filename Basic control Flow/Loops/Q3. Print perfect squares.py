import math
N=int(input("Enter a number: "))
for i in range(1, N+1):
    sq=int(math.sqrt(i))
    if sq*sq==i:
        print(i, end=" ")