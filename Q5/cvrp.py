#Capacitative Vehicle Routing Problem

def check_legal(current, capacities):
	for x in range(len(list)):
		total_capacity = 0
		for y in range(len(list[i])):
			total_capacity += capacities[x][y]
	return total_capacity <= 100:
	
def cost_function(solution, positions):
	total_cost = 0
	for item in solution:
		for subitem in item:
			if subitem == item[0] or subitem == item[len(item) - 1]:
				total_cost += euclidean(positions[0], positions[subitem])
			
			#if this isnt the last node
			if subitem != item[len(item) - 1]:
				nextnode = item[item.index(subitem)+1]
				total_cost += euclidean(positions[nextnode], positions[subitem])
	return total_cost
	
def annealing_loop(initial, positions, capacities, cities, min_vehicles, initial_temp, final_temp, alpha):
	current_cost = cost_function(initial, positions)
	best_cost = current_cost
	current = best = initial
	iter = 0
	while current_temp > final_temp:
		while iter < max_iter:
			possible_moves = get_possible_move(current, min_vehicles, capacities)
			possible_cost = cost_function(possible_moves, positions)
			delta = possible_cost - current_cost
			
			if delta > 0:
				randomval = random.random()
				if randomval < math.exp(-1*delta / current_temp):
					current = possible_moves
					current_cost = possible_cost
			else:
				current = possible_moves
				current_cost = possible_cost
			iter+=1
		current_temp = current_temp * alpha
		
		if current_cost < best_cost:
			best = current
			best_cost = current_cost
	return(best, best_cost)