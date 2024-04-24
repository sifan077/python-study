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
