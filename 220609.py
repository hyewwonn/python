d = {"apple": 100, "orange": 200, "banana": 300}
for item in d:
    print(item, d[item])

a = [(1, 2), (3, 4), (5, 6)]

for(first, last) in a:
    print(first+last)

for i in range(0, 10):
    for j in range(0, i):
        print("*", end="")
    print("")

for i in range(1, 11):
    print("*"*i)

for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*1))
for i in range(1, 9+1):
    print("3 x {} = {}".format(i, 3*1))
for i in range(1, 9+1):
    print("4 x {} = {}".format(i, 4*1))
for i in range(1, 9+1):
    print("5 x {} = {}".format(i, 5*1))

for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} x {} = {}".format(dan, i, dan*i))

for i in range(1, 6):
    print("  "*(5-i), end="")
    print("* "*(2*i-1))

table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+"")
    print()

for i in range(1, 9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i, 2*i))

array = []
for i in range(1, 10, 2):
    array.append(i*i)
print(array)

array = [i*i for i in range(1, 10, 2)]
print(array)

array = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array)


x = 3
while x < 6:
    print(x)
    x += 1

# echo = input()
# while echo != "exit":
#     print(echo)
#     echo = input()

# print("")

# echo = input()
# while True:
#     if echo == "exit":
#         break
#     print(echo)
#     echo = input()

print(list(range(10)))
print(list(range(5, 10)))
print(list(range(10, 0, -1)))
print(list(range(10, 20, 2)))


lst = [1, 2, 3, 4, 5]
print(lst)
lst = [i**2 for i in lst]
print(lst)

test = ("apple", "banana", "orange")
test_len = [len(i) for i in test]
print(test_len)

d = {100: "apple", 200: "banana", 300: "orange"}
d_upper = [v.upper() for v in d.values()]
print(d_upper)

lst = [10, 25, 30]
iteL = filter(None, lst)
for item in iteL:
    print("item : {0}".format(item))


def getBiggerThan20(i):
    return i > 20


lst = [10, 25, 30]
iteL = filter(getBiggerThan20, lst)
for item in iteL:
    print("item : {0}".format(item))

num = (int)(input("수 입력 : "))
if num % 3 == 0:
    print("{}은(는) 3의 배수이다.".format(num))
elif num % 5 == 0:
    print("{}은(는) 5의 배수이다.".format(num))
elif num % 8 == 0:
    print("{}은(는) 8의 배수이다.".format(num))
else:
    print("어느 배수도 아니다.")
# 15를 3,5 배수라고 출력 => elif를 if로
# if num%3==0 and num%5==0 and num%8==0: 3, 5, 8의 배수가 아님
# not => !(조건)
# and의 not == or
