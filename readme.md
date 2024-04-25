

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

##### 函数进阶

```python
# 多返回值函数

def get_name_age(name, age):
    """
    获取姓名和年龄的函数

    参数:
    name: 姓名，类型为字符串
    age: 年龄，类型为整数

    返回值:
    返回一个包含姓名和年龄的元组 (name, age)
    """
    return name, age


x, y = get_name_age(age=18, name='小明')
print(x, y)


# 设置默认值在最后,如果不传值，默认值会生效
def get_user_info(name, age, sex='男'):
    """
    获取用户基本信息

    参数:
    name: 用户姓名，字符串类型
    age: 用户年龄，整数类型
    sex: 用户性别，字符串类型，默认为'男'

    返回值:
    返回一个包含用户姓名、年龄和性别的元组
    """

    return name, age, sex


# 参数传入可以修改顺序，指定参数名即可
print(get_user_info(sex='女', age=18, name='小明'))

print(get_user_info(age=18, name='小明'))


# 不定长参数
def get_fix_length_info(*args):
    """
    获取不定长参数的函数

    参数:
    *args: 可变参数列表，类型为元组

    返回值:
    返回一个包含所有参数的元组
    """

    return args


print(get_fix_length_info(1, 2, 3, 4, 5))


# 关键字传入参数
def get_fix_length_info_2(**kwargs):
    """
    获取不定长参数的函数

    参数:
    **kwargs: 可变参数列表，类型为字典

    返回值:
    返回一个包含所有参数的字典
    """

    return kwargs


print(get_fix_length_info_2(name='小明', age=18, sex='男'))


# 传入函数进行运算
def add(a, b):
    """
    实现两个数相加的功能

    参数:
    a -- 第一个加数
    b -- 第二个加数

    返回值:
    两个数的和
    """
    return a + b


def sub(a, b):
    """
    实现两个数相减的功能

    参数:
    a -- 被减数
    b -- 减数

    返回值:
    两个数的差
    """
    return a - b


def operate(a, b, func):
    """
    实现根据指定操作函数对两个数进行操作的功能

    参数:
    a -- 第一个操作数
    b -- 第二个操作数
    func -- 操作函数，接受两个参数并返回结果

    返回值:
    func(a, b)的计算结果
    """
    return func(a, b)


print(operate(1, 2, add))
print(operate(1, 2, sub))

# 匿名函数, lambda
print(operate(6, 2, lambda a, b: a * b))

```



### 4.数据结构

##### 列表

列表可以存储不同类型的数据，可以重复，可以修改。

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

可以当做`Java`的`Map`来理解，就是KV集

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

### 5.IO操作

##### 简单读取

```python
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

# 使用with open会自动关闭文件
with open("./test.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

##### 简单写入

```python
# 写模式，如果文件不存在，会自动创建
f = open('data.txt', 'w',encoding='utf-8')
f.write('hello world2')
# 把内存中的内容写入到磁盘，刷新缓冲区
f.flush()
f.close()

# 追加模式
f = open('data.txt', 'a',encoding='utf-8')
for i in range(1,15):
    f.write('hello world{}\n'.format(i))
f.close()
```

### 6. 异常

程序运行出现意外，会有一些提示信息，可以捕获异常，做一些处理。

```python
# 捕获指定异常,最简单的除数不为0
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
    print('除数不能为0')


# 捕获多个异常
try:
    print(name)
    print(1 / 0)
except (ZeroDivisionError, NameError) as e:
    print('捕获除数为0异常，或者name未定义异常')

# 捕获全部异常
try:
    print(name)
    print(1 / 0)
except Exception as e:
    print('捕获全部异常')
    print(e)
    
# try-except-else-finally
try:
    print(666)
except Exception as e:
    print('出现异常')
else:
    print('没有异常')
finally:
    print('不管有没有异常都会执行')
```

##### 异常传递

```python
def func_1():
    print(1 / 0)


def func_2():
    func_1()


def func_3():
    try:
        func_2()
    except Exception as e:
        print(e)


func_3()
```

### 7.模块

```python
# 导入模块
import time

print(time.time())

# 导入模块别名
import random as rom

print(rom.randint(1, 100))

# 导入模块成员
from random import randint

print(randint(1, 100))

# 导入模块成员别名
from random import randint as rd
print(rd(1, 100))

```

##### 模块导出设置

```python
__all__ = ['add']
# 导入 * 只会导入__all__中的内容 from 自定义模块 import *

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print("我是自定义模块中会被执行的")

