def lenghthofstring(line,length):
    list=[]
    for word in line.split():
        if len(word) == length:
            list.append(word)
    return list

line ="The world has changed and none of us can go back all we can do is our best and sometimes the best that we can do is to start over"
length=int(input("Enter the length of the word: "))
result = lenghthofstring(line, length)
print(f"The words with length {length} are: {result}")  

