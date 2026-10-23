def vowel(A):
    if A in ['a','i','o','u','e','A','I','O','U','E']:
        print(A,"is a vowel")
        return 1
    else:
        print(A,"is not a vowel")
        return 0

isvowelornot=vowel(input("Enter a character:"))
print("Return value of the function is:",isvowelornot)
