N=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(N):
    element=int(input("Enter an element: "))
    list.append(element)
print("The list is:",list)
list.reverse()
print("The list in reverse order is:",list,end=" ")
