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