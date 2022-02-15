#골프게임
import turtle as t
import random as r
t.shape("turtle")

def turn_up():  #키보드 화살표 up을 눌렀을때
    t.lt(1)

def turn_down():   
    t.rt(1)

def fire(): #스페이스누르면 발사
    a = t.heading()      #거북이가 바라보는 각도 저장
    while t.ycor() > 0:  #거북이의 y좌표 ycor
        t.forward(15)
        t.rt(1)



    #while 이 빠지면 스탑

    d = t.distance(ta,0)   #거북이와 목표지점과의 거리
    t.sety(r.randint(300,400))  #글자표시 영역

    if d <= 714 and d >= 696:
        t.color("blue")
        t.write("good",False,"center",("",15))
    else:
        t.color("red")
        t.write("bed",False,"center",("",15))

    t.goto(-900,10)
    t.color("black")
    t.setheading(a)

    
t.goto(-950,0)  #땅그리는 부분
t.down()
t.goto(950,0)

ta= r.randint(50,150) #목표지점 설정
t.pensize(10)
t.color("green")
t.up()
t.goto (ta+700,2)
t.down()
t.goto(ta+710,2)

t.color("black")
t.up()
t.goto (ta-900,2)
t.setheading(20)

t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")

t.listen()


