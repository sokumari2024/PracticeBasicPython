def square_add(n):
    sum=0
    sum=n*(n+1)*(2*n+1)/6
    return sum

n=int(input("Enter a number: "))
result=square_add(n)
print("The sum of squares of the first", n, "natural numbers is:", int(result))