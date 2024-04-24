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
