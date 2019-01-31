# Thomas McHugh
# CSC 243 Assignment 4

def getChoice():
    'Asks user to choose an option from a menu and returns the choice'
    # Print option menu
    print('What would you like to search for?')
    optionMenu = ['Press 1 for the lowest grade.', 'Press 2 for the highest grade.', 'Press 3 for the average grade.', 'Press 4 to search for a grade.']
    for option in optionMenu:
        print(option)

    numOfOptions = len(optionMenu)

    # Repeat asking for input until the user provides a correct option
    while True:
        # Retrieve input from user
        txtUserChoice = input('Enter a choice: ')
        # Cast to int
        try:
            intUserChoice = int(txtUserChoice)

            # Check if this is an option
            if intUserChoice >= 1 and intUserChoice <= numOfOptions:
                return intUserChoice
        except:
            # The user did not enter an appropriate type of input
            errorAlert = 'Enter your choice using the digits 1-{0}.'.format(numOfOptions)
            print(errorAlert)

def getFileAsString(fileName):
    'Returns the string of a text file'
    # Read in contents of file
    # Extra fun: make sure the file exists
    # If the file was not or was not found in the directory
    ## Ask for a new file
    while True:
        try:
            fileInput = open(fileName, 'r')
            fileText = fileInput.read()
            fileInput.close()
            return fileText
        except:
            print('The file to examine was not found.')
            fileName = input('Please enter a new file to examine: ')

            
def checkGrades():
    'Checks different options a user chooses for a csv file of grades'
    # Ask the user for their selection for an option
    userSelection = getChoice()

    # Read in contents of exam_grades.csv
    fileName = 'exam_grades.csv'
    fileText = getFileAsString(fileName)

    # Convert to list of ints from exam grades
    txtGradeList = fileText.split(",")
    # Cast text list to list of ints
    intGradeList = []
    for grade in txtGradeList:
        intGrade = int(grade)
        intGradeList.append(intGrade)

    if userSelection == 1:
        # Get the lowest grade
        minGrade = min(intGradeList)

        returnText = 'The lowest grade is {0}.'.format(minGrade)
        print(returnText)
    elif userSelection == 2:
        # Get the highest grade
        maxGrade = max(intGradeList)

        returnText = 'The highest grade is {0}.'.format(maxGrade)
        print(returnText)
    elif userSelection == 3:
        # Get the average grade
        sumGradeList = sum(intGradeList)
        lenGradeList = len(intGradeList)
        avgGrade = sumGradeList/lenGradeList

        # Round the average grade to one decimal point
        avgGrade = round(avgGrade, 1)

        returnText = 'The average grade is {0}.'.format(avgGrade)
        print(returnText)
    elif userSelection == 4:
        # Search for a grade
        ## No need for else statement because infinite loop run until option is 1-4
        # Ask user for a number to search for
        print()
        searchNum = input('Enter a number to search for: ')
        intSearchNum = int(searchNum)

        # Check if the search number was present in the grade list
        numPresent = intSearchNum in intGradeList

        # Return the proper text to the user depending on if the number was in the list
        returnText = ''
        if numPresent == True:
            returnText = 'The grade {0} was present.'.format(intSearchNum)
        else:
            returnText = 'The grade {0} was NOT present.'.format(intSearchNum)
        print(returnText)