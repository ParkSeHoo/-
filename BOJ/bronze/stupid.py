a,b =map(int,input().split())

a1 = a//100
a2 = (a%100)//10
a3 = a%10

stupid_a = a3*100+a2*10+a1

b1 = b//100
b2 = (b%100)//10
b3 = b%10

stupid_b = b3*100+b2*10+b1

if stupid_a>stupid_b:
    print(stupid_a)
else :
    print(stupid_b)