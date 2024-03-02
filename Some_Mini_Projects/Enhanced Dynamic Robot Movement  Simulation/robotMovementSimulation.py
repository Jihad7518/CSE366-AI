
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import heapq

class Environment:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.grid = np.zeros((n, m))
        self.start_position = None
        self.end_position = None
        self.obstacles = []

    def add_obstacle(self, position):
        self.obstacles.append(position)

    def set_start_position(self, position):
        if self.is_valid_position(position):
            self.start_position = position
            self.grid[position[0], position[1]] = 2  # Representing start position as 2

    def set_end_position(self, position):
        if self.is_valid_position(position):
            self.end_position = position
            self.grid[position[0], position[1]] = 3  # Representing end position as 3

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < self.n and 0 <= y < self.m

    def generate_grid(self):
        return self.grid
class Robot:
    def __init__(self, environment, start_position):
        self.environment = environment
        self.position = start_position
        self.energy = 100
        self.valid_moves = []  # Initialize an empty list for valid moves

    def move(self, direction):
        x, y = self.position
        dx, dy = direction
        new_x, new_y = x + dx, y + dy

        if self.is_valid_move((new_x, new_y)):
            self.position = (new_x, new_y)
            self.energy -= 1  # Decrease energy by 1 for each movement
            self.valid_moves.append((new_x, new_y))  # Store valid moves
            return True
        else:
             # Obstacle encountered, recalculate path using A* and choose an alternative move
             optimal_path = pathfinder.find_path(self.position, self.environment.end_position)
             if optimal_path:
                next_position = optimal_path[0]  # Next position after recalculating path
                self.position = next_position
                self.energy -= 1
                self.valid_moves.append(next_position)
                return True
             else:
                # No valid path found, stay in the same position
                return False
