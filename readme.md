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

