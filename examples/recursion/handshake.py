# Thomas McHugh
# Handshake example

def handshake(numOfPeople):
	'In a party of N people, each person will shake her/his hand with each other person only once. Will return total number of hand-shakes that would happen.'
	if numOfPeople > 1:
		# Total shakes are the number of people minus the individual shaking
		totalShakes = numOfPeople - 1
		# Return the sum of shakes recursively
		return totalShakes + handshake(numOfPeople - 1)
	else:
		# One person remaining
		## Nobody to shake hand
		return 0
		
print(handshake(5))