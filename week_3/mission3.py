num = int(input("몇단 보쉴?: "))

if 1 <= num <= 9:
    for i in range(1,10):
        print(num," * ",i," = ",num*i)
else:
    print("종료되었습니다.")
    