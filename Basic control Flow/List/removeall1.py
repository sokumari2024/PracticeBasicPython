List=[1,2,3,1,4,5,1,6,7,1,9,10]
def removeall(List):
    for i in List:
        if i==1:
            List.remove(i)
    return List
print(removeall(List))
