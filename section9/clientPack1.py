#Approach1:
# import sys
# sys.path.append("D:/Python/PycharmProject/pythonProject/section9/pack1")
# sys.path.append("D:/Python/PycharmProject/pythonProject/section9/pack1/pack2")
#
# import module1
# import module2
#
# module1.display()
# module2.show()

#Approach2:
import sys
sys.path.append("D:/Python/PycharmProject/pythonProject/section9/pack1")
sys.path.append("D:/Python/PycharmProject/pythonProject/section9/pack1/pack2")

from module1 import *
from module2 import *

display()
show()

# output
# This is display function from module1
# This is show function from module2