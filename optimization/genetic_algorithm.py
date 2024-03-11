import numpy as np
from utils.logger import logger

class GeneticAlgorithm:
    def __init__(self, config):
        self.population_size = config['population_size']
        self.num_generations = config['num_generations']
        self.crossover_rate = config['crossover_rate']
        self.mutation_rate = config['mutation_rate']
        self.elite_size = config['elite_size']
        self.tournament_size = config['tournament_size']

    def optimize(self, data, constraints, objectives):
        try:
            # Initialize the population
            population = self._initialize_population(data, constraints)

            # Evaluate the fitness of the initial population
            fitness_values = self._evaluate_fitness(population, objectives)

            for generation in range(self.num_generations):
                logger.info(f"Generation {generation + 1}")

                # Select parents for reproduction
                parents = self._select_parents(population, fitness_values)

                # Perform crossover to create offspring
                offspring = self._crossover(parents)

                # Perform mutation on the offspring
                offspring = self._mutate(offspring)

                # Evaluate the fitness of the offspring
                offspring_fitness = self._evaluate_fitness(offspring, objectives)

                # Combine the population and offspring
                combined_population = np.concatenate((population, offspring))
                combined_fitness = np.concatenate((fitness_values, offspring_fitness))

                # Select the best individuals for the next generation
                population, fitness_values = self._select_next_generation(combined_population, combined_fitness)

            # Get the best solution from the final population
            best_solution_index = np.argmin(fitness_values)
            best_solution = population[best_solution_index]
            best_objective_value = fitness_values[best_solution_index]

            optimization_result = {
                'solution': best_solution,
                'objective_value': best_objective_value
            }

            return optimization_result
        except Exception as e:
            logger.error(f"Error occurred during genetic algorithm optimization: {str(e)}")
            raise e

    def _initialize_population(self, data, constraints):
        population = []
        for _ in range(self.population_size):
            individual = constraints.generate_random_solution(data)
            population.append(individual)
        return np.array(population)

    def _evaluate_fitness(self, population, objectives):
        fitness_values = []
        for individual in population:
            fitness = objectives.evaluate(individual)
            fitness_values.append(fitness)
        return np.array(fitness_values)

    def _select_parents(self, population, fitness_values):
        parents = []
        for _ in range(self.population_size):
            tournament_indices = np.random.choice(len(population), size=self.tournament_size, replace=False)
            tournament_fitness = fitness_values[tournament_indices]
            winner_index = tournament_indices[np.argmin(tournament_fitness)]
            parents.append(population[winner_index])
        return np.array(parents)

    def _crossover(self, parents):
        offspring = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            if np.random.rand() < self.crossover_rate:
                crossover_point = np.random.randint(1, len(parent1))
                child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
                child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
                offspring.append(child1)
                offspring.append(child2)
            else:
                offspring.append(parent1)
                offspring.append(parent2)
        return np.array(offspring)

    def _mutate(self, offspring):
        mutated_offspring = []
        for individual in offspring:
            if np.random.rand() < self.mutation_rate:
                mutation_point = np.random.randint(len(individual))
                individual[mutation_point] = np.random.uniform(low=0, high=1)
            mutated_offspring.append(individual)
        return np.array(mutated_offspring)

    def _select_next_generation(self, combined_population, combined_fitness):
        elite_indices = np.argsort(combined_fitness)[:self.elite_size]
        elite_population = combined_population[elite_indices]
        elite_fitness = combined_fitness[elite_indices]

        remaining_indices = np.argsort(combined_fitness)[self.elite_size:]
        remaining_population = combined_population[remaining_indices]
        remaining_fitness = combined_fitness[remaining_indices]

        selected_indices = np.random.choice(len(remaining_population), size=self.population_size - self.elite_size, replace=False)
        selected_population = remaining_population[selected_indices]
        selected_fitness = remaining_fitness[selected_indices]

        next_generation = np.concatenate((elite_population, selected_population))
        next_generation_fitness = np.concatenate((elite_fitness, selected_fitness))

        return next_generation, next_generation_fitness