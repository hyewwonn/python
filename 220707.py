# g = 1


# def testScope(a):
#     global g
#     g = 2
#     return g+a


# print(testScope(1))
# print(g)


# def p(*b): #이름상관없음
#     str = ""
#     for a in b:
#         str = str+a
#     print(str)


# p("👎")
# p("👎", "😋")
# p("👎", "😍", "❤", "🐸")

# def union(*ar):
#     result = []
#     for item in ar:
#         for x in item:
#             if x not in result:
#                 result.append()

# def gugudan(dan=2):
#     for i in range(1, 10):
#         print("{} x {} = {}".format(dan, i, dan*i))


# gugudan(3)
# gugudan()


# def setValue(newValue):
#     x = newValue


# retValue = setValue(10)
# print(retValue)


# def swap(x, y):
#     return y, x


# print(swap(1, 2))  # 여러 개 리턴 -> 튜플
# retValue = swap(1, 2)
# print(retValue[0], retValue[1])  # 튜플 () 없애기 (or for문)

# def sum(*num):
#    sumvalue = 0
#    for i in range(0, len(num)+1):
#        sumvalue += num[i]
#    return sumvalue


#result = sum(1, 3)
#print("1 + 3 = ", result)

#print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))


# def min(*nums):
#    min = nums[0]
#    for i in range(1, len(nums)):
#        if min > nums[i]:
#            min = nums[i]
#    return min


# result = min(1, 3)
# print("min(1, 3) = ", result)
# print("min(0, 3, -11) = ", min(0, 3, -11))


# def min(*numbers):
#    min_value = numbers[0]
#    for number in numbers:
#        if min_value > number:
#            min_value = number
#        return min_value


# result = min(1, 3)
# print("min(1,3) =", result)
# print("min(0,3,-11) =", min(0, 3, -11))


# def div_name(n):
#     return n[0], n[1:]


# surname, name = div_name("양혜원")
# print("성 : ", surname)
# print("이름 : ", name)
