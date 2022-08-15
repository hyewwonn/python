print("1 ~ N  까지의 소수와 그 갯수를 구하는 프로그램")
n = int(input("N 입력 : "))

def isPrimeNumber(n):
    res = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res


res = isPrimeNumber(n)
s = str(res)[1:-1]
print("소수 : ", s)
print("1 ~ {}까지 소수의 갯수 : {}".format(n, len(res)))
