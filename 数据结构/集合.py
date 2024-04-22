# 定义集合,集合是无序且不重复的元素集合,不支持下表访问
s = {1, 2, 3, 4, 5, 5}
print(s)

s_empty = set()
print(s_empty)

# 添加元素
s_empty.add("python")
s_empty.add("python")
s_empty.add("java")
s_empty.add("go")
print(s_empty)

# 删除元素,如果元素不存在,会报错
s_empty.remove("python")
print(s_empty)

# 随机删除元素
print(s_empty.pop())
print(s_empty)

# 清空集合
s_empty.clear()
print(s_empty)

# 集合运算,得到s1有的但s2没有的元素
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.difference(s2))

# 得到s1和s2的并集
print(s1.union(s2))

# 得到s1和s2的交集
print(s1.intersection(s2))

# 得到集合中的个数
print(len(s1))

# 遍历集合
for i in s1:
    print(i, end=" ")
print()

while len(s1) != 0:
    print(s1.pop(), end=" ")
