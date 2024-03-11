from optimization.genetic_algorithm import GeneticAlgorithm
from optimization.linear_programming import LinearProgramming
from optimization.constraints import Constraints
from optimization.objectives import Objectives
from utils.performance_metrics import calculate_performance_metrics
from utils.logger import logger
from utils.visualizer import Visualizer

class Optimizer:
    def __init__(self, config):
        self.config = config
        self.constraints = None
        self.objectives = None
        self.ga_optimizer = None
        self.lp_optimizer = None
        self.visualizer = Visualizer(config['visualization'])

    def set_constraints(self, constraints_data):
        try:
            self.constraints = Constraints(constraints_data)
            logger.info("Constraints set successfully")
        except Exception as e:
            logger.error(f"Error occurred while setting constraints: {str(e)}")
            raise e

    def set_objectives(self, objectives_data):
        try:
            self.objectives = Objectives(objectives_data)
            logger.info("Objectives set successfully")
        except Exception as e:
            logger.error(f"Error occurred while setting objectives: {str(e)}")
            raise e

    def initialize_optimizers(self):
        try:
            self.ga_optimizer = GeneticAlgorithm(self.config['genetic_algorithm'])
            self.lp_optimizer = LinearProgramming(self.config['linear_programming'])
            logger.info("Optimizers initialized successfully")
        except Exception as e:
            logger.error(f"Error occurred while initializing optimizers: {str(e)}")
            raise e

    def optimize(self, data):
        try:
            # Set constraints and objectives based on the data
            self.set_constraints(data['constraints'])
            self.set_objectives(data['objectives'])

            # Initialize optimizers
            self.initialize_optimizers()

            # Run optimization
            optimization_result, performance_metrics = self.run_optimization(data)

            logger.info("Optimization completed successfully")
            return optimization_result, performance_metrics
        except Exception as e:
            logger.error(f"Error occurred during optimization: {str(e)}")
            raise e

    def run_optimization(self, data):
        try:
            # Run genetic algorithm optimization
            ga_result = self.ga_optimizer.optimize(data, self.constraints, self.objectives)

            # Run linear programming optimization
            lp_result = self.lp_optimizer.optimize(data, self.constraints, self.objectives)

            # Combine optimization results
            optimization_result = self._combine_results(ga_result, lp_result)

            # Calculate performance metrics
            performance_metrics = calculate_performance_metrics(optimization_result, data)

            # Visualize the optimization results
            self.visualizer.plot_optimization_results(optimization_result, performance_metrics)

            return optimization_result, performance_metrics
        except Exception as e:
            logger.error(f"Error occurred during optimization: {str(e)}")
            raise e

    def _combine_results(self, ga_result, lp_result):
        # Extract the objective function values from the optimization results
        ga_objective_value = ga_result['objective_value']
        lp_objective_value = lp_result['objective_value']

        # Compare the objective function values to determine the best solution
        if ga_objective_value < lp_objective_value:
            best_solution = ga_result['solution']
            best_objective_value = ga_objective_value
            best_algorithm = 'Genetic Algorithm'
        else:
            best_solution = lp_result['solution']
            best_objective_value = lp_objective_value
            best_algorithm = 'Linear Programming'

        # Create the combined optimization result
        combined_result = {
            'best_solution': best_solution,
            'best_objective_value': best_objective_value,
            'best_algorithm': best_algorithm,
            'ga_result': ga_result,
            'lp_result': lp_result
        }

        return combined_result