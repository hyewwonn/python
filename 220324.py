# h = "  Happy Programming! "
# print(len(h))
# print(h.count("p"))
# print(h.upper())
# print(h.lower())
# print(h.strip())
# print(h.replace("Happy", "Funny"))
# print(h.find("ap"))
# print(h.rfind("a"))
# print(h.find("zoo"))

# print("\n")

# print("a" in h)
# print("amp" in h)
# x = "01::23::ab::&&"
# y = x.split("::")
# print(y)
# print(", ".join(y))

# print("\n")

# s = "name: {}, number: {}, soccer: {}"
# print(s.format("Ronaldo", 7, True))
# print("name: {name}, number: {num}".format(name = "Jordan", num = 23))

# print("{:d}".format(515))
# print("{:5d}".format(515))
# print("{:+5d}".format(515))
# print("{:=+5d}".format(515))
# print("{:05d}".format(515))
# print("{:+05d}".format(515))

# print("{:f}".format(11.17))
# print("{:12f}".format(11.17))
# print("{:12.1f}".format(11.17))

# print("{:=+6.1f}".format(11.17))

# print("\n")

# a = 2
# b = 3
# s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)
# print(s)
# # 함수와 메서드의 차이점
# # 함수는 누가 하는지가 없음
# # 메서드는 클래스에 소속, 함수는 소속 없이

# print("\n")

# # 직접 대입하기
# s1 = 'name : {0} '.format('BlockDMask')
# print(s1)

# # 변수로 대입하기
# age = 55
# s2 = 'age : {0}'.format(age)
# print(s2)

# # 이름으로 대입하기
# s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='남')
# print(s3)

# # 인덱스를 입력하지 않으면?
# s4 = 'name : {}, city : {}'.format('BlockDMask', 'seoul')
# print(s4)

# # 인덱스 순서가 바뀌면?
# s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
# print(s5)

# # 인덱스를 중복해서 입력하면?
# s6 = 'test1 {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')
# print(s6)

# # 중괄호 출력
# s7 = 'Format example. {{}}, {}'.format('test')
# print(s7)

# # 중괄호로 겹쳐진 인자값
# s8 = 'This is value {{{0}}}'.format(1212)
# print(s8)

# # 왼쪽 정렬
# s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
# print(s9)

# # 오른쪽 정렬
# s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
# print(s10)

# # 가운데 정렬
# s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
# print(s11)

# # 왼쪽 정렬
# s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a')
# print(s12)

# # 오른쪽 정렬
# s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b')
# print(s13)

# # 가운데 정렬
# s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')
# print(s14)

# # 정수 N자리
# s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
# print(s15)

# # 소수점 N자리
# s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
# print(s16)

# print("\n")

# a = 2
# b = 1
# #s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)

# for a in range(2,10): #2~3단 #반복문이나 조건문 끝에 콜론
#     print('{0}단'.format(a))
#     for b in range(1,10): #1~9
#         print('{0} x {1} = {2:2}'.format(a, b, a * b))
#     print('\n')

# #% 서식문자
# #print('%s 왔나요?') % name[i]
# #%기호 뒤에 자료형을 가리키는 문자 사용

# num = 50
# s = 'my age %d' % num

# print(s)

# #%s 문자열 %d 정수 %f 실수

# names = ['kim', 'park', 'lee']
# for name in names:
#     print('my name is %s' % name)

# money = 10000
# s2 = 'give me %d won' % money
# print(s2)

# d = 3.141592
# print('value %f' % d)

# #출력해야 할 값이 두 개 이상인 경우 ()를 이용
# s1 = 'my name is %s. age: %d' % ('mirim', 100)
# print(s1)

# #출력해야 할 값이 점점 많아질수록
# age = 78
# money = 20000
# name = 'Jang'
# weight = 63.12
# etc = 'abcde'
# s2 = 'my name is %s, age: %d, weight: %f, money: %d, etc: %s' % (name, age, weight, money, etc)
# print(s2)

# #문자열 포매팅
# month = 1
# while month <= 12:
#     print(f'2020년 {month}월')
#     month = month + 1 #month++

