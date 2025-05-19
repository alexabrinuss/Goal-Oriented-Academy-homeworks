num = int(input("enter your number:"))
num00 = int(input("enter your score:"))
for i in range(num, num00):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
    print(i)