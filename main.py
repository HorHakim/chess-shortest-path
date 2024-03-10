import numpy
import random
import copy

random.seed(1)


knight_position = random.randint(0, 7), random.randint(0,7)
goal_position = random.randint(0, 7), random.randint(0, 7)



def get_shortest_path_length(knight_position, goal_position, current_path=[]):

	shortest_path_length = float("inf")

	possible_moves = get_possible_moves(knight_position)

	for possible_move in possible_moves:
		current_path.append(possible_move)

		if current_path[-1] == goal_position and len(current_path) < shortest_path_length :
			shortest_path = copy.deepcopy(current_path)
			shortest_path_length = len(shortest_path)
	
