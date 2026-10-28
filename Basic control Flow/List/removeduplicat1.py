list=[1,2,3,1,4,5,1,6,7,1,9,10]
counter=list.count(1)
print("The number of times 1 appears in the list is:", counter)
def removeduplicates(list):
    for i in list:
        if list.count(i)>1:
            while list.count(i)>1:
                list.remove(i)
    return list
print(removeduplicates(list))