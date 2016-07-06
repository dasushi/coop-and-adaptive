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

legal_moves = {(x, y): [] for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)}
	
#Test if a move is legal, based on the board limits
def check_legal(board, new_move):
	return new_move[0] >= 0 and new_move[1] >= 0 and \ 		#check if the move is within 
	new_move[0] < len(board) and new_move[1] < len(board) 	#the limits of the board

#Rate a possible move based on the state of the board
#number of moves for player - number of moves for opponent
def evaluation(board, player_pos, opp_pos):
	total = 0
	for x, y in player_pos:
		for move in legal_moves:
			new_move = (x + move[0], y + move[1])
			if check_legal(board, new_move) and new_move not in player_pos:
				total += 2 #adjust this parameter? but this is good outcome for player
	for x, y in opp_pos:
		for move in legal_moves:
			new_move = (x + move[0], y + move[1])
			if check_legal(board, new_move) and new_move not in opp_pos:
				total -= -1 #good for opponent
				
	return total
	
def move(board, pos_before, pos_after, stones, player, count)
	count_pos_before = board[pos_before[0]][pos_before[1]]
	if count > 0:
		if count_pos_before < count:
			count = count_pos_before
		
		if board[pos_after[0]][pos_after[1]][0] == player:
			board[pos_after[0]][pos_after[1]][1] += count
		else:
			board[pos_after[0]][pos_after[1]][0] = color
			board[pos_after[0]][pos_after[1]][1] = count
		stones.add(pos_after)
		
		if board[pos_before[0]][pos_before[1]][1] <= 0:
			board[pos_before[0]][pos_before[1]][0] = None
			board[pos_before[0]][pos_before[1]][1] = 0
			if pos_before in stones:
				stones.remove(pos_before)
			
		return count > 0
	return False
	
def random_move(board, player, player_pos, opp_pos):
	random_moves = random.sample(player_pos, len(player_pos))
	for x, y in random_moves:
		random.shuffle(legal_moves)
		
		for move in legal_moves:
			initial_move = (x + move[0], y + move[1])
			count = board[x][y][1]
			if check_legal(board, initial_move) and initial_move not in opp_pos:
				new_move = (initial_move[0] + move[0], initial_move[1] + move[1])
				if new_move in opp_pos or not(check_legal(board, new_move)):
					return move(board, (x,y), initial_move, count, player_pos, player)
				else:
					final_move = (new_pos[0] + move[0], new_pos[1] + move[1])
					if final_move in opp_pos or not(check_legal(board, final_move)):
						return move(board, (x,y), initial_move, 1, player_pos, player) or \
							move(board, (x,y), new_move, num - 1, player_pos, player)
					else:
						return move(board, (x,y), initial_move, 1, player_pos, player) or \
							move(board, (x,y), new_move, 2, player_pos, player) or \
							move(board, (x,y), final_move, num - 3, player_pos, player)
	return False
	
def find_best_child(board, player_pos, opp_pos, max):
	new_max = float("inf")
	
	for x, y in opp_pos:
		for move in legal_moves:
			initial_move = (x + move[0], y + move[1])
			
			if check_legal(board, initial_move) and initial_move not in player_pos:
				possible_moves = set(opp_pos)
				possible_moves.add(initial_move)
				
				next_move = (initial_move[0] + move[0], initial_move[1] + move[1])
				if next_move not in player_pos and check_legal(board, next_move):
					possible_moves.add(next_move)
					final_move = (next_move[0] + move[0], next_move[1] + move[1])
					if final_move not in player_pos and check_legal(board, final_move):
						possible_moves.add(final_move)
				value = evaluation(board, player_pos, opp_pos)
				if value < max: 
					return value
				if value < new_max:
					new_max = value
		
	return new_max
	
def best_legal_move(board, player, opponent, player_pos, opp_pos):
	current_best = []
	value = -1*float("inf")
	for x,y in player_pos:
		for move in legal_moves:
			initial_move = (x + move[0], y + move[1])
			total_move = []
			
			if check_legal(board, initial_move) and initial_move not in player_pos:
				total_move.append(initial_move)
				total_move.append((x,y))
				possible_moves = set(opp_pos)
				possible_moves.add(initial_move)
				
				next_move = (initial_move[0] + move[0], initial_move[1] + move[1])
				
				if next_move not in player_pos and check_legal(board, next_move):
					total_move.append(next_move)
					possible_moves.add(next_move)
					
					final_move = (next_move[0] + move[0], next_move[1] + move[1])
					
					if final_move not in player_pos and check_legal(board, final_move):
						total_move.append(final_move)
						possible_moves.add(final_move)
				new_value = find_best_child(board, possible_moves, opp_pos, value)
				if new_value >= value:
					current_best = total_move
					value =  new_value
	if current_best.empty(0:
		return False
	else:
		count = board[current_best[0][0]][current_best[0][1]][1]
		if len(current_best) == 2:
			return move(board, current_best, count, player_pos, color)