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
