#공룡 장애물 피하기 게임
import pygame as p

p.init()#초기화

s=(600,300)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님의 요구")
g_y=0
sp=0
score=0
jump=False
bg=p.image.load("배경.jpg")
en=p.image.load("선인장.png")
f=p.font.SysFont("malgungothic",25)
f1=p.font.SysFont("malgungothic",50)


bg_re=bg.get_rect(left=0,top=0)
en_re=en.get_rect(left=550,top=200)

bg1=p.image.load("배경.jpg")

bg1_re=bg1.get_rect(left=600,top=0)


gong=p.image.load("go.png")
g_re=gong.get_rect(left=50,top=180)

playing = True
x=clock=p.time.Clock()
while playing:
    clock.tick(60)
    score+=1
    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if  event.type==p.KEYDOWN:
            if event.key==p.K_SPACE:
                if jump:
                    g_y=-18
                    jump=False
            
                
                

    sc.fill(white)
    sc.blit(bg,bg_re)
    sc.blit(bg1,bg1_re)
    sc.blit(gong,g_re)
    sc.blit(en,en_re)
    bg_re.left-=2
    en_re.left-=5+sp
    bg1_re.left-=2
    
    if bg_re.left<=-600:
        bg_re.left=600
    if bg1_re.left<=-600:
        bg1_re.left=600
    #중력만들기
    
    g_re.top +=g_y
    g_y+=1
    if g_re.top>=200:
        g_re.top=200
        jump=True
    if en_re.left<=-5:
        en_re.left=550
    if score%2000==0:
        sp+=1

        
    



    t=f.render("점수{}".format(score),True,(255,255,0))
    t1=f1.render("GAME OVER",True,(255,0,0))
    sc.blit(t,(450,0))
    




    if g_re.colliderect(en_re):
        sc.blit(t1,(150,100))
        playing=False
    p.display.flip()

            
            
    
