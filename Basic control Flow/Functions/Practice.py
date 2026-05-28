#items=["Book","Pen","NoteBook","BackPack","Pencil"]
#sale=[150,20,90,200,10]
#costs=[100,10,50,150,5]
from functools import reduce
items = []
sale = []
costs = []

threshold = int(input("Enter threshold amount: "))

for i in range(5):
    item = input("Enter the name of the item: ")
    items.append(item)

    saleprice = int(input("Enter the sale price of the item: "))  # convert to int
    sale.append(saleprice)

    costprice = int(input("Enter the cost price of the item: "))  # convert to int
    costs.append(costprice)

print("Items:", items)
print("Sales:", sale)
print("Costs:", costs)

# Zip all three together
ziplist = list(zip(items, sale, costs))

# Filter based on sale > threshold
filteredlist = list(filter(lambda x: x[1] > threshold, ziplist))

print("Filtered List (item, sale, cost):")
print(filteredlist)

profit=[]
for item, saleprice, costprice in ziplist:
    profit.append((item, saleprice - costprice))

print("Profit List (item, profit):")
print(profit)


profitAmount =reduce(lambda x, y: x + y, [p[1] for p in profit])

print(profitAmount)
