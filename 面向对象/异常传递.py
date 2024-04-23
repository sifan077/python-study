def func_1():
    print(1 / 0)


def func_2():
    func_1()


def func_3():
    try:
        func_2()
    except Exception as e:
        print(e)


func_3()
