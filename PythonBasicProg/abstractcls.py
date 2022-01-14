# Lecture 61, 62
from abc import ABC, abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("Running")      

comp1 = laptop()
#comp1.process()        

#Iterator
class topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <=5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

#values = topten()
#print(values.__next__())
#for i in values:
#    print(i)                        

#Generator
def topten():
    n=1
    while n<5:
        sq = n*n
        yield sq
        n = n+1

values =   topten()
for i in values:
    print(i)      