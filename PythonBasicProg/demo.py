number = input()
nu = int(number)
en = 0
while(en!=1):
    p = 0
    num = nu
    while(num!=0):
        a =num%10
        num = num//10
        p = p *10 +a 
    if(nu==p):
        print(nu)
        en =1
        break
    else:
        num = nu + p
        nu = num

        