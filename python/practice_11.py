height = int(input("키입력"))
age = int(input("나이 입력"))

if height >= 140:
    
    if age >= 10:
        print("입장가능")
    else:
        print("입장 불가능")
else:
    print("입장 불가능")