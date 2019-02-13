import math

def isPalindrome(text):
	firstCharacter = text[0]
	lastCharacter = text[len(text) - 1]
	if len(text) == 1:
		return True
	elif firstCharacter == lastCharacter:
		if len(text) - 2 > 0: 
			return isPalindrome(text[1 : len(text) - 1])
		else:
			if text[0] == text[1]:
				return True
			else:
				return False
	else:
		return False
		
def getPalindromesBySize(text, size):
	sizeText = ''
	palindromeCount = 0
	
	skipNext = False
	skipped = 0
	
	for i in range(len(text)):
		if skipNext == False:
			sizeText += text[i]
			if i+size <= len(text):
				subText = text[i : i+size]

				if isPalindrome(subText.lower()) == True:
					sizeText += subText[1 : len(subText)] + ' '
					palindromeCount += 1
					
					if size > 1:
						skipNext = True
				else:
					sizeText += ' '
			else:
				sizeText += ' '
		else:
			skipped += 1
			if skipped == size-1:
				skipNext = False
	return sizeText, palindromeCount
	
def allPalindromes(text):
	searchSizes = range(1, len(text)+1)
	for searchSize in searchSizes:
		palindromes, palindromeCount = getPalindromesBySize(text, searchSize)
		if palindromeCount > 0:
			print(palindromes)

print(isPalindrome('need'))
		