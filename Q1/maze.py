#25 x 25 maze
#bottom left is 0,0, top right 24, 24

#heuristic: manhattan distance to goal?
#create tree with empty connections where there is a 0
#root node is start point, end points are leaves

from heapq import heappop, heappop
class MazeNode(object):
	def __init__(self, initial_value=0):
		self.value = initial_value
	def __init__(self, x, y):
		if maze[x][y+1]==1 
			self.up = new MazeNode(x,y+1)	
		if maze[x][y-1]==1
			self.down = new MazeNode(x,y-1)	
		if maze[x-1][y]==1
			self.left = new MazeNode(x-1,y)	
		if maze[x+1][y]==1
			self.right = new MazeNode(x+1,y)
			
	

maze = {{1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1},
		{0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		{0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1},
		{1,1,3,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1},
		{1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1},
		{1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,1},
		{1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1},
		{0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0},
		{1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0},
		{1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0},
		{1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0},
		{1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0},
		{1,1,4,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1},
		{1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1},
		{1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1},
		{1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1},
		{0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1},
		{0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1},
		{1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1},
		{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}}
		
# Main 
def solve():
	for int i in range(0,3):
		#start to E1
		tree = createTree(start, e1, maze)
		breadthFirst(tree)
		depthFirst(tree)
		aStar(tree)
		#start to E2
		tree = createTree(start, e2, maze)
		breadthFirst(tree)
		depthFirst(tree)
		aStar(tree)
		#start from 0,0 to 24,24
		tree = createTree({0,0}, {24,24}, maze)
		breadthFirst(tree)
		depthFirst(tree)
		aStar(tree)

# Maze to Graph 		
def createTree(start1, start2, end1, end2, maze):
	rootnode = maze[start1][start2]
	
	return rootnode
	
#BFS
def breadthFirst(tree):
	queue = [(tree, [tree])] #(current node, [array for path])
	while queue:
		(current, path) = queue.pop(0)
		for nextnode in maze[current] - set(path):
			if nextnode == goalnode:
				yield path + [nextnode]
			else:
				queue.append((next, path + [next]))
#DFS
def depthFirst(tree):
	stack = [(start, [start])] #(current node, [array for path])
	while stack:
		(current, path) = stack.pop()
		for nextnode in maze[current] - set(path):
			if nextnode == goalnode:
				yield path + [next]
			else:
				stack.append((next, path + [next]))
	return visited

#A*
def aStar(start, goal, maze):
	queue = []
	heappush(queue, (0 + heuristic(start, goal), 0, "", start))
	visited = set()
	graph = createTree(maze)
	while queue:
		_, cost, path, current = heappop(queue)
		if current == goal:
			return path
		if current in visited:
			continue
		visited.add(current)
		for direct, neighbor in graph[current]:
			heappush(queue, (cost+ heuristic(neighbor, goal), cost + 1, path + direct, neighbor))
	


def heuristic(cell, goal):
	return 10 * (abs(cell[0] - goal[0]) + abs(cell[1] - goal[1]))