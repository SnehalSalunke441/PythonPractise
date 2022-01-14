# Lectures 49,50,51,52

'''
class Computer:
    def config(self):
        print(" i5, 16gb, 1TB")

comp1 =  Computer()
print(type(comp1))
comp1.config()        
'''

class Computer:
    hardware = "Computer System"    #class variable

    def __init__(self, cpu, ram, age):
        self.cpu = cpu    #instance variables
        self.ram = ram
        self.age = age

    def config(self):
        print("Configuration is CPU {}, RAM {}".format(self.cpu, self.ram))

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False    


comp1 = Computer("i5", 16, 9)
comp2 = Computer("Ryzen3", 8, 9)
#comp1.config()
#comp2.config()

if comp1.compare(comp2):
    print("Same age")
else:
    print("Different age")    

print(Computer.hardware, comp1.age)
comp1.age = 12 #way to change instance variable
Computer.hardware = "Laptop"
print("After Changng values: ", Computer.hardware, comp1.age)