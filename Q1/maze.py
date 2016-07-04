#25 x 25 maze
#bottom left is 0,0, top right 24, 24

#heuristic: manhattan distance to goal?
#create tree with empty connections where there is a 0
#root node is start point, end points are leaves	

maze = [[1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,3,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,1],
		[1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
		[1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0],
		[1,1,4,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
		[1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
		[1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1],
		[1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1],
		[0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1],
		[0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
		[1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
		
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
		
def solve(x, y):
	if maze
		
def createTree(maze):
	height = len(maze)
	width = len(maze[0]) if height else 0
	tree = {(x, y): [] for y in range(width) for x in range(height) if not maze[x][y]}
	for x, y in tree.keys():
		if not maze[x + 1][y] and x < height - 1:
			tree[(x + 1, y)].append(("U", (row, col))
			tree[(x, y)].append(("D", (x + 1, y)))
		if not maze[x][y + 1] and y < width - 1:
			tree[(x, y + 1)].append(("L", (x,y)))
			tree[(x,y)].append(("R", (x, y + 1)))
	return tree
	
#BFS
def breadthFirst(start, end, tree):
	queue = deque([("", start)]) #(current node, [array for path])
	visited = set()
	tree = createTree(start, end, maze)
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
def aStar(tree):