if __name__ == '__main__':
    print("我是自定义模块导入不会执行")
```

### 8.包

包导入基本同模块，但是其`__all__`写到包下的`__init.py__`中。

```python
__all__ = ['module1', 'module2']
```

### 9.json使用

```python
import json

data = [
    {"name": "张三", "age": 18, },
    {"name": "李四", "age": 20, },
    {"name": "王五", "age": 22, },
    {"name": "赵六", "age": 24, },
    {"name": "孙七", "age": 26, },
    {"name": "周八", "age": 28, },
    {"name": "吴九", "age": 30, },
    {"name": "郑十", "age": 32, },
    {"name": "王十一", "age": 34, },
    {"name": "赵十二", "age": 36, },

]
# 如果需要中文，需要设置ensure_ascii=False
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

# 准备字典,把字典转换为json字符串
dic = {
    "name": "张三",
    "age": 18,
    "sex": "男",
    "hobby": ["吃饭", "睡觉", "打豆豆"]
}
json_str = json.dumps(dic, ensure_ascii=False)
print(json_str)

# 把字符串转换为列表
data_str = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 20}, {"name": "王五", "age": 22}, {"name": "赵六", "age": 24}, {"name": "孙七", "age": 26}, {"name": "周八", "age": 28}, {"name": "吴九", "age": 30}, {"name": "郑十", "age": 32}, {"name": "王十一", "age": 34}, {"name": "赵十二", "age": 36}]'
data = json.loads(data_str)
print(data)
print(type(data))

# 把字符串转换为字典
dic_str = '{"name": "张三", "age": 18, "sex": "男", "hobby": ["吃饭", "睡觉", "打豆豆"]}'
dic = json.loads(dic_str)
print(dic)
print(type(dic))
```

### 10. 可视化pyecharts

##### 折线图

```python
from pyecharts.charts import Line

# 创建一个线图对象
line = Line()

# 添加x轴数据，代表三个国家的名称
line.add_xaxis(["中国", "美国", "日本"])

# 添加y轴数据，以"GDP"为系列名，[30, 20, 10]为对应三个国家的GDP数据
line.add_yaxis("GDP", [30, 20, 10])

# 渲染并输出图表
line.render()

```

##### 地图

版本不同的时候需要做一下城市名映射。

```python
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

namemap = {'黑龙江省': '黑龙江', '吉林省': '吉林', '辽宁省': '辽宁', '北京市': '北京', '天津市': '天津',
           '河北省': '河北', '山西省': '山西', '内蒙古自治区': '内蒙古', '上海市': '上海', '江苏省': '江苏',
           '山东省': '山东', '浙江省': '浙江', '安徽省': '安徽', '江西省': '江西',
           '福建省': '福建', '广东省': '广东', '澳门特别行政区': '澳门', '台湾省': '台湾', '香港特别行政区': '香港', '西藏自治区': '西藏',
           '广西壮族自治区': '广西', '海南省': '海南', '河南省': '河南', '湖北省': '湖北', '湖南省': '湖南', '陕西省': '陕西', '新疆维吾尔自治区': '新疆',
           '宁夏回族自治区': '宁夏', '甘肃省': '甘肃', '青海省': '青海', '重庆市': '重庆', '四川省': '四川', '贵州省': '贵州', '云南省': '云南'}

data = [
    ("北京市", 100),
    ("天津市", 200),
    ("河北省", 300),
    ("山西省", 400),
    ("内蒙古自治区", 500),
    ("辽宁省", 600),
    ("吉林省", 700),
    ("黑龙江省", 800),
    ("上海市", 900),
    ("江苏省", 1000),
    ("浙江省", 1100),
    ("安徽省", 1200),
    ("福建省", 1300),
    ("江西省", 1400),
    ("山东省", 1500),
    ("河南省", 1600),
    ("湖北省", 1700),
    ("湖南省", 1800),
    ("广东省", 1900),
]
map.add("中国", data, "china")

# map.set_global_opts(
#     title_opts={"title": "中国地图展示"},
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#
#     ),
# )

map.render()

```

##### 柱状图

```python
from pyecharts.charts import Bar
from pyecharts.options import *

bar = Bar()

bar.add_xaxis(['中国', '美国', '日本'])
# bar.add_yaxis('GDP', [25, 20, 10])
bar.add_yaxis('GDP', [25, 20, 10], label_opts=LabelOpts(position='right'))

# 反转坐标轴
bar.reversal_axis()

bar.render()

```

##### 时间柱状图

```python
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

