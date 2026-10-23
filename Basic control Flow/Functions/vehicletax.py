def vehicletax(price):
    if price > 100000:
        tax = (price * 20) / 100
        #tax = round(tax,1)
    elif price >75000 and price <= 100000:
        tax = (price * 15) / 100
    elif price > 50000 and price <= 75000:
        tax = price * 10 / 100
    else:
        tax = price * 5 / 100
    return round(tax,1)

price = int(input("Enter the price of the vehicle: "))
tax = vehicletax(price)
print("The tax for the vehicle is:", tax)   