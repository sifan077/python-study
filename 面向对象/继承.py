class Phone:
    """
    手机类，用于表示手机的基本信息。

    参数:
    - brand: 手机品牌，类型为str。
    - price: 手机价格，类型为float或int。
    """

    def __init__(self, brand, price):
        """
        初始化手机类实例。

        参数:
        - brand: 手机品牌，类型为str。
        - price: 手机价格，类型为float或int。
        """
        self.brand = brand  # 手机品牌
        self.price = price  # 手机价格

    def sya_hi(self):
        """
        打印手机品牌和价格。
        """
        print(f'手机品牌是{self.brand}，价格是{self.price}')


# 单继承
class MiPhone(Phone):
    """
    小米手机类，继承自手机类，添加了手机颜色属性。

    参数:
    - brand: 手机品牌，类型为str。
    - price: 手机价格，类型为float或int。
    - color: 手机颜色，类型为str。
    """

    def __init__(self, brand, price, color):
        """
        初始化小米手机类实例。

        参数:
        - brand: 手机品牌，类型为str。
        - price: 手机价格，类型为float或int。
        - color: 手机颜色，类型为str。
        """
        super().__init__(brand, price)  # 调用父类的初始化方法
        self.color = color  # 手机颜色

    def sya_hi(self):
        """
        重写父类的方法。
        此方法打印一条消息，并调用父类的同名方法。

        参数:
        self - 表示实例本身的引用，允许访问类的属性和方法。

        返回值:
        无
        """
        print("重写父类的方法:", end=" ")
        super().sya_hi()  # 调用父类的sya_hi方法

    def say_hi2(self):
        print(f'手机品牌是{self.brand}，价格是{self.price}，颜色是{self.color}')


mp = MiPhone('小米', 1999, '黑色')
mp.sya_hi()
mp.say_hi2()


# 多继承
class NFC:
    nfc = True


# 语法：class 子类名（父类1，父类2，父类3...），多个父类同名属性左侧优先
class NFCPhone(MiPhone, NFC):
    """
    NFC手机类，继承自小米手机类和NFC类，添加了NFC功能。

    参数:
    - brand: 手机品牌，类型为str。
    - price: 手机价格，类型为float或int。
    - color: 手机颜色，类型为str。
    """

    def __init__(self, brand, price, color):
        super().__init__(brand, price, color)
        self.nfc = NFC.nfc


nfc_phone = NFCPhone('小米', 1999, '黑色')
nfc_phone.sya_hi()
nfc_phone.say_hi2()
print(nfc_phone.nfc)
