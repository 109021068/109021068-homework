class Student:
    def __init__(self, name, id, gender, department, clas):
        self.studName = name
        self.studId = id
        self.studGender = gender
        self.studDepartment = department
        self.studClas = clas
    def showInfo(self):
        print(self.studName)
        print(self.studId)
        print(self.studGender)
        print(self.studDepartment)
        print(self.studClas)
x = Student("林宜孜","109021068","女","資工系","B班")
x1 = Student("方秋雅","109021008","女","資工系","B班")
x2 = Student("陳聖瑋","109021494","男","資工系","B班")
x.showInfo()
x1.showInfo()
x2.showInfo()