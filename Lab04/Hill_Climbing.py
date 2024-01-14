import random

class HillClimbing:
    def __init__(self, problem_size):
        self.problem_size = problem_size
        self.current_solution = [random.randint(0, 1) for _ in range(problem_size)]
        self.current_value = self.evaluate(self.current_solution)

    def evaluate(self, solution):
        # Example problem: Count the number of ones in the binary string
        return sum(solution)

    def get_neighbors(self, solution):
        neighbors = []
        for i in range(len(solution)):
            neighbor = solution.copy()
            neighbor[i] = 1 - neighbor[i]  # Flip 0 to 1 and vice versa
            neighbors.append(neighbor)
        return neighbors

    def hill_climbing(self):
        while True:
            neighbors = self.get_neighbors(self.current_solution)
            best_neighbor = max(neighbors, key=self.evaluate)

            if self.evaluate(best_neighbor) <= self.current_value:
                # Local maximum reached or plateau, terminate
                break

            self.current_solution = best_neighbor
            self.current_value = self.evaluate(best_neighbor)

    def print_result(self):
        print("Best Solution:", self.current_solution)
        print("Best Value:", self.current_value)

if __name__ == "__main__":
    problem_size = 10
    hill_climbing_instance = HillClimbing(problem_size)

    print("Initial Solution:", hill_climbing_instance.current_solution)
    print("Initial Value:", hill_climbing_instance.current_value)

    hill_climbing_instance.hill_climbing()

    print("\nAfter Hill Climbing:")
    hill_climbing_instance.print_result()

