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
		pivot = int(listOfNums[len(listOfNums)-1])
		
		itemFromLeft = listOfNums[0]
		itemFromLeftIndex = 0
		
		itemFromRight = listOfNums[len(listOfNums)-2]
		itemFromRightIndex = len(listOfNums)-2
		
		while itemFromLeftIndex <= itemFromRightIndex:
			if itemFromLeft > pivot and itemFromRight < pivot:
				listOfNums[itemFromLeftIndex], listOfNums[itemFromRightIndex] = listOfNums[itemFromRightIndex], listOfNums[itemFromLeftIndex]
				
				itemFromRightIndex -= 1
				itemFromRight = listOfNums[itemFromRightIndex]
				
				itemFromLeftIndex+=1
				itemFromLeft = listOfNums[itemFromLeftIndex]			
			elif itemFromRight < pivot:
				itemFromLeftIndex+=1
				itemFromLeft = listOfNums[itemFromLeftIndex]
			elif itemFromLeft > pivot:
				itemFromRightIndex -= 1
				itemFromRight = listOfNums[itemFromRightIndex]
			else:
				itemFromRightIndex -= 1
				itemFromRight = listOfNums[itemFromRightIndex]
				
				itemFromLeftIndex+=1
				itemFromLeft = listOfNums[itemFromLeftIndex]

		listOfNums[itemFromLeftIndex], listOfNums[len(listOfNums)-1] = listOfNums[len(listOfNums)-1], listOfNums[itemFromLeftIndex]
		
		
		firstHalf = listOfNums[0:itemFromLeftIndex]
		secondHalf = listOfNums[itemFromLeftIndex+1:len(listOfNums)]
		return quicksort(firstHalf) + [listOfNums[itemFromLeftIndex]] + quicksort(secondHalf)

print(quicksort([69,24,6,3,20,4,55,5,1,32]))

	