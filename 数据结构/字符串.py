msg = ' Hello, Xiao Yue Si Fan'

print(msg[2])
print(msg[-2])

print(msg.index('Xiao'))

# replace 会构造一个新的字符串，原本的字符串不会改变
print(msg.replace('Xiao Yue', '晓月'))
print(msg)

# split 切割字符串得到一个字符串列表
print(msg.split(" "), type(msg.split(" ")[0]))
print(msg)

# strip 去除字符串首尾的空格
print(msg.strip())

# count 统计字符串中某个字符出现的次数
print(msg.count('a'))

# len 统计字符串的长度
print(len(msg))
