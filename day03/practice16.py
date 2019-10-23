"""
    猜数字
    随机产生一个数字
    猜数字，大了小了
"""
import random

random_number = random.randint(1,100)
print(random_number)
count = 0
while True:
    guess_num = int(input("请输入一个数字："))
    count +=1
    if guess_num >random_number:
        print("大了，大了")
    elif guess_num <random_number:
        print("小了，小了")
    else:
        print("恭喜答对了,你打了"+str(count)+"次")
        break