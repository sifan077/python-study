import my_package.module1
import my_package.module2

my_package.module1.info1()
my_package.module2.info2()

from my_package import module1
from my_package import module2

module1.info1()
module2.info2()

from my_package.module1 import info1
from my_package.module2 import info2

info1()
info2()

from my_package import *
# 访问不到module3

from my_package import module3

module3.info3()
