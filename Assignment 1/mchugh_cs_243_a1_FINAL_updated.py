# Thomas McHugh
# CS 243 Assignment 1
import math

# Problem 1
# Write a function that accepts 2 lists of numbers, and adds the lowest number from each list, and returns the sum.
def addTwoLowest(firstList, secondList):
    'Adds together the lowest number from two lists'
    # Retrieve minimum values from each list
    firstListMin = min(firstList)
    secondListMin = min(secondList)

    return firstListMin + secondListMin

# Problem 2
# Write a function that accepts 2 lists of numbers, and returns the average of the last number in each list.
def averageLastTwo(firstList, secondList):
    'Finds the average of the last number from two lists'
    # Retrieve last number from each list
    firstListLastNum = firstList[-1]
    secondListLastNum = secondList[-1]

    # Calculate average of nums
    return (firstListLastNum + secondListLastNum) / 2

# Problem 3
# Write a function that accepts two arguments, and treats them as the two non-hypoteneuse sides of a right-angle triangle.
def calcHypoteneuse(firstNum, secondNum):
    'Finds the hypoteneuse from two non-hypoteneuse sides of a right-angle triangle'
    # Calculate the square of first num and second num
    firstNumSquared = firstNum ** 2
    secondNumSquared = secondNum ** 2

    # Get the sum of the squared nums
    hypotenuseSquared = firstNumSquared + secondNumSquared
    # Square root the hypotenuse squared to get the hypotenuse
    return math.sqrt(hypotenuseSquared)

# Problem 4
# Create an empty list.
# Then you will ask the user to enter 3 numbers. 
# Ask for them one at a time, and enter each into the list. 
# Recall that there is a function to add items into a list.
def problem4():
    'Problem #4'
    userInputNums = []

    firstNumInput = eval(input("Enter the 1st number: "))
    secondNumInput = eval(input("Enter the 2nd number: "))
    thirdNumInput = eval(input("Enter the 3rd number: "))

    userInputNums.append(firstNumInput)
    userInputNums.append(secondNumInput)
    userInputNums.append(thirdNumInput)

    userInputNumsHighest = max(userInputNums)
    userInputNumsLowest = min(userInputNums)

    userInputNumsAverage = sum(userInputNums) / len(userInputNums)
    # Round userInputNumsAverage to one decimal place
    userInputNumsAverage = round(userInputNumsAverage, 1)
    
    print("The highest number is:", userInputNumsHighest)
    print("The lowest number is:", userInputNumsLowest)
    print("The average is:", userInputNumsAverage)

# Problem 5
# Write a function that accepts a list of strings and returns a single string that is a concatenation of the entire list.
def makeBigString(stringList):
    'Concatenates every string from a list of strings'
    concatenatedString = ""
    for string in stringList:
        concatenatedString = concatenatedString + string
    return concatenatedString

problem4()