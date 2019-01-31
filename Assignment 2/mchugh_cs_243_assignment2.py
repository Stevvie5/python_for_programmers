# Thomas McHugh
# CS 243 Assignment 2

def nameSearch(userName, letter):
    'Returns the number of times a letter is present in a name'
    # Convert both strings to all lower case so it can be compared
    userNameLower = userName.lower()
    letterLower = letter.lower()

    # Returns count of letter in name
    letterInNameCount = userNameLower.count(letterLower)
    return letterInNameCount

def fileStringSearch(fileName, text):
    'Checks if a string of text is present in a text file'
    # Check if string of text is too small for the problem
    # If it is return -1
    if len(text) < 3:
        return -1
    else:
        # Read file and get whole document in a string
        fileInput = open(fileName, 'r')
        fileText = fileInput.read()
        fileInput.close()

        # Convert to lower so strings can be compared
        fileTextLower = fileText.lower()
        textLower = text.lower()

        # Check if string of text is in the document's text
        isTextInFileText = textLower in fileTextLower
        return isTextInFileText

def problem3(year, month, day, location = 'A'):
    'Problem #3: returns the proper representation of a date depending on location'
    # Convert location to uppercase so as to remove any accidental lowercase values
    location = location.upper()
    
    # Location should either represent default value, A, or N, otherwise function will return -1
    if location == 'A':
        # Location is America so return the properly formatted string
        dateStringAmerica = 'The years is: {0}. The day is: {1}/{2}.'.format(year, month, day)
        return dateStringAmerica
    elif location == 'N':
        # Location is not America so return the properly formatted string
        dateStringInternational = 'The years is: {0}.  The day is: {2}/{1}.'.format(year, month, day)
        return dateStringInternational
    else:
        # Location entered is not supported
        return -1

def problem4():
    'Problem #4'
    # Determine file name and get entire file text as a string
    csvFileTitle = 'exam_grades.csv'

    fileInput = open(csvFileTitle, 'r')
    gradesText = fileInput.read()
    fileInput.close()

    # Split text by commas into an array
    strGradeList = gradesText.split(",")

    # Cast array of strings into an array of ints
    intGradeList = []
    for grade in strGradeList:
        intGrade = eval(grade)
        intGradeList.append(intGrade)
    
    # Calculate mean of newly casted array
    gradeListSum = sum(intGradeList)
    gradeListLength = len(intGradeList)
    gradeListAverage = gradeListSum/gradeListLength

    return gradeListAverage