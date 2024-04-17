# 数字转为字符串
num = str(123)
print(type(num), num)

# 字符串转为数字
num = int('123')
print(type(num), num)

# 字符串转为浮点数
num = float('123.456')
print(type(num), num)

# 浮点数转换为字符串
num = str(123.456)
print(type(num), num)

# 布尔转换为数字
num = int(True)
print(type(num), num)

# 数字转换为布尔，如果为0，则为False，如果不为0，则为True
print(bool(0), bool(3241.41))
num = bool(1)
print(type(num), num)
