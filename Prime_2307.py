#2307 양혜원
print("1 ~ N  까지의 소수와 그 갯수를 구하는 프로그램")
num = int(input("N 입력 : "))

def isPrimeNumber(num):
    cnt = 0
    li = []
    for i in range(2, num):
        if num % i == 0:
            cnt = 1
            break

        if cnt == 0:
            li += [i]
    
    print("소수 : ",  li)
    print("1~ {} 까지 소수의 갯수 : ".format(num), len(li))

isPrimeNumber(num)