class Student:
    def __init__(self, submarks1, submarks2, creditss1, creditss2):
        self.submarks1 = submarks1
        self.submarks2 = submarks2
        self.creditss1 = creditss1
        self.creditss2 = creditss2

    def subpoint1(self):
        if self.submarks1 >= 90:
            return 10
        if self.submarks1 < 90 and self.submarks1 >= 75:
            return 9
        if self.submarks1 > 75 and self.submarks1 >= 60:
            return 8
        if self.submarks1 < 60 and self.submarks1 >= 45:
            return 7    
        if self.submarks1 < 45 :
            return 0
    
    def subpoint2(self):
        if self.submarks2 >= 90:
            return 10
        if self.submarks2 < 90 and self.submarks2 >= 75:
            return 9
        if self.submarks2 > 75 and self.submarks2 >= 60:
            return 8
        if self.submarks2 < 60 and self.submarks2 >= 45:
            return 7    
        if self.submarks2 < 45 :
            return 0
        
    def gpa(self):
       
        if self.creditss1 == 0 and self.creditss2 == 0:
            return 0
        else:
            total_credits = self.creditss1 + self.creditss2
        return round((self.subpoint1() * self.creditss1 + self.subpoint2() * self.creditss2) / total_credits, 2)
    
student1 = Student(85, 76, 3, 4)
print(student1.gpa())