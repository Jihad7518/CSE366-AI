import random

class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.population = self.initialize_population()

    def initialize_population(self):
        return [''.join(random.choice('01') for _ in range(self.chromosome_length))
                for _ in range(self.population_size)]

    def evaluate_fitness(self, chromosome):
        return sum(int(bit) for bit in chromosome)

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
        # Perform single-point crossover
        crossover_point = random.randint(1, self.chromosome_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, chromosome, mutation_rate):
        # Perform bit-flip mutation
        mutated_chromosome = ''.join(
            bit if random.random() > mutation_rate else random.choice('01')
            for bit in chromosome
        )
        return mutated_chromosome

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
        best_solution = max(self.population, key=self.evaluate_fitness)
        best_fitness = self.evaluate_fitness(best_solution)
        print("Best Solution:", best_solution)
        print("Best Fitness:", best_fitness)

if __name__ == "__main__":
    population_size = 6
    chromosome_length = 10
    generations = 50
    mutation_rate = 0.01

    ga_instance = GeneticAlgorithm(population_size, chromosome_length)

    print("Initial Population:", ga_instance.population)

    ga_instance.genetic_algorithm(generations, mutation_rate)

    print("\nAfter Genetic Algorithm:")
    ga_instance.print_result()

