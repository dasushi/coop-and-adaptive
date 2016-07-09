#Capacitated Vehicle Routing Problem
import random, math

def check_legal(current, demand_list, max_capacity):
	for path in current:
		capacity = 0
		for node in path:
			capacity += demand_list[node]
			if capacity > max_capacity:
				return False
	return True
	
def cost_function(solution, positions):
	total_cost = 0
	for path in solution:
		for node in path:
			if node == path[0] or node == path[len(path) - 1]:
				total_cost += euclidean(positions[0], positions[node])
			#if this isnt the last node
			elif node != path[len(path) - 1]:
				total_cost += euclidean(positions[path[path.index(node)+1]], positions[node])
	return total_cost
	
def euclidean(p1, p2):
	return round(math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])))

	
def get_route(positions, demand_list, min_vehicles, max_capacity):
	route = []
	cities = positions
	while len(cities)>1:
		capacity = 0
		path = []
		for y in xrange(min(7,len(cities)-1)):	
			iter = 0
			choice = random.choice(cities[1:])
			capacity += demand_list[choice]
			while capacity > max_capacity and iter < 5: 
				capacity -= demand_list[choice]
				choice = random.choice(cities[1:])
				iter+=1
				capacity += demand_list[choice]
			if capacity > max_capacity:
				break
			else:
				cities.remove(choice)
				path.append(choice)
		route.append(path)
	return route
	
def random_solution(cities, min_vehicles, max_capacity, demand_list):
	legal = False
	iter = 0
	while not legal:
		new_solution = list(get_route(cities, demand_list, min_vehicles, max_capacity))
		legal = True
		for path in new_solution:
			capacity = 0
			for node in path:
				capacity += demand_list[node]
			if capacity > max_capacity:
				legal = False
				break
	return new_solution
	
def find_valid_neighbour(initial, demand_list, max_capacity):
	legal = False
	solution = []
	while not legal:
		new_solution = initial
		maxval = len(new_solution) - 1
		source = random.randint(0, maxval)
		destination = random.randint(0, maxval)
		#if the source list has only 1 node, pick another
		while not(len(new_solution[source]) > 1):
			source = random.randint(0, maxval)
		#if we picked the same source and destination, try again
		while destination == source:
			destination = random.randint(0, maxval)
		#we need to pick an index from our source path
		position_index = random.randint(0, len(new_solution[source]) - 1)
		#swap the node into the other path
		source_node = new_solution[source][position_index]
		new_solution[source].remove(source_node)
		new_solution[destination].append(source_node)
		#if it is empty now, remove it
		if not(new_solution[destination]):
			new_solution.remove(new_solution[destination])
		#verify if legal, if it is, return it
		legal = check_legal(new_solution, demand_list, max_capacity)
		if legal:
			solution = new_solution
	return solution
	
def annealing_loop(initial, positions, demand_list, cities, min_vehicles, max_capacity, initial_temp, final_temp, alpha, max_iter):
	current_cost = cost_function(initial, positions)
	best_cost = current_cost
	current = initial
	best = initial
	current_temp = initial_temp
	iter = 0
	while current_temp > final_temp:
		while iter < max_iter:
			#find potential moves to make`
			possible_moves = find_valid_neighbour(current, demand_list, max_capacity)
			possible_cost = cost_function(possible_moves, positions)
			#if iter%50==0:
			#	print("Iteration: " + str(iter) + " at " + str(current_temp) + ", cost: " + str(possible_cost) + ", best cost: " + str(best_cost))# + ", path: " + str(possible_moves))
 			#calculate improvement in cost
			delta = possible_cost - current_cost
			#if it is better than previous, or if we pass a random check, then accept it
			if delta < 0 or random.random() < math.exp(-1*delta / current_temp):
				current = possible_moves
				current_cost = possible_cost
				
			iter+=1
		iter = 0
		current_temp *= alpha
		print("Temp: " + str(current_temp) + ", cost: " + str(current_cost) + ", best cost: " + str(best_cost))
		#accept solution if it is an improvement
		if current_cost < best_cost:
			best = current
			best_cost = current_cost
			
	return(best, best_cost)
	

positions = []
demand_list = []
depots = []
initial_temp = 600
final_temp = 100
alpha = 0.96
max_iter = 100
min_vehicles = 1
max_capacity = 100
dimension = 1
read_flag = 0

inputfile = open('A-n33-k5.vrp', 'r')
for raw in inputfile:
	value = raw.split()
	header = value[0]
	if read_flag > 0:
		read_flag -= 1
	if header == "NAME":
		name = value[2]
	elif header == "COMMENT":
		min_vehicles = int(value[9][0])
	elif header == "CAPACITY":
		max_capacity = int(value[2])
	elif header == "DIMENSION":
		dimension = int(value[2])
	elif header == "DEPOT_SECTION":
		read_flag = 6
		print "In DEPOT_SECTION"
	elif header == "DEMAND_SECTION":
		read_flag = 4
		print "In DEMAND_SECTION"
	elif header == "NODE_COORD_SECTION":
		read_flag = 2
		print "In NODE_COORD_SECTION"
	elif header == "EOF":
		read_flag = 0
		print "EOF"
		
	if read_flag == 1:
		positions.append((int(value[1]), int(value[2])))
		read_flag += 1
	elif read_flag == 3:
		demand_list.append((int(value[1])))
		read_flag += 1
	elif read_flag == 5:
		read_flag += 1
		depots.append((int(value[0])))
cities = [x+1 for x in xrange(len(positions) - 1)]
print("Starting, min vehicles: " + str(min_vehicles) + ", max_capacity: " + str(max_capacity) + ", dimensions/nodes:" + str(dimension))
random_solution = random_solution(cities, min_vehicles, max_capacity, demand_list)
print(random_solution)
print(cost_function(random_solution, positions))
(best, value) = annealing_loop(random_solution, positions, demand_list, cities, min_vehicles, max_capacity, initial_temp, final_temp, alpha, max_iter)
print("Solution found with value of: " + str(value))
print(str(best))
for route in best:
	print(str(route))
	capacity = 0
	for edge in route:
		capacity += demand_list[edge]
	print(str(capacity))
	capacity = 0