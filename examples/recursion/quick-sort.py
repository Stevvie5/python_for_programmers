import math

def getPivot(listOfNums):
	# Perform median of three
	# To determine pivot
	firstPoint = listOfNums[0]
	lastPoint = listOfNums[len(listOfNums)-1]
		
	# Get the median
	medianPointIndex = int((len(listOfNums) + 1)/2)
	medianPoint = listOfNums[medianPointIndex-1]
		
	# Sort the points
	points = [firstPoint, medianPoint, lastPoint]
		
	if points[0] > points[2]:
		points[0], points[2] = points[2], points[0]
		
	if points[0] > points[1]:
		points[0], points[1] = points[1], points[0]
			
	if points[1] > points[2]:
		points[1], points[2] = points[2], points[1]
			
	listOfNums[0] = points[0]
	listOfNums[medianPointIndex-1] = points[1]
	listOfNums[len(listOfNums)-1] = points[2]
		
	return listOfNums

def quicksort(listOfNums):
	if len(listOfNums) <= 1:
		return listOfNums
	elif len(listOfNums) == 2:
		if listOfNums[1] < listOfNums[0]:
			listOfNums[0], listOfNums[1] = listOfNums[1], listOfNums[0]
		return listOfNums
	else:
		listOfNums = getPivot(listOfNums)
		medianPointIndex = int((len(listOfNums) + 1)/2)
		
		# Move the pivot to the end
		listOfNums[medianPointIndex-1], listOfNums[len(listOfNums)-1] = listOfNums[len(listOfNums)-1], listOfNums[medianPointIndex-1]
		
		pivotCopyList = list(listOfNums)
		pivot = pivotCopyList[len(listOfNums)-1]
		
		itemFromLeft = listOfNums[0]
		itemFromLeftIndex = 0
		
		itemFromRight = listOfNums[len(listOfNums)-2]
		itemFromRightIndex = len(listOfNums)-2
		
		while itemFromLeftIndex <= itemFromRightIndex:
			increaseLeft = 1
			decreaseRight = 1
			
			if itemFromLeft > pivot and itemFromRight < pivot:
				listOfNums[itemFromLeftIndex], listOfNums[itemFromRightIndex] = listOfNums[itemFromRightIndex], listOfNums[itemFromLeftIndex]
			elif itemFromRight < pivot:
				decreaseRight = 0
			elif itemFromLeft > pivot:
				increaseLeft = 0
				
			itemFromRightIndex -= decreaseRight
			itemFromLeftIndex+= increaseLeft
			
			itemFromRight = listOfNums[itemFromRightIndex]
			itemFromLeft = listOfNums[itemFromLeftIndex]
			
		listOfNums[itemFromLeftIndex], listOfNums[len(listOfNums)-1] = listOfNums[len(listOfNums)-1], listOfNums[itemFromLeftIndex]
		
		
		firstHalf = listOfNums[0:itemFromLeftIndex]
		secondHalf = listOfNums[itemFromLeftIndex+1:len(listOfNums)]
		return quicksort(firstHalf) + [listOfNums[itemFromLeftIndex]] + quicksort(secondHalf)
		
print(quicksort(["hi", "apple", "tommy", "barab", "goose", "daniel"]))

	