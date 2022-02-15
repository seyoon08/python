
while True :
    
    print("==================")
    print("== 1. 원의 둘레 구하기 ==")
    print("== 2. 원의 넓이 구하기 ==")
    print("== 3. 그만두기 ==")
    print("==================")
    print()
    s = int(input("메뉴선택 :"))


    if s==3 :
        print("종료")
        break
    if s == 1 or s == 2  :
        lo= int(input("지름 값? :"))
    if s ==1:
        print("원의 둘레 출력중....")
        x = lo * 3.14 
        print ("원의 둘레:",x)
    elif s ==2:
        print("원의 넓이 출력중....")
        x = (lo / 2) ** 3.14
        print ("원의넓이:",x)

