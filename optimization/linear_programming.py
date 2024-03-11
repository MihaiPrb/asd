from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus
from utils.logger import logger

class LinearProgramming:
    def __init__(self, config):
        self.solver = config['solver']
        self.timeout = config['timeout']

    def optimize(self, data, constraints, objectives):
        try:
            # Create a new linear programming problem
            problem = LpProblem("Supply_Chain_Optimization", LpMinimize)

            # Define decision variables
            variables = self._create_variables(data)

            # Define objective function
            objective = self._create_objective(variables, objectives)
            problem.setObjective(objective)

            # Add constraints to the problem
            self._add_constraints(problem, variables, constraints)

            # Solve the linear programming problem
            problem.solve(solver=self.solver, timeLimit=self.timeout)

            # Check the status of the solution
            if LpStatus[problem.status] == 'Optimal':
                # Retrieve the optimal solution
                solution = self._get_solution(variables)
                objective_value = problem.objective.value()

                optimization_result = {
                    'solution': solution,
                    'objective_value': objective_value
                }

                return optimization_result
            else:
                logger.warning("Linear programming problem could not be solved optimally.")
                return None
        except Exception as e:
            logger.error(f"Error occurred during linear programming optimization: {str(e)}")
            raise e

    def _create_variables(self, data):
        variables = {}
        for _, row in data.iterrows():
            variable_name = f"x_{row['source']}_{row['destination']}"
            variable = LpVariable(variable_name, lowBound=0, cat='Continuous')
            variables[variable_name] = variable
        return variables

    def _create_objective(self, variables, objectives):
        objective = lpSum(objectives.get_cost(var_name) * variable for var_name, variable in variables.items())
        return objective

    def _add_constraints(self, problem, variables, constraints):
        # Add supply constraints
        for constraint in constraints.supply_constraints:
            problem.addConstraint(
                lpSum(variables[var_name] for var_name in constraint['variables']) <= constraint['value']
            )

        # Add demand constraints
        for constraint in constraints.demand_constraints:
            problem.addConstraint(
                lpSum(variables[var_name] for var_name in constraint['variables']) >= constraint['value']
            )

        # Add capacity constraints
        for constraint in constraints.capacity_constraints:
            problem.addConstraint(
                lpSum(variables[var_name] for var_name in constraint['variables']) <= constraint['value']
            )

    def _get_solution(self, variables):
        solution = {}
        for var_name, variable in variables.items():
            solution[var_name] = variable.value()
        return solution