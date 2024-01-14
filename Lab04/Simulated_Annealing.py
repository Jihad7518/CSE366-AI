
import math
import random

class SimulatedAnnealing:
    def __init__(self, problem_size):
        self.problem_size = problem_size
        self.current_solution = [random.randint(0, 1) for _ in range(problem_size)]
        self.current_value = self.evaluate(self.current_solution)
        self.temperature = 1.0
        self.cooling_rate = 0.95

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

    def acceptance_probability(self, new_value):
        if new_value > self.current_value:
            return 1.0
        return math.exp((new_value - self.current_value) / self.temperature)

    def simulated_annealing(self):
        while self.temperature > 0.1:
            new_solution = random.choice(self.get_neighbors(self.current_solution))
            new_value = self.evaluate(new_solution)

            if random.random() < self.acceptance_probability(new_value):
                self.current_solution = new_solution
                self.current_value = new_value

            self.temperature *= self.cooling_rate

    def print_result(self):
        print("Best Solution:", self.current_solution)
        print("Best Value:", self.current_value)

if __name__ == "__main__":
    problem_size = 10
    sa_instance = SimulatedAnnealing(problem_size)

    print("Initial Solution:", sa_instance.current_solution)
    print("Initial Value:", sa_instance.current_value)

    sa_instance.simulated_annealing()

    print("\nAfter Simulated Annealing:")
    sa_instance.print_result()
