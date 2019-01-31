# Thomas McHugh
# CSC 243 Assignment 3

def listOfWordsInFile(fileName, letter):
    'Returns a list containing all of the words in a file that contain a specific letter'
    # Check if letter is not a letter
    if len(letter) > 1:
        # Returns -1 if letter is longer than just a single character
        return -1
    else:
        # Read text of the file as lines
        fileInput = open(fileName, 'r')
        fileTextLines = fileInput.readlines()
        fileInput.close()

        # Get words from list of text in lines
        # Using this method in case two words is connected by a new line
        wordsList = []
        for textLine in fileTextLines:
            wordsList += textLine.split(" ")

        # Loop through words list
        containsLetterList = []
        for word in wordsList:
            # Make the word lower case 
            # To compare with the lower case version of letter
            lowercaseWord = word.lower()
            if letter.lower() in lowercaseWord:
                # Remove the new line part of the word if it contains one
                wordWithoutNewLine = word.split("\n")
                containsLetterList.append(wordWithoutNewLine[0])
        return containsLetterList
'''
Pseudocode for problem #1
1. Make sure the letter submitted is not a word, number, etc. 
2. If it is not a letter, return -1
3. If it is actually a letter read the file and get an list of its text for each line
4. Recurse through the lines of text. Seperate each line into words and add it to a list of words
5. Recurse through the words
6. Check if the word contains the letter
7. If it does add to a list of words that contain the list 
8. Return the list of words
'''

def convertCase(iFileName, oFileName):
    'Converts all upper case letters to lower case, and all lower case letters to upper case letters in an input file. Outputs the result to a file'
    # Get the text of the input file
    fileInput = open(iFileName, 'r')
    fileInputText = fileInput.read()
    fileInput.close()

    # Define string where the reverse case text will go
    reverseCaseText = ''

    # Loop through every character
    ## Reverse the case and add the character to the reverse case text
    for i in range(len(fileInputText)):
        character = fileInputText[i]
        if character.isupper():
            reverseCaseText += character.lower()
        else:
            reverseCaseText += character.upper()
    
    # Write the newly created string to the output file
    fileOutput = open(oFileName, 'w')
    fileOutput.write(reverseCaseText)
    fileOutput.close()
'''
Pseudocode for problem #2
1. Retrieve the text for a file as a single string
2. Loop through each character in the string
3. If the character is upper add it to a new string as a lower case character
4. If the character is lower add it to a new string as an upper case character
5. Open the output file and write the new string to it
'''

def highestLowestGrades():
    'Reads in the contents of a csv file of grades. Prints out the highest and lowest grades in the file.'
    fileName = 'exam_grades.csv'
    # Open the file and read the text of the file
    fileInput = open(fileName, 'r')
    fileText = fileInput.read()
    fileInput.close()

    # Get the individuals grades by splitting the text by commas
    gradeList = fileText.split(",")
    gradeListInt = []

    # Loop through every value and convert to int
    for i in range(len(gradeList)):
        gradeAsInt = int(gradeList[i])
        gradeListInt.append(gradeAsInt)
    
    minValue = min(gradeListInt)
    maxValue = max(gradeListInt)

    print("The highest grade is {0} and the lowest grade is {1}".format(maxValue, minValue))
'''
Pseudocode for problem #3
1. Read in as a string the exam_grades.csv file
2. Split the grades into a list by comma
3. Loop through the grade list and cast to ints
4. Get the min and max of the list
7. Print out the highest and lowest grades
'''