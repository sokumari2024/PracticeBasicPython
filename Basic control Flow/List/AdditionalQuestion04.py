N=int(input())
A=[]
for i in range(N):
    element=int(input())
    A.append(element)
print(A)
for j in A:
    if j<0:
        print(j,end=" ")
