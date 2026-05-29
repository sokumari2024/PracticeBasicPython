list1=['ccc', 'bb', 'dd', 'aaa', 'bB']
sortedlist=sorted(list1, key=lambda x: (len(x), x))
print(sortedlist)
