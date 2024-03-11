import numpy as np

class Constraints:
    def __init__(self, constraints_data):
        self.supply_constraints = constraints_data['supply_constraints']
        self.demand_constraints = constraints_data['demand_constraints']
        self.capacity_constraints = constraints_data['capacity_constraints']

    def is_feasible(self, solution):
        # Check if the solution satisfies all the constraints
        if not self._check_supply_constraints(solution):
            return False
        if not self._check_demand_constraints(solution):
            return False
        if not self._check_capacity_constraints(solution):
            return False
        return True

    def generate_random_solution(self, data):
        # Generate a random feasible solution based on the problem data and constraints
        solution = np.random.uniform(low=0, high=1, size=len(data))
        while not self.is_feasible(solution):
            solution = np.random.uniform(low=0, high=1, size=len(data))
        return solution

    def _check_supply_constraints(self, solution):
        for constraint in self.supply_constraints:
            total_supply = sum(solution[var_index] for var_index in constraint['variable_indices'])
            if total_supply > constraint['value']:
                return False
        return True

    def _check_demand_constraints(self, solution):
        for constraint in self.demand_constraints:
            total_demand = sum(solution[var_index] for var_index in constraint['variable_indices'])
            if total_demand < constraint['value']:
                return False
        return True

    def _check_capacity_constraints(self, solution):
        for constraint in self.capacity_constraints:
            total_flow = sum(solution[var_index] for var_index in constraint['variable_indices'])
            if total_flow > constraint['value']:
                return False
        return True