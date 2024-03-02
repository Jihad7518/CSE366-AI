
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
