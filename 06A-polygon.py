import turtle as t

n=5;
t.color("purple")
t.begin_fill()
for i in range(n):
    t.fd(50)
    t.left(360/n)
t.end_fill()
