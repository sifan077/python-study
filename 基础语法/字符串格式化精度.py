price = 19.8564
# 全部小数
msg = '商品单价为%f元' % price
print(msg)
#  小数点后两位
msg = '商品单价为%.2f元' % price
print(msg)
#  宽度12 位小数2位
msg = '商品单价为%12.2f元' % price
print(msg)

# 格式化 f 'xxx{变量名 or 表达式}xxx'
name = '小明'
age = 18.564
msg = f'我是{name}，今年{age}岁'
print(msg)

print(f"2*5={2 * 5}")
