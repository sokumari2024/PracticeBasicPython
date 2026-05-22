runs=[62,85,74,10,12,101,122,99,81,102,110]
result=[]
for i in runs:
    if runs.index(i)%2==0:
        result.append(i)
print(result)