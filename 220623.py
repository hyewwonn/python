import random

# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "6면 주사위 굴린 결과 :", n)


# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(10)

# def rolling_dice(pip, repeat):
#     for r in range(1, repeat + 1):
#         n = random.randint(1, pip)
#         print(pip, "6면 주사위 굴린 결과 :", n)


# rolling_dice(2, 3)
# rolling_dice(6, 4)
# rolling_dice(10, 12)


# def func_sum(in_list):
#     sum = 0
#     li = in_list.split(" ")
#     for i in range(0, len(li)):
#         sum += int(li[i])
#     return sum


# in_list = input("데이타 입력 : ")
# print("합 : ", func_sum(in_list))


# def p(*args):
#     str = ""
#     for a in args:
#         str = str+a
#     print(str)


# p("👎")
# p("👎", "😋")
# p("👎", "😍", "❤", "🐸")


# def p(space, space_num, *args):  # 가변인수맨마지막에
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)


# p(",", 3, "👎", "😋")
# p("👌", 2, "👎", "😍", "❤")
# p("_", 3, "👎", "😍", "❤", "🐸")


# def star(shape, *num):  # 가변인수맨마지막에
#     for i in range(0, len(num)):
#         print(shape * num[i])


# star("❤", 3)
# star("😎", 1, 2, 3)

# def fn(a, b, c, d*):
#     print(a, b, c, d)


# # 다음 코드 모두 실행되지 않음
# # fn(c=3, b=2, a=1, 4, 5) #SyntaxError: invalid syntax
# fn(1, 2, c=3, 4, 5)
