

import turtle as t
import random

score = 0
playing = False

te = t.Turtle()
te.shape("turtle")
te.color("hot pink")
te.pensize(3)
te.up()
te.goto(0,200)
te.down()

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.up()
ts.goto(0,-200)

t.title("Turtle Run")
t.shape("turtle")
t.color("sky blue")
t.pensize(3)
t.up()
t.bgcolor("yellow")
t.down()

def turn_rt():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_lt():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing =True
        t.clear()
        play()
def play():
    global score
    global playing
    ang = te.towards (t.pos())
    te.setheading(ang)
    
    t.forward(10)
    te.forward(8) 
    if t.distance(ts) < 12 :
        score = score + 1
        t.write
        y = random.randint(-500,500)
        x = random.randint(-950,950)
        ts.goto(x,y)
    if t.distance(te) < 12 :
        ta = "Score:" + str (score)
        ma("GAME OVER",ta)
        playing = False
        score = 0
    if playing:
        t.ontimer(play,100)
        

def ma(m1,m2):
    t.clear
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)  #거북이위치를 처음으로
    t.write(m2,False,"center",("",20))
    t.home() 

        
t.onkeypress(turn_rt,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_lt,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")
t.listen()
#start()

