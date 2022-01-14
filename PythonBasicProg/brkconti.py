#break, continue, pass
#Print 1st 50 fibonacci numbers
a = 0
b = 1
i = 3
end = 5
print(a, " ", b, " ", end = " ")
while i<=end:
    c = a + b
    a = b
    b = c
    print(c, " ", end = " ")
    i = i + 1
print()


#check prime number or not
x = int(input("Enter a number: "))
i = 2
while i <= x-1:
    if(x % i == 0):
        print("Not Prime Number")
        break
    i = i + 1
if i == x:
    print("Prime Number")    
    
    