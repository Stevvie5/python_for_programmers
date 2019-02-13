def blastOff(num):
	if num < 0:
		return -1
	elif num == 0:
		return "Blastoff!"
	else:
		print(num)
		return blastOff(num-1)
		
print(blastOff(10))