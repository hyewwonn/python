# print(bool(True))
# print(bool(False))
# print(bool(0))
# print(bool(3))
# print(bool(""))
# print(bool("test"))
# print(bool([]))
#print(bool([1, 2, 3]))

# 중첩if
#n = (int)(input("숫자 입력 : "))
# if(n > 0):
#    print("plus")
# else:
#    print("minus")

# if(n % 2 == 0):
#    print("even")
# else:
#    print("odd")

#n = (int)(input("숫자 입력 : "))
# if(n > 0):
#    print("plus")
#    if(n % 2 == 0):
#        print("even")
#    else:
#        print("odd")
# else:
#    print("minus")
#    if(n % 2 == 0):
#        print("even")
#    else:
#        print("odd")

table = [["월", "화", "수", ], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+"")
    print()
