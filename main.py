import numpy
import random
import copy
from itertools import product

import time
import tqdm

import matplotlib.pyplot as plt
random.seed(1)


class PathFinder:
	def __init__(self, start_position, end_position, grid_shape=(8, 8)):
		self.start_position = start_position
		self.end_position = end_position
		self.current_path = [start_position]
		self.grid_shape = grid_shape

		self.shortest_path_length=float("inf")


	def is_possible_move(self, potential_position, row_move, col_move):
		knight_move = True if abs(row_move) + abs(col_move) == 3 and all((row_move, col_move)) else False

		inside_grid = potential_position[0] < self.grid_shape[0] and\
					  potential_position[1] < self.grid_shape[1] and\
					  potential_position[0] >= 0 and\
					  potential_position[1] >= 0

		in_current_path = potential_position in self.current_path

		return knight_move and inside_grid and not in_current_path

	
	def get_possible_moves(self):
		moves = []

		current_row, current_col = self.current_path[-1]
		
		for row_move, col_move in product(range(-2, 3), range(-2, 3)):
			potential_position = current_row + row_move, current_col + col_move
			
			if self.is_possible_move(potential_position, row_move, col_move):
				moves.append(potential_position)

		return moves


	def get_shortest_path_length(self):

		if len(self.current_path) > self.shortest_path_length - 1:
			return None

		for possible_move in self.get_possible_moves():
			self.current_path.append(possible_move)
	
			if possible_move == self.end_position:
				self.shortest_path_length = len(self.current_path) - 1
				# self.print_all_moves_of_current_path()
				
			self.get_shortest_path_length()
	
			self.current_path.pop()	



	def print_all_moves_of_current_path(self):
		for position in self.current_path[1:]:
			grid = numpy.zeros(self.grid_shape, dtype=str)
			grid[:] = "O"
			grid[self.start_position] = "S"
			grid[self.end_position] = "E"
			grid[position] = "K"
			print(grid)
			print("_"*50)
		print(f"Path lenght = {self.shortest_path_length}")
		print("_"*100)
	


def generate_problems(grid_size, number_of_problems):
	problems = []
	for _ in range(number_of_problems):
		start_position = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
		end_position = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
		while end_position == start_position:
			end_position = random.randint(0, grid_size-1), random.randint(0, grid_size-1)

		problems.append((start_position, end_position))

	return problems


if __name__ == '__main__':
	number_of_problems = 1000
	mean_times = []
	mean_lengths = []

	for grid_size in tqdm.tqdm(range(6, 11)):
		problems = generate_problems(grid_size, number_of_problems)
		time_problems = []
		length_problems = []

		for problem in tqdm.tqdm(problems):
			starting_time = time.time()
			
			grid_shape = (grid_size, grid_size)
			path_finder_object = PathFinder(problem[0], problem[1], grid_shape)
			path_finder_object.get_shortest_path_length()
			
			ending_time = time.time()
			time_problems.append(ending_time-starting_time)
			length_problems.append(path_finder_object.shortest_path_length)

		mean_times.append(sum(time_problems)/ number_of_problems)
		mean_lengths.append(sum(length_problems)/ number_of_problems)
		

	plt.figure(figsize=(10, 10))
	plt.plot([grid_size for grid_size in range(6, 11)], mean_times, "r-")
	plt.title(f"Temps moyen / la taille de la grille")

		

	plt.figure(figsize=(10, 10))
	plt.plot([grid_size for grid_size in range(6, 11)], mean_lengths, "r-")
	plt.title(f"Taille moyenne du chemin le plus court / la taille de la grille")
	plt.show()
		