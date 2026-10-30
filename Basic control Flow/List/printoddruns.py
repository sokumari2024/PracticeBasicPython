list=[1,2,3,4,5,6,7,8,9,10,]
oddnumbers=[]
for index,items in enumerate(list):
    if index%2==0:
        oddnumbers.append(items)
print("The odd numbers are:", oddnumbers)
