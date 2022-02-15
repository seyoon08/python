import pygame as p
import random as r
import time as t

p.init()

size = (800,400)
w = (255,255,255)
sc = p.display.set_mode(size)
p.display.set_caption("두더지 게임")
do_image = p.image.load("q.png") 
do_list = []
for i in range(5): 
    do = do_image.get_rect(left=r.randint(0,750),top = r.randint(0,350))
    do_list.append(do)
playing = True
clock = p.time.Clock()

font = p.font.SysFont('malgungothic',20)
score = 0

t1=int(t.time())


p.mixer.init()
hit=p.mixer.Sound("야.wav")
 


while playing:

    clock.tick(60)

    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit
        if event.type == p.MOUSEBUTTONDOWN: #1.마우스를 클릭했을때
            for do in do_list: 
                if do.collidepoint(event.pos):#2. 두더지들을 클릭하게되면
                    
                    score= score+1
                    do_list.remove(do) #3.리스트에 있는 두더지 삭제
                    do = do_image.get_rect(left=r.randint(0,700),top = r.randint(0,300)) #4.두더지 재배치
                    do_list.append(do)#5.리스트에 추가
                    hit.play()
            
    sc.fill(w)
    for do in do_list: 
        sc.blit(do_image,do)

    text = font.render("점수: {}".format(score),True,(0,0,0))
    sc.blit(text,(300,0))
    t2=int(t.time())
    ti=60 - (t2-t1)
    text1 = font.render("남은 시간: {}".format(ti),True,(0,0,0))
    if ti==0 :
        playing=False
    sc.blit(text1,(650,0))
    p.display.flip()

    
