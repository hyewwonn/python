import random
origin = [0, 0, 0]
for i in range(0, 3):
    origin[i] = random.randint(0, 9)

    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)

    # print(origin[i], end='\t')
print()

cnt = 0
while True:
    myData = [0, 0, 0]
    myData = input(f"{cnt}회 숫자를 입력하세요 : ").split(" ")
    myData = list(map(int, myData))  # 문자리스트=>숫자리스트
    cnt = cnt+1

    # 판정
    # strike
    strike = 0
    for i in range(0, 3):
        if(origin[i] == myData[i]):
            strike = strike+1
    print(strike, "strike")

    # ball
    ball = 0
    for i in range(0, 3):  # origin
        for j in range(0, 3):  # myData
            if(i != j):   # ball 처리i==j strike에서 처리됨
                if (origin[i] == myData[j]):
                    ball = ball+1
    print(ball, "ball")

    if strike == 3:
        print(f"축하합니다. {cnt}회만에 맞추었습니다.")
        break
    elif cnt == 10:
        print(f"실패했습니다. {cnt}회가 되었습니다.")
