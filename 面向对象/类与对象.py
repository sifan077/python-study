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
