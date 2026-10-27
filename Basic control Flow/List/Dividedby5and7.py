list=[23,34,25,35,66,70,14]
def dividedby5and7(list):
    newlist=[]
    for i in list:
        if i%5==0 and i%7==0:
            newlist.append(i)
    return newlist
print(dividedby5and7(list))
