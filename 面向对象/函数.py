def hello(name):
    print("Hello,{}".format(name))


hello("Tom")
hello("Jerry")


def add(a):
    return a + 1


print(add(1))


def say_hi():
    print("Hi")


def get_sum(a, b):
    return a + b


print(get_sum(1, 2))


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


print(get_sums(1, 2, 3, 4, 5))


def get_sums2(name, *nums):
    res = 0
    for num in nums:
        res += num
    print(f'{name}的求和结果是{res}')


get_sums2('Tom', 1, 2, 3, 4, 5)


def func_a():
    print("1")


def func_b():
    print("2")
    func_a()
    print("3")


func_b()


def test_global_variable():
    global global_num
    global_num = 10


test_global_variable()
print(global_num)
