#무작위 위치에서 터틀런으로 별 그리기
import turtle as t
import random as r

t.shape("turtle")
t.speed(0)

for x in range(5):
    a=r.randint(1,360)
    t.setheading(a)
    t.forward(10)




    

t.color("hot pink")
t.up()
t.goto(0,0)
t.down()
for x in range(5):
    a=r.randint(1,360)
    t.setheading(a)
    b=r.randint(1,20)
    t.forward(b)

t.color("hot pink")
t.up()
t.goto(0,0)
t.down()
for x in range(5):
    b=r.randint(1,20)
    t.color("hot pink")
    t.up()
    t.goto(r.randint(-300,300),r.randint(-200,200))
    t.down()
    for y in range(5):
        t.forward(100)
        t.left(144)
    

