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

