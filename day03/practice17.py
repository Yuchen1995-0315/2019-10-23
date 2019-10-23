import random

random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 3:
    guess_num = int(input("请输入一个数字："))
    count += 1
    if guess_num > random_number:
        print("大了，大了")
    elif guess_num < random_number:
        print("小了，小了")
    else:
        print("恭喜答对了,你打了" + str(count) + "次")
        break
    # if count ==3:
    #     print("回合结束^_^")
    #     break
else:  # 只有猜错次数超过三次才会执行
    print("回合结束^_^")
