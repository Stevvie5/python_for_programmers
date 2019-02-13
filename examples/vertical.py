def vertical(num):
	if num < 10:
		print(num)
	else:
		print(num%10)
		vertical(num // 10)
print(vertical(361))