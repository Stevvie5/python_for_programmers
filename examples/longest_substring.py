s1 = "ABAZDC"
s2 = "BACBAD"

def subsequence(firstSub, secondSub):
	subsequences = []
	for i in range(len(firstSub)):
		firstSubChar = firstSub[i]
		
		for b in range(len(secondSub)):
			secondSubChar = secondSubChar[b]
			if firstSubChar == secondSubChar:
				subsequences.append()
		