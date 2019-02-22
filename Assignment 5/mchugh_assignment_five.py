# Thomas McHugh
# CSC 243
# Assignment 5

def createStudentDictionary():
	'Returns a dictionary with '
	# Open and read the file lines
	classRosterFileInput = open('class_roster.txt', 'r')
	classRosterLines = classRosterFileInput.readlines()
	classRosterFileInput.close()
	
	classRoster = {}
	
	for rosterItem in classRosterLines:
		# Remove the new line item
		seperatedByNewLineItem = rosterItem.split('\n')
	
		# For each line split values into an array
		studentInfoList = seperatedByNewLineItem[0].split(',')
		
		# Get the info for the student
		studentFirstName = studentInfoList[0]
		studentLastName = studentInfoList[1]
		studentId = studentInfoList[2]
		studentClass = studentInfoList[3]
		
		# Store student info in tuple
		studentInfo = (studentFirstName, studentLastName, studentClass)
		
		# Store tuple by student id in classRoster
		classRoster[studentId] = studentInfo
	return classRoster

def studentSearch(classRoster, studentId):
	try:
		student = classRoster[studentId]
		
		studentFirstName = student[0]
		studentLastName = student[1]
		studentClass = student[2]
		
		studentString = 'First Name: {0}\nLast Name: {1}\nYear: {2}'.format(studentFirstName, studentLastName, studentClass)
		return studentString
	except KeyError:
		return 'No student found with ID: {0}'.format(studentId)
	except:
		return 'An unexpected error occured.'
		