#2307 양혜원
s = (input("점수 입력 : "))
li = s.split(" ")
count = []
max = int(li[0])
min = 101
for i in range(0, len(li)):
    # if int(li[i]) >=90:
    #     count[0]+=[1]
    # elif int(li[i]) >=80:
    #     count[1]+=[1]
    # elif int(li[i]) >=70:
    #     count[2]+=[1]
    # elif int(li[i]) >=60:
    #     count[3]+=[1]
    # else:
    #     count[4]+=[1]


    if int(li[i]) > max:
        max = int(li[i])
    
    if int(li[i]) < min:
        min = int(li[i])

# print("90점 이상    : ", "*"*len(count[0]))
# print("80점 대      : ", "*"*len(count[1]))
# print("70점 대      : ", "*"*len(count[2]))
# print("60점 대      : ", "*"*len(count[3]))
# print("60점 미만    : ", "*"*len(count[4]))

print("최고점수 : ", max)
print("최저점수 : ", min)
