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
print(type(get_fix_length_info_2(name='小明', age=18, sex='男')))


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
