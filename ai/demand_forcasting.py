from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from utils.logger import logger
from data.data_preprocessor import preprocess_data
from utils.feature_selection import select_features
from utils.hyperparameter_tuning import tune_hyperparameters
from utils.model_evaluation import evaluate_model

class DemandForecasting:
    def __init__(self, config):
        self.config = config
        self.model = None

    def train(self, data):
        try:
            # Preprocess the data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Perform feature selection
            selected_features, target = select_features(preprocessed_data, self.config['feature_selection'])

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                selected_features, target, test_size=self.config['test_size'], random_state=self.config['random_state']
            )

            # Create and train the demand forecasting model
            self.model = RandomForestRegressor(random_state=self.config['random_state'])

            # Perform hyperparameter tuning
            best_params = tune_hyperparameters(self.model, X_train, y_train, self.config['hyperparameter_tuning'])
            self.model.set_params(**best_params)

            # Train the model with the best hyperparameters
            self.model.fit(X_train, y_train)

            # Evaluate the model
            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            evaluation_metrics = {
                'mean_squared_error': mse,
                'mean_absolute_error': mae,
                'r2_score': r2
            }

            # Log the evaluation metrics
            logger.info(f"Demand forecasting model evaluation metrics: {evaluation_metrics}")

            logger.info("Demand forecasting model trained successfully")
        except Exception as e:
            logger.error(f"Error occurred while training the demand forecasting model: {str(e)}")
            raise e

    def forecast(self, data):
        try:
            # Preprocess the input data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features
            selected_features = select_features(preprocessed_data, self.config['feature_selection'], target=False)

            # Make demand forecasts using the trained model
            demand_forecasts = self.model.predict(selected_features)

            return demand_forecasts
        except Exception as e:
            logger.error(f"Error occurred while making demand forecasts: {str(e)}")
            raise e

    def evaluate(self, data):
        try:
            # Preprocess the evaluation data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features and target
            selected_features, target = select_features(preprocessed_data, self.config['feature_selection'])

            # Evaluate the demand forecasting model
            evaluation_metrics = evaluate_model(self.model, selected_features, target)

            # Log the evaluation metrics
            logger.info(f"Demand forecasting model evaluation metrics on new data: {evaluation_metrics}")

            return evaluation_metrics
        except Exception as e:
            logger.error(f"Error occurred while evaluating the demand forecasting model: {str(e)}")
            raise e