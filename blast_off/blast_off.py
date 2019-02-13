def blastOff(num):
	if num == 0:
		print("Blast Off!")
	else:
		print(num)
		blastOff(num-1)
		
blastOff(10)