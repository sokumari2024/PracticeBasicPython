A=input("Enter a string: ").lower()
splitedA=list(A)
Counvowel=0
Counconsonant=0
print(splitedA)
for i in splitedA:
       if i in "aeiou":
            Counvowel+=1
       else:  
            Counconsonant+=1
print(f"Number of vowels: {Counvowel}")
print(f"Number of consonants: {Counconsonant}")