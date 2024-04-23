f = open("./test.txt", "r", encoding="utf-8")
print(type(f))
# 如果不传入参数，会读取全部的内容，传入参数，读取指定长度的内容
# print(f.read(15))
# print(f.read())
# 读取每行内容
lines = f.readlines()
print(type(lines))
for line in lines:
    print(line)
# 关闭文件
f.close()

with open("./test.txt", "r", encoding="utf-8") as f:
    print(f.read())

f = open("./test.txt", "r", encoding="utf-8")
words = f.read().split(" ")
f.close()
count = 0
for word in words:
    if word.__contains__("print"):
        count += 1
print(count)
