import math

def isPalindrome(text):
	# Basic find palindrome
	textLength = len(text)
	
	firstHalfStart = 0
	firstHalfEnd = (textLength/2) + 1
	
	secondHalfStart = textLength/2
	secondHalfEnd = textLength
	
	if textLength % 2 != 0:
		middleCharacter = int(math.floor(firstHalfEnd)) - 1
		
		firstHalfEnd = middleCharacter + 1
		secondHalfStart = middleCharacter
	else:
		firstHalfEnd = int(firstHalfEnd) - 1
		secondHalfStart = int(secondHalfStart)
		
	firstHalfText = text[firstHalfStart : firstHalfEnd]
	secondHalfText = text[secondHalfStart : secondHalfEnd]
	
	# Reverse second half
	secondHalfReversed = ''
	for i in range(len(secondHalfText)):
		i = (i*-1) - 1
		secondHalfReversed += secondHalfText[i]
		
	# Check for equal
	if firstHalfText == secondHalfReversed:
		return True
		
	return False

#def possiblePalindromes(text):
	