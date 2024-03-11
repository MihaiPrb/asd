class Objectives:
    def __init__(self, objectives_data):
        self.cost_coefficients = objectives_data['cost_coefficients']
        self.emission_coefficients = objectives_data['emission_coefficients']
        self.time_coefficients = objectives_data['time_coefficients']

    def evaluate(self, solution):
        cost = self._calculate_cost(solution)
        emissions = self._calculate_emissions(solution)
        time = self._calculate_time(solution)

        # Normalize the objective values
        normalized_cost = self._normalize(cost)
        normalized_emissions = self._normalize(emissions)
        normalized_time = self._normalize(time)

        # Calculate the weighted sum of objectives
        weighted_sum = (
            self.cost_coefficients['weight'] * normalized_cost +
            self.emission_coefficients['weight'] * normalized_emissions +
            self.time_coefficients['weight'] * normalized_time
        )

        return weighted_sum

    def _calculate_cost(self, solution):
        total_cost = 0
        for var_name, value in solution.items():
            cost = self.cost_coefficients['values'].get(var_name, 0)
            total_cost += cost * value
        return total_cost

    def _calculate_emissions(self, solution):
        total_emissions = 0
        for var_name, value in solution.items():
            emissions = self.emission_coefficients['values'].get(var_name, 0)
            total_emissions += emissions * value
        return total_emissions

    def _calculate_time(self, solution):
        total_time = 0
        for var_name, value in solution.items():
            time = self.time_coefficients['values'].get(var_name, 0)
            total_time += time * value
        return total_time

    def _normalize(self, value):
        # Implement normalization logic based on your specific requirements
        # This could involve scaling the values to a specific range or using statistical normalization techniques
        # Example placeholder implementation:
        normalized_value = value / 100
        return normalized_value