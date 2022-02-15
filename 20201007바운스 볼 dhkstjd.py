import pygame as p#파이게임생성

p.init()  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (800,600)    #가로,세로

sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("선생님이 욕을해서 만든 게임")    #게임창제목 display:해상도설정

playing = True
#공 이미지 생성
b=p.image.load("12.png")
st=p.image.load("star.png")
st_re=st.get_rect(left=0,top=80)
st2=p.image.load("star.png")
st_re2=st.get_rect(left=220,top=120)
pan=p.image.load("box.png")
p_re=pan.get_rect(left=0,top=500)
p_re1=pan.get_rect(left=50,top=500)
p_re2=pan.get_rect(left=100,top=500)
p_re3=pan.get_rect(left=150,top=500)
p_re4=pan.get_rect(left=200,top=500)
p_re5=pan.get_rect(left=250,top=500)
p_re6=pan.get_rect(left=300,top=500)
p_re7=pan.get_rect(left=400,top=450)
p_re8=pan.get_rect(left=500,top=300)
p_re9=pan.get_rect(left=550,top=300)
p_re10=pan.get_rect(left=600,top=300)
p_re11=pan.get_rect(left=0,top=100)
p_re12=pan.get_rect(left=50,top=100)
p_re13=pan.get_rect(left=100,top=100)
p_re14=pan.get_rect(left=150,top=100)
p_re15=pan.get_rect(left=200,top=100)
p_re16=pan.get_rect(left=250,top=100)
p_re17=pan.get_rect(left=300,top=100)
p_re18=pan.get_rect(left=370,top=100)

clear=False
clear2=False
bg3=p.image.load("bg3.png")
#공 좌표 
b_re=b.get_rect(left=0,top=285)
font=p.font.SysFont("malgungotic",50)
#화면 속도
fps=p.time.Clock()
#고 위치변수
y=0
x=0

e1=True
e2=True


while playing: #while True - 계속 반복하기
    fps.tick(50)#초당보여지는 사진갯수 
    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료

        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                x-=5
            if event.key==p.K_RIGHT:
                x+=5
            
        if event.type==p.KEYUP:
            if event.key==p.K_LEFT:
                x=0
            if event.key==p.K_RIGHT:
                x=0
        
    sc.fill(white)  #배경화면색 설정
    sc.blit(bg3,(0,0))
    sc.blit(b,b_re)
    #공튀코
    b_re.left+=x
    b_re.top+=y
    y+=2
    
    
    text=font.render('CLEAR',True,(0,103,0))
    #공이 바닥에 닿으면 
    if b_re.top>=650:
        b_re.left = 0
        b_re.top = 285
    if b_re.left>770:
        b_re.left=770
    if b_re.left<0:
        b_re.left=0
    if b_re.colliderect(st_re):
        e1=False
        clear=True
        
    if e2:
        sc.blit(st2,st_re2)
    if b_re.colliderect(st_re2):
        e2=False
        clear2=True
    if clear and clear2:
        sc.blit(text,(320,250))
        playing=False
    if e1:
        sc.blit(st,st_re)
    sc.blit(st,st_re)
    sc.blit(st2,st_re2)
    sc.blit(pan,p_re)
    sc.blit(pan,p_re1)
    sc.blit(pan,p_re2)
    sc.blit(pan,p_re3)
    sc.blit(pan,p_re4)
    sc.blit(pan,p_re5)
    sc.blit(pan,p_re6)
    sc.blit(pan,p_re7)
    sc.blit(pan,p_re8)
    sc.blit(pan,p_re9)
    sc.blit(pan,p_re10)
    sc.blit(pan,p_re11)
    sc.blit(pan,p_re12)
    sc.blit(pan,p_re13)
    sc.blit(pan,p_re14)
    sc.blit(pan,p_re15)
    sc.blit(pan,p_re16)
    sc.blit(pan,p_re17)
    sc.blit(pan,p_re18)
    sc.blit(st,st_re)
    if b_re.colliderect(p_re):
        y=-30
    if b_re.colliderect(p_re1):
        y=-30
    if b_re.colliderect(p_re4):
        y=-30
    if b_re.colliderect(p_re7):
        y=-30
    if b_re.colliderect(p_re9):
        y=-30
    if b_re.colliderect(p_re14):
        y=-30
    if b_re.colliderect(p_re18):
        y=-30
    if b_re.colliderect(p_re17):
        y=-30
    
    p.display.flip()    #화면업데이트
