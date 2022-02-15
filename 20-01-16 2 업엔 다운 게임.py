#업 엔 다운게임

import random as r
n=r.randint(1,100)

while True:
    x = int(input("해"))
    if x ==n :
        print("ㅇㅋ")
        break
    if x < n:
        print("UP")
    if x > n:
        print("DOWN")
