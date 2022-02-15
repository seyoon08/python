
import random
import time

a = ["dog","cat","fox","panda","mouse","snake","frog"]

n=1

print ("[타자게임] 준비 되면 엔터")
input()
start = time.time()

q=random.choice(a)


while n<=5 :
    print("문제",n)
    print(q)
    x=input()


    if q==x:
        print("good")
        n=n+1
        q=random.choice(a)

    else:
        print("try again")



end = time.time()

et=end-start
et2= format(et,'2f')

print("걸린시간:",et2,"초")




