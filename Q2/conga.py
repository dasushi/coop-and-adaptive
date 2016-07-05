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
	

def check_legal(board, new_move):
	return new_move[0] >= 0 and new_move[1] >= 0 and \
	new_move[0] < len(board) and new_move[1] < len(board)
	
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
	
def move(board, before, after, stones, player, number)
	count_before = board[before[0]][before[1]]
	if number > 0:
		if count_before < number:
			number = count_before
		
		if board[after[0]][after[1]][0] == player:
			board[after[0]][after[1]][1] += number
		else:
			board[after[0]][after[1]][0] = color
			board[after[0]][after[1]][1] = number
		stones.add(after)
		
		board[before[0]][before[1]][1] <= 0:
			board[before[0]][before[1]][0] = None
			board[before[0]][before[1]][1] = 0
			if before in stones:
				stones.remove(before)
			
		return number > 0
	return False
	