# age = int(input("请输入年龄："))
#
# if age >= 18:
#     print("成年人需要补票10元")
# else:
#     print("未成年人不需要补票")
# print("over")

# score = int(input("请输入成绩："))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("E")
import random

num = random.randint(1, 100)

if int(input("请输入猜测的数字：")) == num:
    print("恭喜你猜对了")
elif int(input("猜错了,再来一次：")) == num:
    print("恭喜你猜对了")
elif int(input("很遗憾，最后一次：")) == num:
    print("恭喜你猜对了")
else:
    print("很遗憾，猜错了,答案是{}".format(num))
