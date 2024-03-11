import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from utils.logger import logger
from utils.data_preprocessing import preprocess_data
from utils.distance_matrix import create_distance_matrix

class RouteOptimization:
    def __init__(self, config):
        self.config = config

    def optimize_routes(self, data):
        try:
            # Preprocess the data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Create distance matrix
            distance_matrix = create_distance_matrix(preprocessed_data, self.config['distance_metric'])

            # Create routing index manager
            manager = pywrapcp.RoutingIndexManager(len(distance_matrix), self.config['num_vehicles'], self.config['depot'])

            # Create routing model
            routing = pywrapcp.RoutingModel(manager)

            # Create and register transit callback
            def distance_callback(from_index, to_index):
                from_node = manager.IndexToNode(from_index)
                to_node = manager.IndexToNode(to_index)
                return distance_matrix[from_node][to_node]

            transit_callback_index = routing.RegisterTransitCallback(distance_callback)

            # Set cost of each arc
            routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

            # Set search parameters
            search_parameters = pywrapcp.DefaultRoutingSearchParameters()
            search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

            # Solve the problem
            solution = routing.SolveWithParameters(search_parameters)

            # Get optimized routes
            optimized_routes = []
            for vehicle_id in range(self.config['num_vehicles']):
                index = routing.Start(vehicle_id)
                route = []
                while not routing.IsEnd(index):
                    node_index = manager.IndexToNode(index)
                    route.append(node_index)
                    index = solution.Value(routing.NextVar(index))
                node_index = manager.IndexToNode(index)
                route.append(node_index)
                optimized_routes.append(route)

            # Calculate total distance
            total_distance = solution.ObjectiveValue()

            # Log the results
            logger.info(f"Optimized routes: {optimized_routes}")
            logger.info(f"Total distance: {total_distance}")

            return optimized_routes, total_distance
        except Exception as e:
            logger.error(f"Error occurred while optimizing routes: {str(e)}")
            raise e