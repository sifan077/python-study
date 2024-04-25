import threading
import time


def sing(msg):
    while True:
        print("唱歌,{}\n".format(msg))
        time.sleep(1)


def dance(msg):
    while True:
        print("跳舞,{}\n".format(msg))
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing, args=("happy",),name="singThread")
    t2 = threading.Thread(target=dance, kwargs={"msg": "crazy"},name="danceThread")
    t1.start()
    t2.start()
