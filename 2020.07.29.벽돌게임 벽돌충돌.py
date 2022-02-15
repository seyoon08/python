import pygame as p

p.init()#초기화

s=(600,900)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님이 폭력을 휘둘러 만든 벽돌게임")
b=p.image.load("block.png")
chell=p.image.load("칠판.png")
b_re=b.get_rect(left=250,top=800)
ba=p.image.load("ball.png")
pan=p.image.load("벽돌.png")
pen_li=[]
for x in range(10):
    for y in range(10):
        p_re= pan.get_rect(left=60*x,top=40*y)
        pen_li.append(p_re)
ba_re=ba.get_rect(left=280,top=430)
x=0
bax=5
bay=5


font=p.font.SysFont('malgungotic',50)

playing = True

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_RIGHT:
                x=10
            if event.key == p.K_LEFT:
                x=-10
        if event.type == p.KEYUP:
            if event.key == p.K_RIGHT:
                x=0
            if event.key == p.K_LEFT:
                x=0

    b_re.left +=x
    sc.fill(white)
    sc.blit(chell,(0,0))
    sc.blit(b,(b_re))
    sc.blit(ba,(ba_re))
    if b_re.left<=0:
        b_re.left=0
    if b_re.left>=500:
        b_re.left=500
    ba_re.top+=bay
    ba_re.left+=bax
    if ba_re.top>=880:
        print("선생님이 폭력을 휘둘러 만든 벽돌게임 오버")
        sc.blit(te,(200,400))
        playing=False
        pass
    if ba_re.top<=0:
        bay=5
    if ba_re.left>=580:
        bax=-5
    if ba_re.left<=0:
        bax=5
    
    te=font.render("GAME OVER",True,(63,74,54))
    
    if b_re.colliderect(ba_re):
        bay=-bay
    for p_re in pen_li:
        sc.blit(pan,p_re)
    for p_re in pen_li:
        if ba_re.colliderect(p_re):
            pen_li.remove(p_re)
            bay=5
    p.display.flip()
