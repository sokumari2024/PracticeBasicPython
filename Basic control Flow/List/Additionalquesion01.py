N=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(N):
    element=int(input("Enter an element: "))
    list.append(element)
print("The list is:",list)
x=int(input("Enter X position where Y has to be insertedin the list: "))
y=int(input("Enter Y value to be inserted in the list: "))
list.insert(x-1,y)
print("The list after inserting Y at X position is:",list)