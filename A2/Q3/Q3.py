import csv
from random import randint, sample

flow = [[0,0,5,0,5,2,10,3,1,5,5,5,0,0,5,4,4,0,0,1],
            [0,0,3,10,5,1,5,1,2,4,2,5,0,10,10,3,0,5,10,5],
            [5,3,0,2,0,5,2,4,4,5,0,0,0,5,1,0,0,5,0,0],
            [0,10,2,0,1,0,5,2,1,0,10,2,2,0,2,1,5,2,5,5],
            [5,5,0,1,0,5,6,5,2,5,2,0,5,1,1,1,5,2,5,1],
            [2,1,5,0,5,0,5,2,1,6,0,0,10,0,2,0,1,0,1,5],
            [10,5,2,5,6,5,0,0,0,0,5,10,2,2,5,1,2,1,0,10],
            [3,1,4,2,5,2,0,0,1,1,10,10,2,0,10,2,5,2,2,10],
            [1,2,4,1,2,1,0,1,0,2,0,3,5,5,0,5,0,0,0,2],
            [5,4,5,0,5,6,0,1,2,0,5,5,0,5,1,0,0,5,5,2],
            [5,2,0,10,2,0,5,10,0,5,0,5,2,5,1,10,0,2,2,5],
            [5,5,0,2,0,0,10,10,3,5,5,0,2,10,5,0,1,1,2,5],
            [0,0,0,2,5,10,2,2,5,0,2,2,0,2,2,1,0,0,0,5],
            [0,10,5,0,1,0,2,0,5,5,5,10,2,0,5,5,1,5,5,0],
            [5,10,1,2,1,2,5,10,0,1,1,5,2,5,0,3,0,5,10,10],
            [4,3,0,1,1,0,1,2,5,0,10,0,1,5,3,0,0,0,2,0],
            [4,0,0,5,5,1,2,5,0,0,0,1,0,1,0,0,0,5,2,0],
            [0,5,5,2,2,0,1,2,0,5,2,1,0,5,5,0,5,0,1,1],
            [0,10,0,5,5,1,0,2,0,5,2,2,0,5,10,2,2,1,0,6],
            [1,5,0,5,1,5,10,10,2,2,5,5,5,0,10,0,0,1,6,0]]
            
            
distance = [[0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7],
            [1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5,6],
            [2,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5],
            [3,2,1,0,1,4,3,2,1,2,5,4,3,2,3,6,5,4,3,4],
            [4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,7,6,5,4,3],
            [1,2,3,4,5,0,1,2,3,4,1,2,3,4,5,2,3,4,5,6],
            [2,1,2,3,4,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5],
            [3,2,1,2,3,2,1,0,1,2,3,2,1,2,3,4,3,2,3,4],
            [4,3,2,1,2,3,2,1,0,1,4,3,2,1,2,5,4,3,2,3],
            [5,4,3,2,1,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2],
            [2,3,4,5,6,1,2,3,4,5,0,1,2,3,4,1,2,3,4,5],
            [3,2,3,4,5,2,1,2,3,4,1,0,1,2,3,2,1,2,3,4],
            [4,3,2,3,4,3,2,1,2,3,2,1,0,1,2,3,2,1,2,3],
            [5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,4,3,2,1,2],
            [6,5,4,3,2,5,4,3,2,1,4,3,2,1,0,5,4,3,2,1],
            [3,4,5,6,7,2,3,4,5,6,1,2,3,4,5,0,1,2,3,4],
            [4,3,4,5,6,3,2,3,4,5,2,1,2,3,4,1,0,1,2,3],
            [5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,2],
            [6,5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1],
            [7,6,5,4,3,6,5,4,3,2,5,4,3,2,1,4,3,2,1,0]]


soln_matrix = [[0]*20]*20
soln = sample(xrange(20), 20)

def tabu_search(solution, solution_matrix):
	best_soln = tmp_solution = solution

	prvs_cost = lwst_cost = cost = get_cost(solution)
	tabu_size = randint(1,10)


	for i in range(2570):
		if (lwst_cost <= 2570):
			break
		tmp_solution = get_neighbour(tmp_solution, solution_matrix, best_soln, tabu_size)

		cost = get_cost(tmp_solution)
		if i == randint(i, i+100) or prvs_cost == cost:
			tabu_size = randint(1,10)
		
		# Track Cycling 
		if i % 2 == 0:
			prvs_cost = cost
		solution_matrix = move_operator(solution_matrix)
		

		if cost < lwst_cost:
			if cost < 2650:
				lwst_cost = cost
				best_soln = tmp_solution

	return [lwst_cost, best_soln]



def get_neighbour(solution, tabu, best_soln, tabu_size):
	lowest = 100000000
	improved_solution = []

	for i in range(len(solution)):
		for j in range(len(solution)):
			if i < j:
				arr = solution[:]
				arr[i], arr[j] = arr[j], arr[i]
				cost = get_cost(arr)

				if cost < lowest:
				 	if (tabu[arr[i]][i] == 0 and tabu[arr[j]][j] == 0)\
                    or (arr == best_soln and tabu[arr[i]][i] < 3 and tabu[arr[j]][j] < 3):
						lowest = cost
						improved_solution = arr
						tabu[arr[j]][j] = tabu_size
						tabu[arr[i]][i] = tabu_size
	print lowest
	return improved_solution


def move_operator(tabu):
    for i in range(len(tabu)):
        for j in range(len(tabu)):
            if tabu[i][j] > 0:
                tabu[i][j] -= 1
    return tabu


def get_cost(solution):
    permutated = [[0]*20]*20
    permute_flow = [[0]*20]*20
    cost = 0

    for i in range(len(solution)):
        permute_flow[i] = flow[solution[i]]

    for i in range(len(solution)):
        column = [row[solution[i]] for row in permute_flow]
        for j in range(len(permutated)):
            permutated[j][i] = column[j]

    for i in range(len(distance)):
    	row_cost = 0
        for j in range(len(distance[0])):
            row_cost += permutated[i][j] * distance[i][j]

        cost += row_cost

    return cost


values = tabu_search(soln, soln_matrix)
print("Tabu Search")
print("Cost: " + str(values[0]))
print("Initial problem: ", soln)
print("Solution: " , values[1])
