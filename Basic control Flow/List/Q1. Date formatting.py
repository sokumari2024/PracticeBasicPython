from datetime import datetime
A=input("Enter a date in the format DD/MM/YYYY: ")
date_obj1 = datetime.strptime(A, "%d/%m/%Y")
formatted_date1 = date_obj1.strftime("%m/%d/%Y")
formatted_date2 = date_obj1.strftime("%Y/%m/%d")

print(f"The formatted date is: {formatted_date1}")
print(f"The formatted date is: {formatted_date2}")