__all__ = ['add']
# 导入 * 只会导入__all__中的内容 from 自定义模块 import *

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print("我是自定义模块中会被执行的")

if __name__ == '__main__':
    print("我是自定义模块导入不会执行")
