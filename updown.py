import random
random_numer = random.randint(1, 100)
# print(random_numer)
cnt = 1
while True:
    try:
        my_number = int(input("1~100 사이의 수 입력 : "))
        if(my_number > random_numer):
            print("DOWN")
        elif(my_number < random_numer):
            print("UP")
        else:
            print(f"축하합니다. {cnt}회 만에 맞추었습니다.")
            break
        cnt = cnt+1
    except:
        print("에러가 발생했습니다. 숫자 1~100을 입력하세요.")
