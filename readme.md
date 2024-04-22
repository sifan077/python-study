# python学习笔记

### 1.基础语法

1. 字面量：代码中,写下来的固定值;
2. 字符串: 任意数量字符组成；
3. 注释

```python
# 单行注释

"""
多
行
注
释
一般用于方法和程序
"""
```

4. 变量，python变量是可以不用声明类型的，比如`a=5`
5. `type`可以获取变量存储的数据的类型，类似  `type(变量)`
6. 数据类型转换,`str()`,`float()`,`int()`,`bool()`,传入参数，返回结果，高精度转低精度会丢失精度
7. 标识符，命名不能数字开头，只能出现中文、英文、数字、下划线，不能使用关键字，关键字没有必要特别记忆，IDE会提示
8. 运算符，常见的数学运算
9. 字符串，支持单引号，双引号，三引号，字符串格式化需要注意精度。

### 2.流程控制

##### 布尔符

* `True`和`False`,分别代表是与否
* 或: `or`
* 和:`and`
* 非:`not`

##### if 语句

###### 最基本使用

```python
age = int(input("请输入年龄："))

if age >= 18:
    print("成年人")
```

###### else使用

```python
age = int(input("请输入年龄："))

if age >= 18:
    print("成年人需要补票10元")
else:
    print("未成年人不需要补票")
```

###### if-elif -else 判断

```python
score = int(input("请输入成绩："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
```

##### while循环

```python
# 计算1-100的和
i = 1

res = 0
while i <= 100:
    res += i
    i += 1
print(res)
```

```python
# 猜数游戏
import random

num = random.randint(1, 100)
count = 0
flag = True
while flag:
    count += 1
    guess = int(input("请输入一个1-100的整数："))
    if guess == num:
        print("恭喜你猜对了,您猜了{}次".format(count))
        flag = False
    elif guess > num:
        print("猜大了")
    else:
        print("猜小了")
```

```python
# 嵌套 99乘法
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("{}*{}={}\t".format(i, j, i * j),end=" ")
        j += 1
    i += 1
    print()
```

##### for循环

```python
name = 'zhangsan'
for i in name:
    print(i)
```

###### range使用

```python
# range(start,stop,step)
for i in range(1, 10, 2):
    print(i, end=' ')

print()
for i in range(10):
    print(i, end=' ')

print()
for i in range(1, 10):
    print(i, end=' ')
```

```python
# 嵌套九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}\t".format(j, i, j * i),end=" ")
    print()

```

##### continue 和 break

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print()

for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i, end=" ")

```

### 3.面向对象

##### 函数

```python
# 无返回值
def hello():
	print("Hello")
hello()
# 有返回值
def add(a):
    return a + 1

print(add(1))

def get_sums(*nums):
    """
    计算传入参数的总和。
    
    参数:
    *nums - 可变参数，表示要进行求和的所有数字。
    
    返回值:
    res - 整数，表示所有输入数字的和。
    """
    res = 0  # 初始化总和为0
    for num in nums:  # 遍历所有输入的数字
        res += num  # 累加当前数字到总和
    return res  # 返回最终计算得到的总和
get_sums(1, 2, 3, 4, 5)

def get_sums2(name, *nums):
    """
    对给定名称和一组数字求和，并打印求和结果。
    
    参数:
    name: str - 需要进行求和操作的名称。
    *nums: 可变参数，表示要进行求和的数字。
    
    返回值:
    无返回值，该函数仅打印求和结果。
    """
    res = 0  # 初始化求和结果为0
    # 遍历所有传入的数字并求和
    for num in nums:
        res += num
    # 打印求和结果
    print(f'{name}的求和结果是{res}')
get_sums2('Tom', 1, 2, 3, 4, 5)

def test_global_variable():
    """
    测试全局变量的函数。
    
    本函数无参数。
    本函数无返回值。
    """
    global global_num  # 引用全局变量global_num
    global_num = 10  # 设置全局变量global_num的值为10
test_global_variable()
print(global_num)
```

### 4.数据结构

##### 列表

```python
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


# 遍历
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
```

##### 元组

元组是不可变的，可以认为是可读的列表。

```python
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
```

##### 字符串

字符组成的列表,不可以修改，长度只取决于内存。

```python
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

```

##### 序列

```python
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
```

##### 集合

集合是无序且不重复的元素集合,不支持下表访问。

```python
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
```

##### 字典

```python
# 定义空字典
empty_dic1 = {}
print(empty_dic1)
empty_dic2 = dict()
print(empty_dic2)

# 定义一个字典,key value,可以理解为Map集合
dic = {'name': '小明', 'age': 18, 'gender': '男'}
print(dic)

# 如果存在键,则更新值,不存在则添加
dic['age'] = 20
dic['address'] = '北京'
print(dic)

# 删除键
dic.pop("address")
print(dic)

# 获取全部的key
print(dic.keys())

# 获取数量
print(len(dic))

# 遍历字典的key
for key in dic:
    print(f'{key}: {dic[key]}')

for k, v in dic.items():
    print(f'{k}: {v}')

```
