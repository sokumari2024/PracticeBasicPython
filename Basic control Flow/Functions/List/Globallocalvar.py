x=50
def sum():
    global x
    print("The value of x is",x) #50
    x=100
    sum=0
    sum=sum+x 
    print("The sum is",sum) #100
sum()
print("The value of x is",x) #50