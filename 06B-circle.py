import turtle as t

n=50
t.bgcolor("black")
t.color("green")
t.speed(0)

for i in range(25):
    t.circle(80)
    t.left(360/n)

t.color("red")

for i in range(25):
    t.circle(80)
    t.left(360/n)
