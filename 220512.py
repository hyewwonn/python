# 얕은 복사(주소복사)
# immutable객체는 얕은 복사와 깊은 복사 차이없음(값이바뀌면 주소바뀜)

# copy 메서드를 이용한 얕은 복사
num = '881120-10682364'
print("연월일 : ", num[:6])
print("숫자 : ", num[7:])

print("성별 : ", num[7])

print("\n")

li = [1, 3, 5, 4, 2]
print("원본 : ", li)
li.sort()
li.reverse()
print("결과 : ", li)

li2 = ['Life', 'is', 'too', 'short']
print(" ".join(li2))

print("\n")

t = (1, 2, 3)
t += 4,
print(t)

print("\n")

a = {'A': 90, 'B': 80, 'C': 70}
print("원본 딕셔너리 : ", a)
b = a.pop('B')
print("'B'추출 후 딕셔너리 : ", a)
print("추출된 B의 값 : ", b)
