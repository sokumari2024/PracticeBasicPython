N=int(input())
list=[]
for i in range(N):
    element=int(input())
    list.append(element)
print(list)
for i in range(len(list)-1, 0, -1):
    print(list[i],end=" ")
