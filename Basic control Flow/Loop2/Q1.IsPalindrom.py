T=int(input("Enter the number of test cases: "))
originalnum=int(input())
for i in range(1, T+1):
    N=originalnum
    reversnum=0
    while N>0:
      
        digit=N%10 #getting the last digit
        reversnum=reversnum*10+digit #reversing the number
        N=N//10 #removing the last digit
    print(reversnum)
print("The original number is:", originalnum)
if originalnum==reversnum:
    print("The number is a palindrome.")
else:    print("The number is not a palindrome.")

    