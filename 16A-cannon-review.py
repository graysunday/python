import turtle as t
import random as r

def start_position():
    t.goto(-150,10)
    t.setheading(20)
    
def turn_up():
    t.lt(2)

def turn_down():
    t.rt(2)

def fire():
    ang = t.heading()

    while t.ycor() > 0:
        t.fd(15)
        t.rt(5)

    d = t.distance(target,0)
    print(d)
    #t.sety(r.randint(10,100))
    t.goto(t.xcor(), r.randint(10,100))
    if d < 25:
        t.write("성공", False, "center", ("",10))
        atart_position()
    else:
        t.write("실패", False, "center", ("",10))
        start_position()


#바닥면 그리기
t.up()
t.goto(-200,0)
t.down()
t.goto(200,0)
t.up()

#target 그리기
t.color("green")
t.pensize(3)
target = r.randint(50,150)
t.goto(target-25,2)
t.down()
t.fd(50)
t.up()

#거북이 발사장소로 이동 후 위치 잡기
start_positioin()

#키보드 설정에 따른 각도잡기
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.listen()