# #f-string #3.6버전 이상
# #f'문자열 {변수} 문자열'
# s = 'coffee'
# n = 5
# result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
# print(result1)

# #왼쪽정렬
# s1 = 'left'
# result1 = f'|{s1:<10}|'
# print(result1)

# #가운데정렬
# s2 = 'mid'
# result2 = f'|{s2:^10}|'
# print(result2)

# #오른쪽정렬
# s3 = 'right'
# result3 = f'|{s3:>10}|'
# print(result3)

# num = 10
# result = f'my age {{{num}}}, {{num}}'
# print(result) #{10}, {num}

# #f-string과 딕셔너리 #순서x, 키:값, 키로 값을 꺼냄, {}
# d = {'name': 'Mirim', 'gender': 'female', 'age': '18'}
# result =f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]} '
# print(result)

# #리스트 #순서o, []
# n = [100,200,300]

# print(f'list: {n[0]}, {n[1]}, {n[2]}')

# for v in n: #list 개수만큼
#     print(f'list with for : {v}')


# strB = "파이썬 연습"
# print(len(strB))

# print("\n")

# strA = "Hello python"
# x = 5
# y = 3.14
# print(type(strA))
# print(type(x))
# print(type(y))

# print("\n")

# import keyword
# print(keyword.kwlist)

# print("\n")

# print("py""thon")
# print("py"+"thon")
# print("py"*3)

# print("\n")

# strA = "python"
# print(strA[0:1])
# print(strA[1:3])
# print(strA[:2])
# print(strA[-2:])
# print(strA[:])
# #문자열 슬라이싱 - 0부터 시작하고 자기 번호는 제외, 뒤쪽에서 카운트를 시작하면 -1부터 시작

# strB = "python is powerful"
# print(strB[-1])
# print(strB[-2])
# print(strB[7:18])
# print(strB[:])
# print(strB[::2])
# #:(전체)를 출력하고 :2(간격) 띄워서

# print(strB[-11:9])
# print(strB[-11:8])
# print(strB[-18:-12])
# print(strB[-18:-11])

# print("\n")

# colors = ["red", "green", "blue"]
# print(colors)
# print(type(colors))

# print("\n")

# #append() 메서드 - 기존 리스트에 값 추가
# #insert() 메서드 - 원하는 위치에 추가
# print(colors)
# colors.append("blue")
# print(colors)

# colors.insert(1,"black")
# print(colors)

# print(colors.index("red"))
# colors+=["red"]
# print(colors)
# print(colors.index("red",1))
# colors+="red"
# print(colors)

# print("\n")

# #count()메서드 - 현재 해당 값의 개수를 반환
# #pop()메서드 - 값을 뽑아내서 반환 (없애면서 리턴)
# print(colors)
# print(colors.count("red"))
# print(colors.pop())
# print(colors.pop())
# print(colors.pop(1))
# print(colors)
# print()

# print("\n")

# #remove()메서드 - 단순히 해당 값을 삭제
# print(colors)
# #print(colors.remove("blue")) => None
# colors.remove("blue") #앞에거
# print(colors)

# print("\n")

# #extend()메서드 - 데이터 추가
# print(colors)
# colors.extend(["blue", "yellow", "white"])
# print(colors)

# print("\n")

# #sort() 메서드: 오름차순 정렬
# #reverse() 메서드 : 내림차순 정렬
# print(colors)
# colors.sort()
# print(colors)
# colors.reverse()
# print(colors)

# #튜플 : 순서존재, 리스트와 달리 [] 대신 ()로 묶어서 표현하고 읽기 전용

# #세트 : 집합과 동일, 유일한 값의 모임, 순서없음
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print(a.union(b)) #합집합
# print(a.intersection(b)) #교집합
# print(a.difference(b)) #차집합

# def calc(a, b):
#     return a+b, a*b

#     x,y = calc(5, 4)
#     print(x, y)

# print("id : %s, name : %s" % ("kim", "김유신"))

# args = (3, 4)
# print(calc(*args))

# a = {1,2,3,4}
# b = {3,4,4,5}

# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# print("\n")

# a = set((1,2,3,2))
# print(a)
# print(type(a)) #tuple -> set

