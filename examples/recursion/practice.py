def revVert(n):
	if n < 10:
		print(n)
	else:
		print(n%10)
		revVert(n//10)

def printLst(lst):
	if len(lst) == 0:
		# Print New Line 
		print()
	else:
		print(lst[0])
		if len(lst) != 1:
			printLst(lst[1:len(lst)])

def cheer(num):
	if num == 1:
		print('Hurrah', end=' ')
	elif num <= 0:
		print('Erro: Enter a positive number')
	else:
		print('Hip', end=' ')
		cheer(num-1)
def pattern(num):
	if num == 1:
		print(num, end=' ')
	else:
		pattern(num-1)
		print(num, end=" ")
		pattern(num-1)
pattern(5)