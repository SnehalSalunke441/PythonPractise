# pattern of #(4,4)
#a = 4
#while a>=1:
#    b = 4
#    while b>=1:
#        print("#", end = " ")
#        b = b - 1
#    a = a - 1 
#    print()
#print()

# pattern of # (4,3,2,1)
#a = 4
#while a>=1:
#    b = a
#    while b>=1:
#        print("#", end = " ")
#        b = b - 1
#    a = a - 1 
#    print()
#print()

# pattern of #(1, 2,3,4)
#a = 1
#while a<=4:
#    b = 1
#    while b<=a:
#        print("#", end = " ")
#        b = b + 1
#    a = a + 1 
#    print()
#print()

# pattern {1 2 3 4; 2 3 4; 3 4; 4}
for i in range(4):
    p = i+1 
    for j in range(4-i):
        print(p, end = " ")
        p+=1
    print()    
print()
# pattern {A P Q R; A B Q R; A B C R; A B C D}
str1 = "ABCD"
str2 = "PQR"
for i in range(4):
    print(str1[:i+1] + str2[i:])