# b = list(a)
# print(b)
# print(type(b)) #set -> list

# c = tuple(b)
# print(c)
# print(type(c)) #list -> tuple

# print("\n")

# #딕셔너리 : 키-값
# colors = {"apple" : "red", "banana" : "yellow"}
# print(colors)

# colors["cherry"] = "red" #["키"] = "값"
# print(colors)

# for item in colors.items():
#     print(item)

# print(colors)
# del colors["cherry"] #삭제
# print(colors)
# colors.clear()
# print(colors)

# device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
# device["아이맥"] = 15 #추가
# device["아이폰"] = 6 #동일한 키가 있으면 키의 값만 변경
# print(device)
# del device["아이폰"] #삭제
# print(device)

# print("\n")

# phone = {"kim":"1111", "lee":"2222", "park":"3333"}
# print(phone.keys())

# print(phone.values())

# print("park" in phone)
# print("moon" in phone)

# p = phone
# print(p)

# d = {"a":10, "b":200, "c":300}

# print("\n")

# #딕셔너리-for문으로 참조하기
# for key in d.keys():
#     print(key)

# for value in d.values():
#     print(value)

# print("\n")

# #bool : 참과 거짓을 나타내는 자료형(boolean), true/false
# isRight = False
# print(type(isRight))
# print(1 < 2)
# print(1 != 2)
# print(1 == 2)
# print(True and True and False)
# print(True or False or False)

# print("\n")

# #수치를 논리연산자에 포함하는 경우
# #0은 false
# #음수를 포함해 값이 있는 것들은 true
# print(bool(0))
# print(bool(-1))
# print(bool("test"))
# print(bool(None))
# print(bool(""))
# print(bool(" "))
# print(bool(''))
# print(bool(' '))

# print("\n")

# #mutable : 변경되는 객체(객체의 상태를 변경할 수 있음)
# #list, set, dictionary
# #immutable : 변경되지 않는 객체(객체의 상태를 변경할 수 없음)
# #int,float 등

# #immutable 객체(상태 변경 x)
# print("immutable 객체")
# a = 99
# b = 99
# c = 99
# d = 99
# e = 99
# print(hex(id(a)))
# print(hex(id(b)))
# print(hex(id(c)))
# print(hex(id(d)))
# print(hex(id(e)))
# #id가 주소
# #hex : 16진수로 표현하려고
# #데이터가 같으면 주소똑같음
# #하나에 여러 데이터 참조

# print("\n")

# #mutable 갹채(상태 변경 o)
# print("mutable 객체")
# arr1 = [1,2,3]
# arr2 = [1,2,3]
# arr3 = [1,2,3]
# arr4 = [1,2,3]
# print(hex(id(arr1)))
# print(hex(id(arr2)))
# print(hex(id(arr3)))
# print(hex(id(arr4)))
# #주소다름
# #처음부터 다른 방
# #mutable 한 리스트는 값이 자유롭게 바뀔 수 있기 때문에 각각의 메모리를 할당해주는 게 관리가 더 용이하기 때문

# #immutable 객체
# print("=" + 50)
# print("immutable 객체 예제.")
# print("=" + 50)
# print("1. int값이 변경되면?")
# num1 = 99
# num2 = 99
# num3 = 99
# num4 = 99
# print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
# print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
# print(f"num1 값 : {num3} \t주소 : {hex(id(num3))}")
# print(f"num1 값 : {num4} \t주소 : {hex(id(num4))}")
# num1 += 1 #num1 값 증가
# num3 += 1 #num3 값 증가
# num4 += 10 #num4 값 증가
# print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
# print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
# print(f"num1 값 : {num3} \t주소 : {hex(id(num3))}")
# print(f"num1 값 : {num4} \t주소 : {hex(id(num4))}")

# print("\n")

# print("2. str값이 변경되면?")
# s1 = "BlockDMask"
# s2 = "BlockDMask"
# s3 = "BlockDMask"
# s4 = "BlockDMask"
# print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
# print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")
# s1 = s1.replace('D', 'ZZZ') #replace로 값을 변경하고, 새로운 문자열을 s1에 대입하게됨
# s2 = "BlockZZZMask"
# s4 = s4.super() #대문자로 변경
# print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
# print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")

