print("学IT就到" + "黑马程序员")

name = "黑马程序员"
action = "学IT就到"
print(action + name)

print("学IT就到" + name + "黑马程序员")

# 拼接数字别的类型，需要先转换成字符串
tel = 16512341563
print("我的电话是" + str(tel))

# format 格式化字符串,我还是喜欢这种格式
tel = 16512341563
print("我的电话是{}".format(tel))
# 占位符拼接
tel = 16512341563
address = "河南"
msg = "我的电话是%s,地址是%s" % (tel, address)
print(msg)
