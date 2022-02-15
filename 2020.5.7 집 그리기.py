#집 그리기
import pygame as p

p.init()

b=(0,0,0)
w=(255,255,255)
b2=(0,0,255)
g=(0,255,0)
r=(255,0,0)
s=[400,300]

s2=p.display.set_mode(s)

p.display.set_caption("이게임만든사람 천재")

d=False
c=p.time.Clock()

while not d:

      c.tick(10)

      for event in p.event.get():
            if event.type == p.QUIT:
                  d=True

      s2.fill(w)

      p.draw.rect(s2,b2,[30,150,190,150],5)
      p.draw.polygon(s2,r,[[30,150],[125,100],[220,150]])

      p.display.flip()
                  
