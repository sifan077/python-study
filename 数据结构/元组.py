# 定义一个元组
t = (1, 2, 3, 4, 5)
print(t)
print(t[3])

# 元组不可改变。可以认为是可读的列表。

print(((1, 4), 2, (3, 5)).index(2))

print((1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1).count(1))

print((1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1).__len__())

t = (1, 2, 3, 4, 5)
# 遍历
for i in t:
    print(i, end=" ")
print()

for i in range(len(t)):
    print(t[i], end=" ")

print()
index = 0
while index < len(t):
    print(t[index], end=" ")
    index += 1
