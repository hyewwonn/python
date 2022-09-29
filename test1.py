# 2307 양혜원

1.
x = int(input("정수1 입력 : "))
y = int(input("정수2 입력 : "))

x, y = y, x

for a in range(x, y+1):  # 2~3단 #반복문이나 조건문 끝에 콜론
    print('{0}단'.format(a))
    for b in range(1, 10):  # 1~9
        print('{0} x {1} = {2:2}'.format(a, b, a * b))

    print('\n')


print("\n")

# 2.
n1 = int(input("점수1 입력 : "))
n2 = int(input("점수2 입력 : "))
n3 = int(input("점수3 입력 : "))
n4 = int(input("점수4 입력 : "))
n5 = int(input("점수5 입력 : "))

print("입력된 점수 :", n1, n2, n3, n4, n5)
sum = n1+n2+n3+n4+n5
print("합계 :", sum)
avg = (sum/5)
print("평균 :", '{0:0.2f}'.format(avg))

if avg >= 60:
    print('{0:0.2f}점으로 합격입니다.'.format(avg))
else:
    print('{0:0.2f}점으로 불합격입니다.'.format(avg))


print("\n")

# 3.
d = {"메로나": [1000, 20], "비비빅": [700, 3], "바밤바": [850, 100]}

print("상품명 가격 수량")
for keys in d:
    print('{0}"\t"{1}"\t"{2}'.format(d, d[keys][0], d[keys][1]))

print("\n")

# 3-3.
print("2. 상품 수정")
i = d[(input("상품명 입력 : "))]
print("1. 가격 수정")
print("2. 수량 수정")
menu = int(input("메뉴 입력 : "))
if menu == 1:
    d[i] = int(input("가격 입력 : "))

else:
    pass

print("\n")
print("상품명 가격 수량")
for k, v in d.items():
    print(k, v)

print("\n")

# 3-4.
print("3. 상품 삭제")
de = (input("상품명 입력 : "))
del d[de]

print("상품명 가격 수량")
for k, v in d.items():
    print(k, v)

# 3-5

# 3-6
