def volume_sphere(r):
    '''input: r = Input in integer format
       output:return Vol of sphere upto two decimals'''
    # YOUR CODE GOES HERE
    
    Vol=None
    vol=round(((4*22/7*r**3)/3),2)
   
    return vol
r=int(input())
for i in range(1,r+1):
    volume_sphere(r)
spvolume=volume_sphere(r)
print(spvolume)