# print("\n")

# #mutable 객체
# print("=" * 50)
# print("mutable 객체 예제.")
# print("=" * 50)
# print("1.list 값이 변경되면?")
# arr1 = ['a','b', 77]
# arr2 = ['a','b', 77]
# arr3 = ['a','b', 77]
# print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")
# arr1.append(10) #['a','b', 77, 10]
# arr2.append(10) #['a','b', 77, 10]
# print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")

# print("\n2. dictionary 값이 변경되면?")
# d1 = {'a' : 11, 'b' : 22, 'c' : 33}
# d2 = {'a' : 11, 'b' : 22, 'c' : 33}
# d3 = {'a' : 11, 'b' : 22, 'c' : 33}
# print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")
# d1['a'] = 99
# d2['d'] = 44
# print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")

# print("\n")

# from re import X


# student_grade = 2
# student_class = 3
# student_number = 7
# student_name = "양혜원"
# student_height = 158.0

# print(type(student_grade))
# print(type(student_class))
# print(type(student_number))
# print(type(student_name))
# print(type(student_height))

import copy


our_team = ["김비야", "김유진", "박선주", "백선미", "안소영",
            "양혜원", "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하진"]
print(our_team[9])

print(our_team[5:9])

# club = {"혜원": "js study"}
# print(club)

# l = []
# print(l)
# player = ["Messi", 10, True]
# print(player)
# print(list("Happy"))
# print(list((1125, 2436)))
# print(list({"사과", "배"}))
# nums = list(range(3))
# print(nums)

# nums + [10, 11]
# print(nums)
# nums += [10, 11]
# print(nums)
# nums.append(20)
# print(nums)
# nums.append([30, 31])
# print(nums)
# nums.insert(2, 40)
# print(nums)
# nums.extend([50, 51])
# print(nums)

# print("\n")

# nums[7]
# print(nums[7])
# nums[7] = 60
# print(nums)

# print("\n")

# del nums[2]
# print(nums)
# nums.remove(20)
# print(nums)
# print(nums.pop())
# print(nums.pop(5))
# nums.append(10)
# print(nums)
# nums.remove(10)
# print(nums)
# nums.clear()
# print(nums)

# print("\n")

# nums = list(range(3))
# print(nums)
# nums += [100, 10]
# print(nums)
# print(nums[3])
# print(3 in nums)
# print(10 in nums)

# print("\n")

# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)

# print("\n")

# print(range(3))
# print(range(1, 10))
# print(range(1, 10, 2))
# print(set(range(1, 10, 2)))
# print(list(range(1, -5, -2)))
# for i in range(3):
#     print(i)

# print("\n")

# t = ()
# print(t)
# xy = (2560, 1440)
# print(xy)
# color = 129, 247, 216
# print(color)
# print(xy + color)
# print(xy * 2)

# print("\n")

# color = 129, 247, 216
# red, green, blue = color
# print(red)
# print(green)
# print(blue)
# x, y = 1920, 1080
# print(x)
# print(y)

# print("\n")

# x = 2560
# y = 1440
# x, y = y, x
# print(x)
# print(y)
# a = (123, "abc", True, 123)
# print(a[1])
# print(a[2:])
# print(a[:2])
# print(a[1] = 2)
# print(a.index("abc"))
# print(a.count(123))

# print("\n")

# t = (1, 2, 3)
# t += (4,)  # , 있어야 오류 안 남
# print(t)

# print("\n")

# d = {}
# print(d)
# urls = {"google": "google.com", 18: "unesco.org"}

# urls["x"] = 2560
# print(urls)

# urls["x"] = 1920
# print(urls)

# del urls["x"]
# print(urls.pop(18))
# urls.clear()
# print(urls)

# print("\n")

# urls = {"google": "google.com", 18: "unesco.org"}
# print(urls["google"])
# print(urls.get("google"))
# print("google" in urls)
# print("google.com" in urls)
# print("google.com" in urls.values())

# print("\n")

