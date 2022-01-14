#Lecture 53, 54

class Student:
    school = "RJ TVM"

    '''
    def instancemethod(self, name):
        self.name = name
        print("Name of student: ", self.name)

    @classmethod
    def info(cls):
        print("School name: ", cls.school)

    @staticmethod
    def infocs():
        print("This is static method")
     
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()   #Object of inner class inside outer class

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8 GB"

#lap1 = Student.Laptop()
#print(lap1.brand)
s1 = Student("Sita", 21)
print(s1.name, s1.age, s1.lap.brand)

#s1 = Student()
#s1.instancemethod("Manish")
#s1.info()
#Student.infocs()            