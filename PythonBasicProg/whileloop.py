#while loop demo
x = int(input("Enter any number: "))
while x>0:
    print("Snehal and Vitthal", end = " ")
    n= 4
    while(n>0):
        print("hungry ", end = " ")
        n = n-1
    x = x-1
    print()

# write a code to print no. from 1 to 100, skip numbers divisible by 3 or 5
i = 1
while i<=100:
    if i%3==0 or i%5 == 0 :
        i = i + 1
        continue
    else: 
        print(i, " ", end =" ")
    i = i + 1    

print() 
print()

#write a code to print a pattern of matrix of # (5 *5)
i = 5

while i>0:
    j = 5
    while j>0:
        print("# ", end = " ")
        j = j - 1
    i = i - 1
    print()      


