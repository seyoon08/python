#슈팅게임2(3(적군 점수))
import pygame as p
import random as r
p.init()#초기화

s=(600,800)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("적들아,나와라")
ship=p.image.load("u.png")
ship_le=ship.get_rect(left=250,top=700)
bg=p.image.load("o.png")
b=p.image.load("b.png")
en=p.image.load("0.png")
en_li=[]
b_lest=[]
for x in range(1,50):
        en_re=en.get_rect(left=r.randint(0,500),top=0)
        en_li.append(en_re)

x=0
y=0
playing = True
score=0
font=p.font.SysFont("malgungothic",20)

while playing:
        b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
        b_lest.append(b_le)
        for event in p.event.get():
            if event.type == p.QUIT:
                playing =False
                p.quit()
                quit()
            if event.type == p.KEYDOWN:
                if event.key ==p.K_UP:
                    y=-10
                if event.key ==p.K_DOWN:
                    y=10
                if event.key ==p.K_RIGHT:
                    x=10
                if event.key ==p.K_LEFT:
                    x=-10
        if event.type == p.KEYUP:
             if event.key ==p.K_UP:
                y=0
             if event.key ==p.K_DOWN:
                y=0
             if event.key ==p.K_RIGHT:
                x=0
             if event.key ==p.K_LEFT:
                x=0


            
        ship_le.top += y
        ship_le.left += x
        sc.fill(white)
        
        
        sc.blit(bg,(0,0))
        for b_le in b_lest:
            sc.blit(b,b_le)
        for b_le in b_lest:
            b_le.top -= 50
            if b_le.top<=0:
                b_lest.remove(b_le)
        for en_re in en_li:
                sc.blit(en,en_re)
        for en_re in en_li:
                en_re.top +=5
                if en_re.top>=700:
                        en_li.remove(en_re)
                        score=score-1
                        en_re=en.get_rect(left=r.randint(0,500),top=0)
                        en_li.append(en_re)
   
        for en_re in en_li:
                for b_le in b_lest:
                        if b_le.colliderect(en_re):
                                b_lest.remove(b_le)
                                en_li.remove(en_re)
                                score=score+1
                                en_re=en.get_rect(left=r.randint(0,500),top=0)
                                en_li.append(en_re)
        sc.blit(ship,ship_le)
        t=font.render("점수:{}".format(score),True,(255,255,255))
        sc.blit(t,(10,10))
        p.display.flip()



    