from random import randint


def get_bar_chart():
    bar = Bar()

    bar.add_xaxis(['中国', '美国', '日本'])
    # bar.add_yaxis('GDP', [25, 20, 10])
    bar.add_yaxis('GDP', [randint(10, 100), randint(10, 100), randint(5, 35)], label_opts=LabelOpts(position='right'))

    # 反转坐标轴
    bar.reversal_axis()
    return bar


timeLine = Timeline()

timeLine.add(get_bar_chart(), '点1')
timeLine.add(get_bar_chart(), '点2')
timeLine.add(get_bar_chart(), '点3')
timeLine.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_timeline_show=True,
    is_loop_play=True,
)

timeLine.render('时间线柱状图.html')

```

具体的使用，看着官网文档，自己填充就行。

### 11.面向对象

##### 类与对象

类的基本定义与`Java`没有太大区别，定义成员方法差别也不大。

```python
# 定义类
class Student:
    name = None
    age = None
    gender = None
    address = None
    nation = None

    # 自定义成员方法
    def say_hi(self):
        """
        向大家打招呼并介绍自己。

        方法无需参数，并且没有返回值。
        通过调用实例的属性，自我介绍包括：名字、年龄、地址和民族。
        """
        print('大家好，我是%s，今年%s岁，来自%s，我是%s人。' % (self.name, self.age, self.address, self.nation))

    def say_hi2(self, msg):
        """
        向指定对象Say Hi，并输出消息。

        :param self: 对象自身引用，允许访问对象的属性和方法。
        :param msg: 要输出的消息字符串。
        :return: 无返回值。
        """
        print("{}说:{}".format(self.name, msg))  # 格式化输出对象名称和消息

    # 重写__str__方法
    def __str__(self):
        """
        将对象转换为字符串形式，方便打印或输出。
        现在可以理解为java 的 toString()方法。打印会默认调用

        参数:
        self: 表示对象自身，此处用于访问对象的属性。

        返回值:
        str: 返回一个包含姓名、年龄、性别、地址和民族的字符串。
        """
        return '姓名：%s，年龄：%s，性别：%s，地址：%s，民族：%s' % (self.name, self.age, self.address, self.address, self.nation)


# 创建对象
student = Student()
# 访问修改成员属性
student.name = '张三'
student.age = 18
student.gender = '男'
student.address = '北京'
student.nation = '汉'
print(student)
student.say_hi()
student.say_hi2("你好")
```

##### 构造方法

构造函数也就是创建对象的方法,`__init__`中需要几个参数，也就是需要多少参数的构造。`__gt__`、`__eq__``__lt__``__str__`等重写可以重写操作符和打印信息之类的。

```python
class Person:
    name = None
    age = None
    sex = None

    def __init__(self, name, age, sex):
        """
           Person类的构造函数。

           参数:
           - name: 字符串，表示人的姓名。
           - age: 整数，表示人的年龄。
           - sex: 字符串，表示人的性别。

           返回值:
           - 无
           """
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        """
        将对象转换为字符串表示形式。

        参数:
        - self: 对象自身的引用。

        返回值:
        - 返回一个字符串，包含对象的姓名、年龄和性别信息。
        """
        return f'{self.name} {self.age} {self.sex}'

    def __lt__(self, other):
        """
        重载小于号操作符的方法。

        参数:
        self: 当前对象的实例。
        other: 与当前对象进行比较的另一个对象实例。

        返回值:
        返回一个布尔值，表示当前对象的年龄是否小于另一个对象的年龄。
        """
        return self.age < other.age

    def __gt__(self, other):
        """
        重载大于运算符的方法。

        参数:
        - self: 当前对象的实例。
        - other: 与当前对象进行比较的另一个对象实例。

        返回值:
        - 返回一个布尔值，表示当前对象的年龄是否大于另一个对象的年龄。
        """
        return self.age > other.age

    def __eq__(self, other):
        """
        实现对象的等于比较方法。

        参数:
        - self: 当前对象的实例。
        - other: 与当前对象进行比较的另一个对象实例。

        返回值:
        - 返回一个布尔值，表示当前对象与另一个对象是否在年龄上相等。
        """
        return self.age == other.age


p = Person('张三', 18, '男')
print(p)

p2 = Person('李四', 20, '男')
print(p2)

if p < p2:
    print(f'{p.name} 年龄{p.age}小于 {p2.name} {p2.age}')
else:
    print(f'{p.name} 年龄{p.age}不小于 {p2.name} {p2.age}')

