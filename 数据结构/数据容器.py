# 声明一个列表字面量
[1, "3", "a", "d"]
# 创建一个嵌套列表
q = [[1, 3, 5], [], 123]

# 获取嵌套列表内容
print(type(q), type(q[0]))
print(q[0][1])
# 创建一个列表
arr = [1, 2, 3, 4, 5, "a", "qqq"]
print(arr)
print(type(arr))

# 通过索引访问列表元素
print(arr[0])

# 倒序索引去除
print(arr[-1])

brr = [1, 2, 3, 4, 5, "a", "qqq"]
# 删除第2个元素
brr.pop(1)
print(brr)

# 在指定位置插入元素
brr.insert(2, 66544)
print(brr)

# 查找元素
print(brr.index(3))
# 添加一个元素
brr.append(6)
print(brr)
# 添加多个元素
brr.extend([7, 8, [9, 10]])
print(brr)
# 删除最后一个元素
brr.pop()
print(brr)
# 删除指定索引的元素
brr.pop(0)
print(brr)
# 删除指定元素
brr.remove(3)
print(brr)

brr = [1, 2, 3, 4, 5, "a", "qqq"]
index = 0
while index < len(brr):
    print(brr[index], end=" ")
    index += 1
print()
for item in brr:
    print(item, end=" ")
print()
for i in range(0, len(brr)):
    print(brr[i], end=" ")
