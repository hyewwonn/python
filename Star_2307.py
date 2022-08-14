#2307 양혜원
s = (input("점수 입력 : "))
li = s.split(" ")
count = []
max = int(li[0])
min = 101


    if int(li[i]) > max:
        max = int(li[i])
    
    if int(li[i]) < min:
        min = int(li[i])

print("최고점수 : ", max)
print("최저점수 : ", min)
