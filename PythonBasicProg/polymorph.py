#Lecture 57, 58,59,60

class Laptop:
    def code(self, ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print("Compiling in pycharm")        

class Myeditor:
    def execute(self):
        print("Compiling in pycharm") 
        print("Convention check")
        print("Executing code")       

#ide = Pycharm()
ide = Myeditor()  #must have method called execute(), similar to execute in Pycharm
lap1 = Laptop()
#lap1.code(ide)

#print(int.__add__(3,5))
#Operator overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __sub__(self, s2):
        m1 = self.m1 - s2.m1
        m2 = self.m2 - s2.m2
        m3 = Student(m1, m2)
        return m3 
    
    def sum(self, a = None, b = None, c = None):
        s = 0
        if a!= None and b != None and c!=None:
            s = a+b+c 
        elif a!=None and b!=None:
            s = a+b 
        else:
            s = a 
        return s 



s1 = Student(98,95)
#s2 = Student(90, 85)
#s3 = s1 - s2
#print("Student 3: subject1:{} subject2: {}".format(s3.m1, s3.m2))

#ans = s1.sum(10,1,9)  #s1.sum(10,9)  #s1.sum(10)
#print(ans)

# Method Overiding
class A:
    def show(self):
        print("In show of A")

class B(A):
    pass
    #def show(self):
    #    print("In show of B")

b1 = B()
b1.show()                
