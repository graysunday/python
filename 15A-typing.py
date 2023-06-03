import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

print("준비가 되면 [Enter]를 누르세요.")
input()
ts = time.time()
n = 1
good = 5

while n <= good:
    
    a = random.choice(w)
    print(a)
    b = input()

    if a == b:
        print("통과 - ",n, "/", good)
        n = n+1
    else:
        print("오타! 다시도전")

te = time.time()
te = format(te-ts, ".2f")
print("통과!!")
print("문제풀기 걸린시간 : ", te)
