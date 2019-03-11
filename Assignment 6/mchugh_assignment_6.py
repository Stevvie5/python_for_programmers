# Thomas McHugh
# Assignment 6
# CSC 243

class Student(object):
	'A class to hold information regarding students in a class and their grade.'
	# Create instance variable for name
	# Create getter and setter methods for name
	def setName(self, inputName):
		'Set the name of the student'
		self.name = inputName
	
	def getName(self):
		'Get the name of the student'
		return self.name
		
	# Create instance variable for percentGrade
	# Create getter and setter methods for percentGrade
	def setPercentGrade(self, inputGradeAsPercent):
		'Set the grade of the student as a percentage out of 100%'
		self.percentGrade = inputGradeAsPercent
		
	def getPercentGrade(self):
		'Get the grade of the student as a percentage out of 100%'
		return self.percentGrade
		
	# Create instance variable for letterGrade
	# Create getter and setter methods for letterGrade
	def calcLetterGrade(self):
		'Calculate the letter grade of the student'
		if self.percentGrade >= 90:
			self.letterGrade = 'A'
		elif self.percentGrade >= 80:
			self.letterGrade = 'B'
		elif self.percentGrade >= 70:
			self.letterGrade = 'C'
		elif self.percentGrade >= 60:
			self.letterGrade = 'D'
		else:
			self.letterGrade = 'F'
			
	def getLetterGrade(self):
		'Get the student grade as a letter'
		return self.letterGrade
		
	def addBonus(self, bonusPercent):
		'Adds bonus points to grade based on percentage'
		# Convert percentage to fraction out of 100
		# Multiply by percentGrade to retrieve bonus points
		bonusPointsRatio = bonusPercent/100
		bonusPoints = bonusPointsRatio*self.percentGrade
		
		# Add bonus points to percent grade
		self.percentGrade += bonusPoints
	
	def printStudentInfo(self):
		'Returns the information about the student'
		try:
			return 'Name: {0}\nPercent Grade: {1}\nLetter Grade: {2}'.format(self.name, self.percentGrade, self.letterGrade)
		except:
			return 'Error. Some information for the student has not yet been set.'
		
	def __str__(self):
		return self.printStudentInfo()