# 装饰器使用
# 我觉得可以当做拦截器理解，做一些功能增强

def aop(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


@aop
def test():
    print("test")


test()
