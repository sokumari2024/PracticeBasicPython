#This program calculates the percentage and grade based on the marks entered by the user

A=int(input("Enter the first number: "))
B=int(input("Enter the second number: "))
C=int(input("Enter the third number: "))
D=int(input("Enter the fourth number: "))
E = int(input("Enter the fifth number: "))
percentage = int((A+B+C+D+E)/5)
print("The percentage is: ", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80 and percentage < 90:
    print("Grade: B")
elif percentage >= 70 and percentage < 80:
    print("Grade: C")
elif percentage >= 60 and percentage < 70:
    print("Grade: D")
elif percentage >= 40 and percentage < 60:
    print("Grade: E")     
else:
    print("Grade: F") 