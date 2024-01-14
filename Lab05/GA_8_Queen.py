import random

class GeneticAlgorithm8Queens:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = self.initialize_population()

    def initialize_population(self):
        return [random.randint(0, 63) for _ in range(self.population_size)]

    def evaluate_fitness(self, chromosome):
        # Count the number of conflicts (queens attacking each other)
        conflicts = 0
        for i in range(7):
            for j in range(i + 1, 8):
                if chromosome[i] == chromosome[j] or \
                        chromosome[i] - i == chromosome[j] - j or \
                        chromosome[i] + i == chromosome[j] + j:
                    conflicts += 1
        return 28 - conflicts  # Maximum fitness is 28 (no conflicts)

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
        crossover_point = random.randint(1, 7)
        child1 = (parent1 & (255 << crossover_point)) | (parent2 & (255 >> (8 - crossover_point)))
        child2 = (parent2 & (255 << crossover_point)) | (parent1 & (255 >> (8 - crossover_point)))
        return child1, child2

    def mutate(self, chromosome, mutation_rate):
        # Perform bit-flip mutation
        for i in range(8):
            if random.random() < mutation_rate:
                bit_mask = 1 << i
                chromosome ^= bit_mask
        return chromosome

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
        print("Best Solution:", bin(best_solution)[2:].zfill(8))
        print("Best Fitness:", best_fitness)

if __name__ == "__main__":
    population_size = 10
    generations = 50
    mutation_rate = 0.01

    ga_instance = GeneticAlgorithm8Queens(population_size)

    print("Initial Population:", [bin(chromosome)[2:].zfill(8) for chromosome in ga_instance.population])

    ga_instance.genetic_algorithm(generations, mutation_rate)

    print("\nAfter Genetic Algorithm:")
    ga_instance.print_result()

