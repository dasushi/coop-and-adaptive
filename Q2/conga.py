#Conga playing question, 4x4 grid game
#each player starts with 10 stones at (1,4) and (4,1)
#Stones can be distributed in a row as long as not blocked by an enemy stone
#Goal is to block opponent so they have no legal moves

#(1,4) (2,4) (3,4) (4,4)
#(1,3) (2,3) (3,3) (4,3)
#(1,2) (2,2) (3,2) (4,2)
#(1,1) (2,1) (3,1) (4,1)

#Must make a random player and a minmax player with alphabeta pruning
#Experiment with different evalutation functions

import random

legal_moves = [[x, y] for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0) and x!=y and x!=-y]
	
#Test if a move is legal, based on the board limits
def check_legal(new_move):
	#check if the move is within the limits of the board
	return new_move[0] >= 0 and new_move[1] >= 0 and new_move[0] <= 3 and new_move[1] <= 3

#Rate a possible move based on the state of the board
#number of moves for player - number of moves for opponent
def evaluation(board, player_pos, opp_pos):
	total = 0
	total += calculate_evaluation(player_pos, opp_pos, 2)
	total += calculate_evaluation(opp_pos, player_pos, -1)
	return total
	
def calculate_evaluation(player_pos, opp_pos, adjust):
	total = 0
	for x, y in player_pos:
		for move in legal_moves:
			new_move = (x + move[0], y + move[1])
			if check_legal(new_move) and new_move not in opp_pos:
				total += adjust
	return total
	
def change_value(board, move, player_pos, player, value):
	if board[move[0]][move[1]][0] == player:
		board[move[0]][move[1]][1] += value
	#if it is unoccupied
	elif board[move[0]][move[1]][0] == None:
		board[move[0]][move[1]][0] = player
		board[move[0]][move[1]][1] = value
		player_pos.add(move) #add to the player's list
	
def perform_move(board, move_list, player_pos, player):
	count_before = board[move_list[0][0]][move_list[0][1]][1]
	if count_before >= 1:
		#figure out how many stones to move
		#print move_list
		if len(move_list) == 2:
			change_value(board, move_list[1], player_pos, player, count_before)
			count_before = 0
		elif len(move_list) == 3:
			change_value(board, move_list[1], player_pos, player, 1)
			count_before -= 1
			if count_before > 0:
				change_value(board, move_list[2], player_pos, player, count_before)
				count_before = 0
		elif len(move_list) == 4: 
			change_value(board, move_list[1], player_pos, player,1)
			count_before -= 1
			if count_before > 0:
				change_value(board, move_list[2], player_pos, player, min(count_before, 2))
				count_before -= min(count_before, 2)
				if count_before > 0: 
					change_value(board, move_list[3], player_pos, player, count_before)
					count_before = 0
		
		#take away stones from initial spot		
		board[move_list[0][0]][move_list[0][1]][1] = count_before
		
		#remove the original spot if there aren't any stones left
		if count_before <= 0:
			board[move_list[0][0]][move_list[0][1]][0] = None
			board[move_list[0][0]][move_list[0][1]][1] = 0
			if move_list[0] in player_pos:
				player_pos.remove(move_list[0])
			
		return True
	return False
	
def random_move(board, player, player_pos, opp_pos):
	random_moves = random.sample(player_pos, len(player_pos))
	for x, y in random_moves:
		random.shuffle(legal_moves)
		
		for move in legal_moves:
			move_list = [(x,y),(x + move[0], y + move[1])]
			value = board[x][y][1]
			#print move_list
			if check_legal(move_list[1]) and move_list[1] not in opp_pos:
				temp_move = (move_list[1][0] + move[0], move_list[1][1] + move[1])
				if temp_move in opp_pos or not(check_legal(temp_move)) or value < 2:
					#print("Found a random move: " + str(move_list))
					return perform_move(board, move_list, player_pos, player)
				else:
					move_list.append(temp_move)
					temp_move = (move_list[2][0] + move[0], move_list[2][1] + move[1])
					if temp_move in opp_pos or not(check_legal(temp_move)) or value < 4:
						#print("Found a random move: " + str(move_list))
						return perform_move(board, move_list, player_pos, player)
					else:
						move_list.append(temp_move)
						#print("Found a random move: " + str(move_list))
						return perform_move(board, move_list, player_pos, player)
	print "Stuck! Random(" + player + ") loses"
	return False
	
def find_best_value(board, player_pos, opp_pos, best):
	new_min = float("inf")
	
	for x, y in opp_pos:
		for move in legal_moves:
			temp_move = (x + move[0], y + move[1])
			value = board[x][y][1]
			
			if check_legal(temp_move) and temp_move not in player_pos:
				possible_moves = set(opp_pos)
				possible_moves.add(temp_move)
				temp_move = (temp_move[0] + move[0], temp_move[1] + move[1])
				if temp_move not in player_pos and check_legal(temp_move) and value > 1:
					possible_moves.add(temp_move)
					temp_move = (temp_move[0] + move[0], temp_move[1] + move[1])
					if temp_move not in player_pos and check_legal(temp_move) and value > 3:
						possible_moves.add(temp_move)
				value = evaluation(board, player_pos, possible_moves) #
				if value < best: 
					return value
				if value < new_min:
					new_min = value
		
	return new_min
	
def minmax_find_move(board, player, player_pos, opp_pos):
	current_best = []
	max_value = 0
	for x,y in player_pos:
		for move in legal_moves:
			temp_move = (x + move[0], y + move[1])
			move_list = [(x,y)]
			value = board[x][y][1]
			
			if check_legal(temp_move) and temp_move not in opp_pos and value > 0:
				possible_moves = set(player_pos)
				possible_moves.add(temp_move)
				move_list.append(temp_move)
				temp_move = (temp_move[0] + move[0], temp_move[1] + move[1])
				
				if temp_move not in player_pos and check_legal(temp_move) and value > 1:
					possible_moves.add(temp_move)
					move_list.append(temp_move)
					temp_move = (temp_move[0] + move[0], temp_move[1] + move[1])
					
					if temp_move not in player_pos and check_legal(temp_move) and value > 3:
						possible_moves.add(temp_move)
						move_list.append(temp_move)
				new_value = find_best_value(board, possible_moves, opp_pos, max_value)
				if new_value >= max_value:
					current_best = move_list
					max_value =  new_value
	if current_best:
		#print("Found a best move: " + str(current_best) + ", value of " + str(max_value))
		move_length = len(current_best)
		return perform_move(board, current_best, player_pos, player)
		#print("Performed move " + str(current_best))
				   
	print("Stuck! MinMax(" + player + ") loses")
	return False
	
def print_board(board):
	for x in range(4):
		for y in range(4):
			print("pos: " + str(x) + ", " + str(y) + " val: " + str(board[x][y]))
	
player_1_pos = set()
player_2_pos = set()
board = [[[None, 0] for x in range(4)] for y in range (4)]
board[0][3] = ["Black", 10]
board[3][0] = ["White", 10]
player_1_pos.add((0,3))
player_2_pos.add((3,0))
turn = 0
while(random_move(board, "Black", player_1_pos, player_2_pos)):
	if(minmax_find_move(board, "White", player_2_pos, player_1_pos)):
		#print "Making a move"
		turn+=1
	else:
		break
print("Random player: " + str(player_1_pos))
print("Minmax player: " + str(player_2_pos))	
print_board(board)
print("Turns it took: " + str(turn))
	
	