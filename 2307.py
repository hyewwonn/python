# 001
print("Hello, World!")

# 002
print("Mirim's Computer")

# 003
print('신씨가 소리질렀다. "도둑이야".')

# 004
print('"C:\Windows"')

# 005
print("안녕하세요.\n만나서\t반갑습니다.")

# 006
print("오늘은", "목요일")

# 007
print("naver", "kakao", "samsung", sep=";")

# 008
print("naver", "kakao", "samsung", sep="/")

# 009
print("first", "second")

# 010
print(5/3)

# 011
삼성전자 = 50000
print(삼성전자*10)

# 012
시가총액 = 298
현재가 = 50000
PER = 15.79
print(type(시가총액))
print(type(현재가))
print(type(PER))

# 013
s = "hello"
t = "python"
print(s+"! "+t)

# 014
print(2 + 2 * 3)

# 015
a = "132"
print(type(a))

# 016
num_str = "720"
num_str = int(num_str)
print(type(num_str))

# 017
num = 100
num = str(num)
print(type(num))

# 018
s = "15.79"
s = float(s)
print(s, type(s))

# 019
year = "2020"
year = int(year)
for i in range(-3, 0):
    print(year+i)

# 020
aircon = 48584
print(aircon*36)

# 021
letters = "python"
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print(string[::2])

# 024
string = "PYTHON"
sr = ''
for char in string:
    sr = char + sr
print(sr)

# 025
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))

# 027
url = "https://www.e-mirim.hs.kr"
# print(url[-3:-1])
url_split = url.split('.')
print(url_split[-1])

# 028
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 029
string = 'abcdefe2a354A32a'
print(string.replace("a", "A"))

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)
