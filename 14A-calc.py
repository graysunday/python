import random

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)

    a = str(a)
    
    if op == 1:
        a = a + "+"

    if op == 2:
        a = a + "-"
        
    if op == 3:
        a = a + "*"
    
    a = a + str(b)

    return a

sc1 = 0
sc2 = 0
r = 5

for x in range(r):
    q = make_question()
    print(q)
    ans = input(" = ")
    
    #print("input = ",ans)
    
    if int(ans) == eval(q):
        sc1 = sc1 + 1
        print("정답")
    else:
        sc2 = sc2 +1
        print("오답")

print("정답 : ", sc1, " 오답 : ", sc2)
if sc1 >= r-1:
    print("당신은 천재입니다.!")
