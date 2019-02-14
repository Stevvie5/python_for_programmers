def reverse(text):
	'Reverse a string'
	if len(text) == 1:
		return text
	else:
		return text[-1] + reverse(text[0 : len(text)-1])
		