```



##### 封装

封装一些变量，对内部可以访问，对外部无法访问，私有方法`__`前缀开头，私有变量也是`__`开头

```python
class Phone:
    IMEI = None
    producer = None
    # 声明私有变量
    __price = None
    __color = None

    def __init__(self, IMEI, producer, price, color):
        self.IMEI = IMEI
        self.producer = producer
        self.__price = price
        self.__color = color
        self.__pre_test()

    def __pre_test(self):
        """
        执行手机出厂测试的私有方法。

        该方法不需要传入任何参数，也没有返回值。
        主要用于手机生产阶段的出厂质量测试，确保手机各项功能正常。
        """
        print("私有方法。手机出场测试")
        if self.__color == '黑色':
            print("手机颜色为黑色，额外进行测试")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


p = Phone("6565656565656565", "小米", 1000, "黑色")
print(p.IMEI)
print(p.producer)
print(p.get_price())
p.set_price(2000)
print(p.get_price())
print(p.get_color())
p.set_color("白色")
print(p.get_color())
```

##### 多态

定义抽象类，但是不实现，提供一个标准，子类去实现

```python
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('wang wang')


class Cat(Animal):
    def speak(self):
        print('miao miao')


class Bird(Animal):
    def speak(self):
        print('chu chu')


def make_sound(animal):
    animal.speak()


if __name__ == '__main__':
    dog = Dog()
    make_sound(dog)
    cat = Cat()
    make_sound(cat)
    bird = Bird()
    make_sound(bird)
```

### 12.类型注解

为了程序更加规范的开发，和IDE的友好提示，可以对变量添加一些类型提示。

```python
# 类型注解，帮助IDE自动提示和验证代码
from typing import List, Tuple, Dict, Set, Union

my_list: List[int] = [1, 2, 3]
print(my_list)
my_tuple: Tuple[int, str] = (1, 'hello')
print(my_tuple)
my_dict: Dict[str, int] = {'a': 1, 'b': 2}
print(my_dict)
my_set: Set[int] = {1, 2, 3}
print(my_set)


def getMax(arr: List[int]) -> int:
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > res:
            res = arr[i]
    return res


def add(a: int, b: int) -> int:
    """
    两个整数相加

    参数:
    a: int - 第一个整数
    b: int - 第二个整数

    返回值:
    int - 两个整数相加的结果
    """
    return a + b


print(add(1, 2))

print(getMax([1, 2, 3, 4, 5]))


class Student:
    name: str = None
    age: int = None
    gender: str = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


def get_student_info(student: Student) -> str:
    """
    获取学生的信息

    参数:
    student: Student - 学生对象

    返回值:
    str - 学生的信息
    """
    return f'{student.name} {student.age} {student.gender}'


student = Student('张三', 18, '男')
print(get_student_info(student))

# union 类型注解
# 可以同时是int或str类型, 相当于(int | str)
my_list: List[Union[int, str]] = [1, 'hello']
print(my_list)
```

### 13.闭包

闭包也就是作用域封装，不让外部修改变量，内部提供方法。

`nonlocal `关键字声明一个变量不是局部变量，即它不是当前函数内部定义的，而是属于其外部（非全局）作用域中的某个封闭函数。`nonlocal ` 关键字允许在内部函数（嵌套函数）中修改其封闭函数（外部函数）的变量，而不会将该变量视为全局变量。 可以简单理解为函数内部修改外部的变量使用这个。

内部函数内存空间不会释放，会一直占用。

```python
# -*- coding: utf-8 -*-
"""
@File    :   闭包.py
@Time    :   2020/08/03
@author  :   sifan
"""


# 简单闭包
def outer(logo):
    """
    创建一个外部函数，用于封装内部函数。

    参数:
    logo - 字符串类型，表示要打印的标志或标识。

    返回值:
    inner - 内部函数，接受一个消息参数并打印标志和消息。
    """

    def inner(msg):
        """
        创建一个内部函数，用于接收消息并打印。

        参数:
        msg - 字符串类型，表示要打印的消息。
        """
        print(logo, msg)  # 打印传入的标志和消息

    return inner


f = outer('hello')
f('world')


def atm(balance):
    def add(money):
        nonlocal balance
        balance += money
        return balance

    def sub(money):
        nonlocal balance
        if balance >= money:
            balance -= money
            return balance
        else:
            return '余额不足'

    return add, sub


add_money, sub_money = atm(100)
print(add_money(100))
print(sub_money(15646))
```

