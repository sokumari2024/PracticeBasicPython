A=[1,0,0,1,1,1,0,0,1,0,1]
B=[0,0,1,1,0,1,1,1,0,0,0,0]
def comparelistvalues(A,B):
    for i in range(len(A)):
        if A[i] == B[i]:
            return True
        else:
            return False
print(comparelistvalues(A,B))
newcomparelist=list(map(lambda x,y: True if x==y else False, A,B))
print(newcomparelist)
intnewcomparelist=list(map(lambda x,y: int( x==y), A,B))
print(intnewcomparelist)