import random
rpc =input("가위,바위,보 중 하나 입력")

choice=["가위", "바위", "보"]

c_choice = random.choice(choice)
print(f"{c_choice} 컴퓨터가 낸 거")
print(f"{rpc} 유저가 낸 거")
if (rpc == c_choice):
    print("무승부")

elif(rpc == "가위"  and c_choice =="보") or (rpc == "바위"  and c_choice =="가위") or (rpc == "보"  and c_choice =="바위"):
    print("당신이 이겼습니다.")
else:
    print("컴퓨터가 이겼습니다.")


    ##############################


    import random

f_b_os = ['+','-','*','/']
f_b_o = random.choice(f_b_os)

x = random.randint(1, 100)
y = random.randint(1, 100)

problem = f"{x} {f_b_o} {y}"
print(f"문제는 : {problem} = ?")

user = int(input("값을 입력하세요"))

if f_b_o == '+':
    correct = x + y
elif f_b_o == '-':
    correct = x - y
elif f_b_o == '*':
    correct = x * y
elif  f_b_o == '/':
    correct = x / y

else:
    print("연산의 문제")


if (user == correct):
    print("정답입니다.")
else:
    print(f"틀렸습니다. 정답은{correct}")