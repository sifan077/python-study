# 捕获指定异常,最简单的除数不为0
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
    print('除数不能为0')

# 捕获多个异常
try:
    print(name)
    print(1 / 0)
except (ZeroDivisionError, NameError) as e:
    print('捕获除数为0异常，或者name未定义异常')

# 捕获全部异常
try:
    print(name)
    print(1 / 0)
except Exception as e:
    print('捕获全部异常')
    print(e)

# try-except-else-finally
try:
    print(666)
except Exception as e:
    print('出现异常')
else:
    print('没有异常')
finally:
    print('不管有没有异常都会执行')
