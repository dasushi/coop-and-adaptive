#25 x 25 maze
#bottom left is 0,0, top right 24, 24

#heuristic: manhattan distance to goal?
#create tree with empty connections where there is a 0


from heapq import heappop, heappop
from collections import deque
			
	
#root node is start point, end points are leaves	

maze = [[1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,3,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
		[0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
		[1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0],
		[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1],
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
		
# Main 
def solve():
	for i in range(3):
		#start to E1
		start = (2, 11)
		e1 = (22, 19)
		breadthFirst(start, e1, maze)
		depthFirst(start, e1, maze)
		aStar(start, e1, maze)
		#start to E2
		e2 = (2, 21)
		breadthFirst(start, e2, maze)
		depthFirst(start, e2, maze)
		aStar(start, e2, maze)
		#start from 0,0 to 24,24
		start = (0,0)
		end = (24,24)
		breadthFirst(start, end, maze)
		depthFirst(start, end, maze)
		aStar(start, end, maze)

		
def createTree(maze):
	height = len(maze)
	if height:
		width = len(maze[0])
	else:
		width = 0
	width = len(maze[0]) if height else 0
	tree = {(x, y): [] for y in range(width) for x in range(height) if not maze[x][y]}
	for x, y in tree.keys():
		if not maze[x + 1][y] and x < height - 1:
			tree[(x + 1, y)].append(("U", (x, y)))
			tree[(x, y)].append(("D", (x + 1, y)))
		if y < width - 1 and not maze[x][y + 1]:
			tree[(x, y + 1)].append(("L", (x,y)))
			tree[(x,y)].append(("R", (x, y + 1)))
	return tree

#BFS
def breadthFirst(start, end, tree):
	queue = deque([(start, "")]) #(current node, [array for path])
	visited = set()
	tree = createTree(maze)
	while queue:
		(current, path) = queue.popleft()
		if current == end:
			break
		if current in visited:
			continue
		visited.add(current)
		import pdb
		pdb.set_trace()
		for direct, relative in tree[current]:
			queue.append((neighbour, path + direct))
	print("Breadth First Traversal")
	print("Visited: " + visited)
	print("Path: " + path)
	
#DFS
def depthFirst(start, goal, maze):
	stack = deque([("", start)]) #(current node, [array for path])
	visited = set()
	tree = createTree(maze)
	while stack:
		(current, path) = stack.pop()
		if current == goal:
			break
		if current in visited:
			continue
		visited.add(current)
		for direct, neighbor in tree[current]:
			stack.append((neighbor, path + dir))
	print("Depth First Traversal")
	print("Visited: " + visited)
	print("Path: " + path)

#A*
def aStar(start, goal, maze):
	queue = []
	heappush(queue, (0 + heuristic(start, goal), 0, "", start))
	visited = set()
	tree = createTree(maze)
	while queue:
		_, cost, path, current = heappop(queue)
		if current == goal:
			break
		if current in visited:
			continue
		visited.add(current)
		for direct, neighbor in tree[current]:
			heappush(queue, (cost+ heuristic(neighbor, goal), cost + 1, path + direct, neighbor))
	print("A* Algorithm")
	print("Cost: " + cost)
	print("Path: " + path)
	print("Visited: " + visited)


def heuristic(cell, goal):
	return 10 * (abs(cell[0] - goal[0]) + abs(cell[1] - goal[1]))


solve()