#2307 양혜원
s = list(input("영문자 입력 : "))
s_reverse = ''

for char in s:
    s_reverse = char + s_reverse
    
print(f'거꾸로 출력: {s_reverse}')
