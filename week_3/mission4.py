num = int(input("몇줄짜리 트리?: "))

for i in range(num):
    sen = " " * (num - i) + "*" * (i * 2 + 1)
    print(sen)