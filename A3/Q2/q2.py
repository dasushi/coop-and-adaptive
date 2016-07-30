from math import hypot
import random
# Calculate 
total_cities = 29
alpha = 1
beta = 5
num_of_ants = 15
evap_rate = 0.1
Q = 2000
iteration_times = 3000

# Fill with 
cities = [
	[ 1150.0,  1760.0],
	[ 630.0, 1660.0 ],
	[ 40.0,  2090.0 ],
	[ 750.0, 1100.0 ],
	[ 750.0, 2030.0 ],
	[ 1030.0,  2070.0 ],
	[ 1650.0,  650.0 ],
	[ 1490.0,  1630.0 ],
	[ 790.0, 2260.0 ],
	[ 710.0, 1310.0 ],
	[ 840.0, 550.0 ],
	[ 1170.0,  2300.0 ],
	[ 970.0, 1340.0 ],
	[ 510.0, 700.0 ],
	[ 750.0, 900.0 ],
	[ 1280.0,  1200.0 ],
	[ 230.0, 590.0 ],
	[ 460.0, 860.0 ],
	[ 1040.0,  950.0 ],
	[ 590.0, 1390.0 ],
	[ 830.0, 1770.0 ],
	[ 490.0, 500.0 ],
	[ 1840.0,  1240.0 ],
	[ 1260.0,  1500.0 ],
	[ 1280.0,  790.0 ],
	[ 490.0, 2130.0 ],
	[ 1460.0,  1420.0 ],
	[ 1260.0,  1910.0 ],
	[ 360.0, 1980.0 ]]


pheromone = [[1000.0]*total_cities]*total_cities
distance = [[hypot(cities[i][0] - cities[j][0], cities[i][1]-cities[j][1]) for j in range(total_cities)] for i in range(total_cities)]

class ant:
	def __init__(self, initial):
		self.current_city = initial
		self.initial = initial
		self.visited = []
		self.visited.append(initial)
		self.unvisited = [x for x in range(29)]
		self.unvisited.remove(initial)


	# Return next city using array of unvisited cities' probabilities
	def calc_next_city(self):
		denominator = 0
		probability = []

		for city in self.unvisited:
			numerator = (pheromone[self.current_city][city]**alpha)*((1/distance[self.current_city][city])**beta)
			denominator += numerator
			probability.append(numerator)

		if denominator == 0:
			return self.unvisited[0]

		probability = [x/denominator for x in probability]

		random_num = random.random()
		tmp = 0
		city_found = False
		possible_city = 0

		while not city_found:
			tmp += probability[possible_city]
			if tmp >= random_num:
				return self.unvisited[possible_city]
			else:
				possible_city += 1

	def construct_solution(self):
		while len(self.unvisited) > 0:
			self.current_city = next_city = self.calc_next_city()
			self.visited.append(next_city)
			self.unvisited.remove(next_city)

	def get_cost(self):
		cost = 0
		for city in range(len(self.visited)-1):
			cost += distance[self.visited[city]][self.visited[city+1]]
		cost += distance[self.initial][self.visited[-1]]
		return cost

	def add_pheromone(self):
		cost = self.get_cost()
		for city in range(28):
			pheromone[self.visited[city]][self.visited[city+1]] += Q / cost
		pheromone[self.initial][self.visited[-1]] += Q / cost

	def reinit(self, initial):
		self.current_city = initial
		self.initial = initial
		self.visited = []
		self.visited.append(initial)
		self.unvisited = [x for x in range(29)]
		self.unvisited.remove(initial)

initial_cities = random.sample(range(29), num_of_ants)
ants = [ant(x) for x in initial_cities]

for i in range(iteration_times):
	
	if i != 0:
		initial_cities = random.sample(range(29), num_of_ants)

		for i in range(num_of_ants):
			ants[i].reinit(initial_cities[i])
		
	
	for ant in ants:
		ant.construct_solution()
	
	#evaporate
	pheromone[:] = [[(1- evap_rate)*pheromone[i][j] for j in range(total_cities)] for i in range(total_cities)]
	
	for ant in ants:
		ant.add_pheromone()
	

best_ant = ants[0]
best_cost = ants[0].get_cost()
for ant in ants:
	if ant.get_cost() < best_cost:
		best_ant = ant
		best_cost = ant.get_cost()

print "Initial: ", best_ant.initial
print "Visited: ", best_ant.visited
print "Cost: " + str(best_ant.get_cost())