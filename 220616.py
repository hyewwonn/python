# income = (int)(input("근로소득 입력(만 원) : "))
# if income <= 2000:
#     tax = 0.05
# elif income <= 4000:
#     tax = 0.15
# elif income <= 8000:
#     tax = 0.25
# else:
#     tax = 0.4

# print("소득세 : {}만 원".format((int)(tax*income))


# income = (int)(input("현 연봉을 입력하세요 : "))
# grade = input("근무평가등급을 입력하세요 : ")

# if grade == "우수":
#     n = income*0.06
# elif grade == "보통":
#     n = income*0.04
# elif grade == "불량":
#     n = income*0.02

# print("연봉인상액 : {}".format((int)(n)))
# print("새 연봉인상액 : {}".format((int)(income+n)))


# def times(a, b):
#     return a*b


# print(times)
# print(times(10, 5))

# myTimes = times
# print(myTimes)
# print(myTimes(10, 5))
# # 주소같음


# # 절댓값
# print(10, "의 절댓값 : ", abs(10))
# print(-10, "의 절댓값 : ", abs(-10))

# # 10진수 => 2진수 변환
# print(128, "의 2진수 : ", bin(128))
# print(1255, "의 2진수 : ", bin(255))
# # 10진수 => 8진수 변환
# print(7, "의 2진수 : ", oct(7))
# print(8, "의 2진수 : ", oct(8))
# # 10진수 => 16진수 변환
# print(15, "의 2진수 : ", hex(15))
# print(16, "의 2진수 : ", hex(16))

# # 연산
# numbers = [1, 5, -2, 0, 6]
# print(numbers, "중 가장 큰 값은 ", max(numbers))
# print(numbers, "중 가장 작은 값은 ", min(numbers))
# print(numbers, "합계는 ", sum(numbers))
# print("2의 10승은", pow(2, 10))

# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은", round(pi))
# print(pi, "의 소수점 1자리 반올림은", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은", round(pi, 3))

# user_name = input("이름은?")
# user_age = input("나이는?")
# print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
# say = "{0}님! 나이는 {1}t[rnsdy! {1}세라니 놀라워요!"
# print(say.format(user_name, user_age))

# pi = "3.14159"
# print("문자열 출력 : ", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi)+100)
# year = "2018"

# print("올해 연도 : ", year)
# print("100년 뒤는 ", int(year) + 100 + "년입니다.")
# print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
# print("올해는 ", str(year) + "년입니다.")

# list = ['d', 'c', 'a', 'b']
# list.reverse()
# print("리스트 항목 순서 뒤집기", list)
# list.sort()
# print("리스트 항목 정렬하기", list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기", list)
# for index, value in enumerate(list):
#     print("인덱스", index, "위치의 값은 ", value)

# str1 = "나는 문자열"
# print(str1)
# n = 3
# print(str(n))  # 오류 발생(변수명으로 str을 사용해서)


# import random

# n = random.randint(1, 6)
# print("결과 :", n)
# n = random.randint(1, 6)
# print("결과 :", n)
# n = random.randint(1, 6)
# print("결과 :", n)


# def rolling_dice():
#     n = random.randint(1, 6)
#     print("6면 주사위 굴린 결과 :", n)


# rolling_dice()
# rolling_dice()
# rolling_dice()


n = (int)((input)("숫자 입력 : "))
cnt = 0
for i in range(2, n):
    if n % i == 0:
        cnt = 1
        break

if cnt == 0:
    print("{}은(는) 소수입니다.".format(n))
else:
    print("{}은(는) 소수가 아닙니다.".format(n))
