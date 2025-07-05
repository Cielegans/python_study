temp = float(input("온도를 입력하세요"))

if(temp>=25):
    print("반바지를 추천합니다.") 

else:
    print("긴바지를 추천합니다.")

##################################33


valueString = (input("문자를 입력하세요."))


if (valueString == "R" or valueString=="r"):
    print("Rectangle")

elif (valueString == "T" or valueString=="t"):
    print("Triangle")

elif (valueString  == "C" or valueString=="c"):
    print("Cricle")

else:
    print("Unknown")

##########################################

value = int(input("반지름을 입력하세요"))

fomular = 3.14*value**2

print(f"{fomular}입니다.")