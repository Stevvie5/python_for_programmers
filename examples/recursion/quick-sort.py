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
		
		pivot = listOfNums[len(listOfNums)-1]
		
		itemFromLeftIndex = 0
		itemFromRightIndex = len(listOfNums)-2

		while itemFromLeftIndex <= itemFromRightIndex:
			itemFromLeft = listOfNums[]
		
		firstHalf = listOfNums[0:itemFromLeftIndex]
		secondHalf = listOfNums[itemFromLeftIndex+1:len(listOfNums)]
		return quicksort(firstHalf) + [listOfNums[itemFromLeftIndex]] + quicksort(secondHalf)
		
print(quicksort([4,7,10,2,3, 50, 1, 23,30,67,82,35]))

	