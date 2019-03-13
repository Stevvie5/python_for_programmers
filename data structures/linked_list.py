class LinkedNode(object):
	__nextNode = None
	__prevNode = None
	
	def __init__(self, nodeObject, nextObject=None):
		self.__nodeObject = nodeObject
		if nextObject != None:
			self.__nextNode = LinkedNode(nextObject)
		
	def getObject(self):
		return self.__nodeObject
		
	def getNextNode(self):
		return self.__nextNode
		
	def getPrevNode(self):
		return self.__prevNode
		
	def setObject(self, nodeObject):
		self.__nodeObject = nodeObject
		
	def setNextObject(self, nextObject):
		self.__nextNode = LinkedNode(nextObject)
		
	def setPrevNode(self, prevNode):
		self.__prevNode = prevNode

class LinkedList(object):
	def __init__(self, headObject):
		self.headNode = LinkedNode(headObject)
		
	def append(self, endObject):
		currentNode = self.headNode
		finalLinkedNode = currentNode.getNextNode()
		
		if finalLinkedNode == None:
			self.headNode.setNextObject(endObject)
		else:
			while finalLinkedNode != None:
				currentNode = finalLinkedNode
				finalLinkedNode = currentNode.getNextNode()
			currentNode.setNextObject(endObject)
				
	def next(self):
		nextNode = self.headNode.getNextNode()
		nextNode.setPrevNode(self.headNode)
		self.headNode = nextNode
	
	def getCurrent(self):
		return self.headNode.getObject()
		
	def prev(self):
		prevNode = self.headNode.getPrevNode()
		self.headNode = prevNode

'''
TESTS

myList = LinkedList(120)
print(myList.getCurrent())

myList.append(130)
myList.append(150)
myList.append(160)

myList.next()
print(myList.getCurrent())
myList.next()
print(myList.getCurrent())
myList.next()
print(myList.getCurrent())

myList.prev()
print(myList.getCurrent())
myList.prev()
print(myList.getCurrent())
myList.prev()
print(myList.getCurrent())
'''


