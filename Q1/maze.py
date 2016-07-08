#25 x 25 maze
#bottom left is 0,0, top right 24, 24

#heuristic: manhattan distance to goal?
#create tree with empty connections where there is a 0


from heapq import heappop, heappush
from collections import deque

maze = [[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0], 
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0], 
        [0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0], 
        [0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0], 
        [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0], 
        [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0],
        [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0],
        [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


# Main 
def solve():

	tree = createTree(maze)
	#start to E1
	start = (13, 2)
	e1 = (5, 23)
	breadthFirst(start, e1, tree)
	depthFirst(start, e1, tree)
	aStar(start, e1, tree)
	#start to E2
	e2 = (13, 3)
	breadthFirst(start, e2, tree)
	depthFirst(start, e2, tree)
	aStar(start, e2, tree)
	# #start from 0,0 to 24,24
	start = (24,0)
	end = (0,24)
	breadthFirst(start, end, tree)
	depthFirst(start, end, tree)
	aStar(start, end, tree)

		
def createTree(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

#BFS
def breadthFirst(start, end, tree):
	queue = deque([(start, "")]) #(current node, [array for path])
	visited = []
	while queue:
		(current, path) = queue.popleft()
		if current == end:
			break
		if current in visited:
			continue
		visited.append(current)
		for direct, relative in tree[current]:
			queue.append((relative, path + direct))
	print("Breadth First Traversal")
	print("Visited: ", visited)
	print("Path: ", path)
	
#DFS
def depthFirst(start, goal, tree):
	stack = deque([("", start)]) #(current node, [array for path])
	visited = []
	while stack:
		(path, current) = stack.pop()
		if current == goal:
			break
		if current in visited:
			continue
		visited.append(current)
		for direct, neighbor in tree[current]:
			stack.append((path + direct, neighbor))
	print("Depth First Traversal")
	print("Visited: ", visited)
	print("Path: ", path)

#A*
def aStar(start, goal, tree):
	queue = []
	heappush(queue, (heuristic(start, goal), 1, "", start))
	visited = []
	while queue:
		_, cost, path, current = heappop(queue)
		if current == goal:
			break
		if current in visited:
			continue
		visited.append(current)
		for direct, neighbor in tree[current]:
			heappush(queue, (cost+ heuristic(neighbor, goal), cost + 1, path + direct, neighbor))
	print("A* Algorithm")
	print("Cost: " + str(cost))
	print("Path: " + str(path))
	print("Visited: " , visited)


def heuristic(cell, goal):
	return 10 * (abs(cell[0] - goal[0]) + abs(cell[1] - goal[1]))


solve()