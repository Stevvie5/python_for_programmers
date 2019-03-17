from linked_list import LinkedList

class StackNode(object):
	__nextNode = None
	
	def __init__(self, nodeObject=None, nextObject=None):
		self.__nodeObject = nodeObject
		if nextObject != None:
			self.__nextNode = StackNode(nextObject)
			
	def getObject(self):
		return self.__nodeObject
		
	def getNextNode(self):
		return self.__nextNode
		
	def setNextObject(self, nextObject):
		self.__nextNode = StackNode(nextObject)
		
	def setNextNode(self, nextNode):
		self.__nextNode = nextNode
		
	def setObject(self, newObject):
		self.__nodeObject = newObject

class Stack(object):
	__headNode = StackNode()

	def push(self, newObject):
		if self.isEmpty():
			self.__headNode.setObject(newObject)
		else:
			newHead = StackNode(newObject)
			newHead.setNextNode(self.__headNode)
			self.__headNode = newHead
	
	def pop(self):
		currentValue = self.__headNode.getObject()
		newHead = self.__headNode.getNextNode()
		self.__headNode = newHead
		return currentValue
		
	def isEmpty(self):
		if self.__headNode.getObject() == None:
			return True
		else:
			return False
			
	def top(self):
		return self.__headNode.getObject()