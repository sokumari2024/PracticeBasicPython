class Smaller:
    def __init__(self, a):
        self.string = a
    
    def  display(self):
        print("This is class smaller")
    
    def evaluate(self):
        self.count = 0
        for item in self.string:
            if item in "aeiouAEIOU":
                self.count=self.count+1
        print("Vowels:", self.count)
        return self.count
    
class Larger:
    def __init__(self, a):
        self.string = a
    
    def  display(self):
        print("This is class larger")
    
    def evaluate(self):
        self.count = 0
        for item in self.string:
            if item not in "aeiouAEIOU":
                self.count=self.count+1
        print("Consonants:", self.count)
        return self.count
    
a=input("Enter a string: ")
if len(a) < 6:
    s = Smaller(a)
    s.display()
    s.evaluate()
else:
    l = Larger(a)
    l.display()
    l.evaluate()