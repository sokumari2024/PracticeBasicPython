A=[7,9,2,51]

def arrayproduct(A):
    product=1
    for item in A:
        product=product*item
    return product
print("The product of the elements in the array is:", arrayproduct(A))
arrayproduct(A)