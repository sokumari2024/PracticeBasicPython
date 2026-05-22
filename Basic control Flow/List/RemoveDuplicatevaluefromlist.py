t=[1,2,1,3,4,1,2]
count=0
value=int(input("Enter the value to remove: "))
for i in t:
    if i==value:
        count+=1
print(f"The value {value} appears {count} times in the list.")
if count>1:
    for i in range(count):
        t.remove(value)
print(t)