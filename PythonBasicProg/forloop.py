x = ["snehal", "Vitthal", "Dattatray" , "Vandana"]
p = "I Love INDIA"

for i in p:
    print(i, " ", end=" ")
print()

for i in range(21, 15, -1):
    print(i, " ", end=" ")
print()

#Print all perfect squares between 1 and 50
a = 1
sqr = a*a
while sqr<=1000:
    print(sqr, end= " ")
    a = a+1
    sqr = a * a
