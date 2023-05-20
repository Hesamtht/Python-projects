class person:
    def __init__(self , name , family , age , address):
        self.name = name
        self.family = family
        self.age = age
        self.address = address
#==============================================================
class student(person):
    def __init__(self, name, family, age, address , studentID):
        super().__init__(name, family, age, address)
        self.studentID = studentID
    def __str__(self):
        return self.name + ' ' + self.family + ' ' + self.age + ' ' + self.address + ' ' + str(self.studentID)  #to " " bezari niaz nis str type koni
    def showinfo(self):
        print(self)
#==============================================================
class teacher(person):
    def __init__(self, name, family, age, address , teacherID):
        super().__init__(name, family, age, address)
        self.teacherID = teacherID
    def __str__(self):
        return self.name + ' ' + self.family + ' ' + self.age + ' ' + self.address + ' ' + str(self.teacherID)
    def showinfo(self):
        print(self)
#==============================================================
class employee(person):
    def __init__(self, name, family, age, address , employeenum):
        super().__init__(name, family, age, address)
        self.employeenum = employeenum
    def __str__(self):
        return self.name + ' ' + self.family + ' ' + self.age + ' ' + self.address + ' ' + str(self.employeenum)
###############################################################################
stu1 = student("Hesam" , "Mozafari" , "20" , "iran" , 12345678)
tea1 = teacher("Ahmad" , "Ghasemi" , "113" , "iran" , 6548)
print(stu1) #ya mitonim az line 37 oun tabeii ro ke to class student neveshtim use konim

student.showinfo(stu1)


teacher.showinfo(tea1)