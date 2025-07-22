# Create a class and with 5 object and modify each object using method
class mobile:
    brand = "Sumsung"
    def __init__(self,camera,color,storage,ram):
        self.screen = camera
        self.color = color
        self.storage = storage
        self.ram = ram
    def updating_features(self,value):
        self.storage = value
m1 = mobile("16mp","black","64gb","4gb")    
print(m1.ram)      
m1.updating_features("256gb")
print(m1.storage)  

m2 = mobile("32mp","blue", "128gb","6gb")
print(m2.color)
m2.updating_features("4gb")
print(m2.ram)

m3= mobile("50mp","skyblue", "256gb","8gb")
print(m3.screen)
m3.updating_features("orange")
print(m3.color) 

m4 = mobile("40mp","green","128gb","4gb")
print(m4.screen)
m4.updating_features("8gb")
print(m4.ram)

m5 = mobile("60mp","purple","256gb","16gb")
print(m5.screen)
m5.updating_features("64gb")
print(m5.storage)