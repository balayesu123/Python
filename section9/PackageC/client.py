# import sys
# sys.path.append("D:/Python/PycharmProject/pythonProject/section9/packageA")
# sys.path.append("D:/Python/PycharmProject/pythonProject/section9/packageB")
#
# import emp
# eobj = emp.Employee(123,"bala",50000)
# eobj.display()
#
# import stu
# sobj = stu.Student(123,"bala",'A')
# sobj.display()

#Approach2:

import sys
sys.path.append("D:/Python/PycharmProject/pythonProject/section9/packageA")
sys.path.append("D:/Python/PycharmProject/pythonProject/section9/packageB")

from emp import *
eobj = Employee(123,"bala",50000)
eobj.display()

from stu import *
sobj = Student(123,"bala",'A')
sobj.display()