# game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
# print(game)
# print(set("Funny"))
# print(set([2048, "Tetris", "Cube"]))
# print(set((2560, 1440)))
# print(set({"google": "google.com", 18: "unesco.org"}))
# print(set(range(3)))  # 순서없음

# print(game.add("FIfa"))
# print(game.update(("NBA", "MLB")))

# print(game.remove("LOL"))

# print("\n")

# s3 = {3, 6, 9, 12}
# s4 = {4, 8, 12, 16}
# s3 & s4
# print(s3.intersection(s4))  # 교집합

# print("\n")

# s3 | s4
# print(s3.union(s4))  # 합집합

# print("\n")

# s3 - s4
# print(s3.difference(s4))  # 차집합

# s3 ^ s3
# print(s3.symmetric_difference(s4))  # 대칭 차집합

club = {"김비야": "영화감상반", "김유진": "코딩클리닉반", "박선주": "도서반", "백선미": "심리학연구반",  "안소영": "금융경제반",
        "양혜원": "피구반", "이혜령": "교지편집반", "임재연": "또래상담반", "최윤영": "사진반", "최혜민": "코딩클리닉반",
        "하도연": "배드민턴반", "하진": "영화감상반"}

print(club["안소영"])

print(club[our_team[0]])

print("=" * 50)
print("mutable 객체 요소로 존재하는 immutable, mutable")
print("=" * 50)
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']
# 리스트(immutable) 객체의 주소
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")
# 리스트 내부의 mutable 요소
print("=" * 50)
print("리스트 내부의 mutable 요소들")
print(f"arr1[0] : {arr1[0]} \t주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr2[0]} \t주소 : {hex(id(arr2[0]))}")
print(f"arr1[1] : {arr1[1]} \t주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr2[1]} \t주소 : {hex(id(arr2[1]))}")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
print(f"arr1[4] : {arr1[4]} \t주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr2[4]} \t주소 : {hex(id(arr2[4]))}")

# 리스트 내부의 mutable 요소
print("=" * 50)
print("리스트 내부의 mutable 요소들")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")

# 얕은 복사(Shallow Copy) - 주소 복사
print("=" * 50)
arr1 = [1, 2, 3]
arr2 = arr1
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

arr1.append(4)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")


print("=" * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
#arr2 = arr1[:]
# arr2 = arr1.copy()  # copy메서드
arr2 = copy.copy(arr1)  # import copy
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

print("\n2.리스트의 끝에 값 추가")
arr2.append(22)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

print("\n3.리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
# 깊은 복사처럼 보여도 얕은복사(내부리스트 주소같음)

print("\n4.리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")

print("\n5.리스트 전체 다시 확인")
arr1[3].append(99)
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

# = 주소동일
# [:] 주소다름, 내부주소동일
# .copy 주소다름, 내부주소동일
# copy.copy() 주소다름, 내부주소동일

# dictionary도 가능

print('='*50)
d1 = {'a': 'Mirim', 'b': [1, 2, 3]}
d2 = copy.copy(d1)  # copy 모듈 얕은복사
print("1. 전체 출력")
print(f"d1 : {d1}, address : {hex(id(d1))}")
print(f"d2 : {d2}, address : {hex(id(d2))}")

print("\n2. 딕셔너리에 새 key, value 추가")
d2['c'] = 'kimchi'
print("d2['c'] = 'kimchi'")
print(f"d1 : {d1}, address : {hex(id(d1))}")
print(f"d2 : {d2}, address : {hex(id(d2))}")

# 딕셔너리 내부에 리스트 value
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b'] : {d1}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2}, address : {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 값 추가")
d1['b'].append('NO')
print("d1['b'].append('NO')")
print(f"d1['b'] : {d1}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2}, address : {hex(id(d2['b']))}")

# 깊은 복사
print('=' * 50)
arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1)  # copy 모듈 깊은 복사
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

print("\n2. 리스트에 새 key, value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

# 리스트 내부에 리스트 추가
print("\n3. 리스트 내부 리스트")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print("arr1[2].append(10)")
print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")

print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

# 얕은복사 = / [:], copy.copy. list객체.copy
# 깊은복사 copy.deepcopy
