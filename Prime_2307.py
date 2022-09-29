# 2307 양혜원
print("1 ~ N  까지의 소수와 그 갯수를 구하는 프로그램")
num = int(input("N 입력 : "))


def isPrimeNumber(num):
    cnt = 0
    result = []
    print("소수 : ", end='')

    for i in range(1, num+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            result.append(i)
            cnt += 1

    print("1~ {} 까지 소수의 갯수 : ".format(num), cnt-1)


isPrimeNumber(num)
