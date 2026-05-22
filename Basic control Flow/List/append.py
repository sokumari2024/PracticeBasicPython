list=[10,20,30,40,50]
list.append(60) #appending new value at the end of the list
print(list)
list.insert(7,100)#
print(list)
print(list[3])#Get the 4th element of the list
print(list.index(30)) #Get the index of the element 30 in the list
list[1]=200 #Mutable:Change the value of the 2nd element to 200
print(list) 
Additionallist=[70,80,90]
list.extend(Additionallist) #extend the list by adding the elements of Additionallistto the end of the list
print(list)
Additionallist2=[70,80,90]
list.append(Additionallist2) #append the list at the end of the list
print(list)
print(list[10][0]) #Get the 8th element of the list  
print(list.count(70)) #Count the number of times 70 appears in the list
print(88 in list) #Check if 88 is present in the list--Membership operator
print(80 in list) #Check if 80 is present in the list