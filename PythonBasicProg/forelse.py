#Prime number or not
x = int(input("Enter a number: "))
b = int(x/2)
for i  in range(2,b+2):
    if(x % i == 0):
        print("Not Prime Number")
        break
else:
    print("Prime Number") 