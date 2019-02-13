def handshake(numOfPeople):
	if numOfPeople > 1:
		totalShakes = numOfPeople - 1
		return totalShakes + handshake(numOfPeople - 1)
	else:
		return 0
		
print(handshake(5))