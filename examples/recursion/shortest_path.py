def createMaze(width, height):
	maze = []
	for line in range(height):
		mazeLine = []
		for item in range(width):
			mazeLine.append(1)
		maze.append(mazeLine)
	return maze
	
def showMaze(maze):
	for line in maze:
		print(line)

def getPointConnections(maze, point):
	connections = []
	
	if point[1] != 0:
		newPoint = (point[0], point[1] - 1)
		connections.append(newPoint)
		
	if point[1] != len(maze) - 1:
		newPoint = (point[0], point[1] + 1)
		connections.append(newPoint)
		
	if point[0] != 0:
		newPoint = (point[0] - 1, point[1])
		connections.append(newPoint)
		
	if point[0] != len(maze[point[1]]) - 1:
			newPoint = (point[0] + 1, point[1])
			connections.append(newPoint)
	return connections
	
#def findShortestPath(maze, source, destination):
	
maze = createMaze(10, 10)