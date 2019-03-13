class Apple(object):
	def __init__(self, value):
		self.value = value
		
	@classmethod
	def from_string(cls, value):
		return cls(value)