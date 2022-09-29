#2307 양혜원
s1 = set(input("첫 번째 문자열 입력 : "))
s2 = set(input("두 번째 문자열 입력 : "))

def intersect(s1, s2):
    s1 & s2
    res = list(s1.intersection(s2))
    res.sort()
    print(res)

intersect(s1, s2)