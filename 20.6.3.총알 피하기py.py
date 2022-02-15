import pygame as p #파일저장명 :20200523_키보드 조작키
import random as r
p.init() # 라이브러리 초기화

size = (700,400) #(가로,세로)


sc = p.display.set_mode(size) # 해상도 크기 설정 
w = (255,255,255) #(R,G,B) 흰색
b = (0,0,0) #검정
#이미지 변수에 업로드 
pl = p.image.load("8 (3).png")
pl_r=pl.get_rect(left=50,top=50)
bg = p.image.load("배경.png")
e = p.image.load("총알.png")
e_r=e.get_rect(left=700,top=200)
bg1=bg.copy()
sco=0
f=p.font.SysFont('malgungothic',20)
f1=p.font.SysFont('malgungothic',50)

p.display.set_caption("키보드 조작") #게임창 제목

playing = True
# 동그라미 좌표 
x= 10
y= 0
# 동그라미 부드럽게
y_c = 0
#배경좌표
bg_1 =0  #첫번째 배경 
bg1_x=700#복사본 배경 
x1=650
y1=0
while playing:

      for event in p.event.get(): # 사용자가 뭘 눌렀는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누른다면
                  playing = False # 게속반복을 종료
                  p.quit() #게임창x버튼 누르면 사라짐 
                  quit #sell 창 종료
            if event.type == p.KEYDOWN: #키보드를 눌렀을때 반응
                  if event.key == p.K_UP: #위 방향키를 누르면 
                        y = -3
                  if event.key == p.K_DOWN: 
                        y = 3
            #if event.type == p.KEYUP: #키보드를 때었을때 반응
                 # if event.key == p.K_UP or event.key == p.K_DOWN:
                       # y = 0
      pl_r.top += y
    
      
      sc.fill(w) #바탕화면 흰색으로
      sc.blit(bg,(bg_1,0)) #배경 화면에 업로드
      sc.blit(bg1,(bg1_x,0))
      sc.blit(e,e_r)
      bg_1 -=1
      bg1_x -=1
      e_r.left -=5
      if e_r.left<0:
            sco +=1
            e_r.left=700
            e_r.top=r.randint(0,350)
      if bg_1 == -700:
            bg_1=700
      if bg1_x == -700:
            bg1_x=700
      sc.blit(pl,pl_r) #비행기 화면에 업로드 
      if pl_r.top>350:
            y=0
      if pl_r.top<5:
            y=0
      t= f.render('점수{}'.format(sco),True,(0,0,0))
      t1=f1.render("GAME OVER",True,(255,0,0))
      if pl_r.colliderect(e_r):
            sc.blit(t1,(200,150))
            playing=False       
      sc.blit(t,(600,0))
            
      
      p.display.flip() #화면 업데이트 

      
      

      


      
