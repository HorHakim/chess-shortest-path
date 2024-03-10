import numpy
import random
random.seed(1)

grid = numpy.zeros(shape=(8,8))
knight_position = random.randint(0, 7), random.randint(0,7)
goal_position = random.randint(0, 7), random.randint(0, 7)

grid[knight_position] = 1
grid[goal_position] = 2

print(grid)



