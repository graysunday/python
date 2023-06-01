import random as r

a = r.randint(1,30)
b = r.randint(1,30)

print(a,"+",b,"=")
x = input()
c = int(x)

if c == a+b:
    print("천재!")
else:
    print("바보?")
