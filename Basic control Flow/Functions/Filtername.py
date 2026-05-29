ids = ["SAM@gmail.com", "Ram@gmail.com", "sam@gmail.com", "samJohnson@iit.com", "SAM@harvard.com"]
name = "sam"
result = list(filter(lambda x : name in x.lower() , ids))
print(result)