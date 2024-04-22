arr = [i for i in range(1, 15)]
print(arr)
# 从1到4，步长1
print(arr[1:4])
# 从3开始 到1结束，步长-1
print(arr[3:1:-1])

my_tuple = (1, 2, 3, 4, 5)
# 从头到尾，步长1
print(my_tuple[:])
# 从头到尾，步长-2
print(my_tuple[::-2])

my_str = "abcdefg"
# 从头到尾，步长2
print(my_str[::2])
# 从头到尾，步长-1
print(my_str[::-1])
