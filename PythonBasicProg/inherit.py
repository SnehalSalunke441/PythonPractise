#Lecture 55, 56

class A:
    def __init__(self):
        print("Init of class A")

    def fun1(self):
        print("I am in fun1 of class A")

class B():
    def __init__(self):
        print("Init of class B")

    def fun2(self):
        print("I am in fun2 of class B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Init of class c")

    def fun3(self):
        super().fun1()
        print("I am in fun3 of class C")

c1 = C()        
#c1.fun1()
#c1.fun2()
#c1.fun3()