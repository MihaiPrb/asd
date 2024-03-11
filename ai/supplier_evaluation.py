from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from utils.logger import logger
from utils.data_preprocessing import preprocess_data
from utils.feature_selection import select_features
from utils.hyperparameter_tuning import tune_hyperparameters
from utils.model_evaluation import evaluate_classification_model

class SupplierEvaluation:
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

            # Create and train the supplier evaluation model
            self.model = RandomForestClassifier(random_state=self.config['random_state'])

            # Perform hyperparameter tuning
            best_params = tune_hyperparameters(self.model, X_train, y_train, self.config['hyperparameter_tuning'])
            self.model.set_params(**best_params)

            # Train the model with the best hyperparameters
            self.model.fit(X_train, y_train)

            # Evaluate the model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)

            evaluation_metrics = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1
            }

            # Log the evaluation metrics
            logger.info(f"Supplier evaluation model evaluation metrics: {evaluation_metrics}")

            logger.info("Supplier evaluation model trained successfully")
        except Exception as e:
            logger.error(f"Error occurred while training the supplier evaluation model: {str(e)}")
            raise e

    def evaluate_supplier(self, data):
        try:
            # Preprocess the input data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features
            selected_features = select_features(preprocessed_data, self.config['feature_selection'], target=False)

            # Evaluate supplier using the trained model
            supplier_evaluation = self.model.predict(selected_features)

            return supplier_evaluation
        except Exception as e:
            logger.error(f"Error occurred while evaluating supplier: {str(e)}")
            raise e

    def evaluate(self, data):
        try:
            # Preprocess the evaluation data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features and target
            selected_features, target = select_features(preprocessed_data, self.config['feature_selection'])

            # Evaluate the supplier evaluation model
            evaluation_metrics = evaluate_classification_model(self.model, selected_features, target)

            # Log the evaluation metrics
            logger.info(f"Supplier evaluation model evaluation metrics on new data: {evaluation_metrics}")

            return evaluation_metrics
        except Exception as e:
            logger.error(f"Error occurred while evaluating the supplier evaluation model: {str(e)}")
            raise e