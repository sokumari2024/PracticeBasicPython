C=int(input("Enter Cost price: "))
S=int(input("Enter Selling price: "))

if S>C:
    print("1")
    print("Profit:",S-C)

else:
    print("-1")
    print("Loss:",C-S)