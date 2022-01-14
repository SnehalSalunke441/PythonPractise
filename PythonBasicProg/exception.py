#Lecture 63, 64

'''
a = 3
b = 0
try:
    print("Resource open")
    print(a/b)
except Exception as e:    
    print("Something went wrong...: ",e)

except ValueError as e:    
    print("Invalid input: ",e)

except ZeroDivisionError as e:    
    print("Cannot divide by zero: ",e)    
finally:
    print("Resource closed")

print("Bye")
'''

# Multithreading
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(3):
            print("Hello")
            sleep(0.5)

class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hii")
            sleep(0.5)

c1 = Hello()
c2 = Hi()
c1.start()   #used to call run method/any method using thread
sleep(0.2)   #if removed may cause collision
c2.start()
c1.join()    #asking main thread to wait for c1 and c2 threads
c2.join()
print("Bye")
