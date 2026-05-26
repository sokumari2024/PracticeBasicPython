class MachineLearning:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        
    def getname(self):
        return self.name
        
    def getcategory(self):
        return self.category
        
    def print(self):
        print("Name:",self.name)
        print("Category:",self.category)

class Supervised(MachineLearning):
    def __init__(self,name,category):
        #YOUR CODE GOES HERE
        super().__init__(name, category)
    def type(self):
        #YOUR CODE GOES HERE
        print("This is a supervised learning algorithm.")
    
class Unsupervised(MachineLearning):
    pass
        


obj1=Supervised(a,b)
obj1.type()
obj2=Unsupervised(c,d)
obj2.type()

