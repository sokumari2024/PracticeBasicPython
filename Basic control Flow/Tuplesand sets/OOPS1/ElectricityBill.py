class Bill:
    Meter_Charges = 150
    def __init__(self, previous_read,current_read):
        
    
        self.previous_read = previous_read
        self.current_read = current_read

    def total_bill(self):
       
        self.units_consumed = self.current_read - self.previous_read
        if self.units_consumed <= 100:
            return self.Meter_Charges+self.units_consumed * 3.5
        elif self.units_consumed <= 200:
            return self.Meter_Charges + (100 * 3.5) + ((self.units_consumed - 100) * 5)
        else:
            return self.Meter_Charges + (100 * 3.5) + (100 * 5) + ((self.units_consumed - 200) * 8)
        
b=Bill(200,650)
print(b.total_bill())