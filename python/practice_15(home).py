val1 = int(input("첫번째 정수"))
val2 = int(input("두번째 정수"))
val3 = int(input("세번째 정수"))



if (val1 <= val2 and val1 < val3):
    smallest = val1

elif(val2 <= val1 and val2 < val3):
    smallest = val2
    

else: smallest = val3

print(f"{smallest}")

################

weight = int(input("체중을 입력하세요"))
height = int(input("키를 입력하세요"))

standard = (height - 100) * 0.9

if (weight > standard):
    print("과체중입니다.")

if (weight == standard):
    print("과체중입니다.")

if (weight < standard):
    print("저체중입니다.")