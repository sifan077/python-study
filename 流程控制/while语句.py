# i = 1
#
# res = 0
# while i <= 100:
#     res += i
#     i += 1
# print(res)


# import random
#
# num = random.randint(1, 100)
# count = 0
# flag = True
# while flag:
#     count += 1
#     guess = int(input("请输入一个1-100的整数："))
#     if guess == num:
#         print("恭喜你猜对了,您猜了{}次".format(count))
#         flag = False
#     elif guess > num:
#         print("猜大了")
#     else:
#         print("猜小了")


i = 1
while i < 10:
    j = 1
    while j <= i:
        print("{}*{}={}\t".format(i, j, i * j),end=" ")
        j += 1
    i += 1
    print()