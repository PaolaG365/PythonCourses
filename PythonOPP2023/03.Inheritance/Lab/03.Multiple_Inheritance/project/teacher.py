from employee import Employee
from person import Person


class Teacher(Employee, Person):
    @staticmethod
    def teach():
        return "teaching..."


teacher1 = Teacher()
print(teacher1.teach())
print(teacher1.sleep())
print(teacher1.get_fired())
