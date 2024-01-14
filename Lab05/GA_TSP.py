import random
import math

class GeneticAlgorithmTSP:
    def __init__(self, cities, population_size):
        self.cities = cities
        self.population_size = population_size
        self.population = self.initialize_population()

    def initialize_population(self):
        return [random.sample(self.cities, len(self.cities)) for _ in range(self.population_size)]

    def evaluate_fitness(self, tour):
        # Calculate the total distance of the tour
        total_distance = sum(self.distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_distance += self.distance(tour[-1], tour[0])  # Return to the starting city
        return 1 / total_distance  # Fitness is the reciprocal of the total distance

    def distance(self, city1, city2):
        # Euclidean distance between two cities
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def select_parents(self):
        # Select parents using tournament selection
        tournament_size = 2
        parents = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            parent = max(tournament, key=self.evaluate_fitness)
            parents.append(parent)
        return parents

    def crossover(self, parent1, parent2):
        # Perform ordered crossover
        crossover_point1 = random.randint(0, len(parent1) - 1)
        crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))

        child1 = parent1[crossover_point1:crossover_point2] + [city for city in parent2 if city not in parent1[crossover_point1:crossover_point2]]
        child2 = parent2[crossover_point1:crossover_point2] + [city for city in parent1 if city not in parent2[crossover_point1:crossover_point2]]

        return child1, child2

    def mutate(self, tour, mutation_rate):
        # Perform swap mutation
        mutated_tour = tour.copy()
        for _ in range(len(tour)):
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(tour)), 2)
                mutated_tour[idx1], mutated_tour[idx2] = mutated_tour[idx2], mutated_tour[idx1]
        return mutated_tour

    def genetic_algorithm(self, generations, mutation_rate):
        for _ in range(generations):
            parents = self.select_parents()
            new_population = []

            for i in range(0, self.population_size, 2):
                parent1, parent2 = parents[i], parents[i + 1]
                child1, child2 = self.crossover(parent1, parent2)

                child1 = self.mutate(child1, mutation_rate)
                child2 = self.mutate(child2, mutation_rate)

                new_population.extend([child1, child2])

            self.population = new_population

    def print_result(self):
        best_tour = max(self.population, key=self.evaluate_fitness)
        best_fitness = self.evaluate_fitness(best_tour)
        print("Best Tour Order:", best_tour)
        print("Best Fitness:", best_fitness)

if __name__ == "__main__":
    cities = [(23.8103, 90.4125), (22.7010, 90.3535), (21.4272, 92.0056),
              (24.8956, 91.8687), (25.7439, 89.2752), (23.1699, 89.2137)]

    population_size = 10
    generations = 50
    mutation_rate = 0.01

    ga_instance = GeneticAlgorithmTSP(cities, population_size)

    print("Initial Population Order:", ga_instance.population)

    ga_instance.genetic_algorithm(generations, mutation_rate)

    print("\nAfter Genetic Algorithm:")
    ga_instance.print_result()

