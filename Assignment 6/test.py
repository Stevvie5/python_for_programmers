from mchugh_assignment_6 import Student

s1 = Student()
s1.setName('Lisa Jackson')
s1.setPercentGrade(72)
s1.calcLetterGrade()

print(s1.getLetterGrade())

s1.addBonus(20)
print(s1.getPercentGrade())
s1.calcLetterGrade()
print(s1.getLetterGrade())

print()
print(s1.printStudentInfo())