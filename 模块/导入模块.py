# 导入模块
import time

print(time.time())

# 导入模块别名
import random as rom

print(rom.randint(1, 100))

# 导入模块成员
from random import randint

print(randint(1, 100))

# 导入模块成员别名
from random import randint as rd
print(rd(1, 100))
