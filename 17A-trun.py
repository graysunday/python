import turtle as t
import random as r

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def play():
    t.fd(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.fd(9)
    if t.distance(ts) < 12:
        start_x = r.randint(-230, 230)
        start_y = r.randint(-230, 230)
        ts.goto(start_x,start_y)
    if t.distance(ts) >= 12:
        t.ontimer(play, 100)

te = t.Turtle() #악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle() #먹이
ts.shape("circle")
te.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

t.setup(500,500) #거북이
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

#거북이 방향조절
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()
