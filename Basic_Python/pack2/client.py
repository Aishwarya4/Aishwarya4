#packages contains diiffrent modules
from Basic_Python.pack1  import module1,module2
# from Basic_Python.StudentPackage.stud import module3
#Approach1
module1.display()
print("Sum :",module1.sum(34,67))
print("Average:",module1.average(23,56))
print("Power :",module1.power(3,3))
module2.show()
# module3.show()


from Basic_Python.EmpPackage.emp import Employee
e = Employee(101,'Aishwarya',200000)
e.displayemp()

from Basic_Python.StudentPackage.stud import Student
s = Student(1,'Damini','A')
s.displaystud()
