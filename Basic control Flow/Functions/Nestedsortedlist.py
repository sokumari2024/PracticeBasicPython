def sort_strings(str_list):
    sortedlist=[]
    for items in str_list:
        result=sorted(items, key=lambda x: (x.count('a'),len(x),x), reverse=True)
        sortedlist.append(result)
    print(sortedlist)
    
    #print(sortedlist)
    return sortedlist


str_list=[['mango', 'banana', 'guava'],['rose', 'sandalwood'],['bccc', 'aaa','baac', 'c']]
sort_strings(str_list)