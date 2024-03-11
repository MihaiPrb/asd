from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from utils.logger import logger
from utils.data_preprocessing import preprocess_data
from utils.feature_selection import select_features
from utils.model_evaluation import evaluate_anomaly_detection

class AnomalyDetection:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = StandardScaler()

    def train(self, data):
        try:
            # Preprocess the data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Perform feature selection
            selected_features, _ = select_features(preprocessed_data, self.config['feature_selection'])

            # Scale the selected features
            scaled_features = self.scaler.fit_transform(selected_features)

            # Create and train the anomaly detection model
            self.model = IsolationForest(n_estimators=self.config['n_estimators'],
                                         max_samples=self.config['max_samples'],
                                         contamination=self.config['contamination'],
                                         random_state=self.config['random_state'])
            self.model.fit(scaled_features)

            logger.info("Anomaly detection model trained successfully")
        except Exception as e:
            logger.error(f"Error occurred while training the anomaly detection model: {str(e)}")
            raise e

    def detect_anomalies(self, data):
        try:
            # Preprocess the input data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features
            selected_features = select_features(preprocessed_data, self.config['feature_selection'], target=False)

            # Scale the selected features
            scaled_features = self.scaler.transform(selected_features)

            # Detect anomalies using the trained model
            anomaly_scores = self.model.decision_function(scaled_features)
            anomaly_labels = self.model.predict(scaled_features)

            # Create a DataFrame with anomaly scores and labels
            anomaly_results = selected_features.copy()
            anomaly_results['anomaly_score'] = anomaly_scores
            anomaly_results['is_anomaly'] = anomaly_labels

            # Filter and return the anomalous data points
            anomalies = anomaly_results[anomaly_results['is_anomaly'] == -1]

            return anomalies
        except Exception as e:
            logger.error(f"Error occurred while detecting anomalies: {str(e)}")
            raise e

    def evaluate(self, data):
        try:
            # Preprocess the evaluation data
            preprocessed_data = preprocess_data(data, self.config['preprocessing'])

            # Select the relevant features
            selected_features = select_features(preprocessed_data, self.config['feature_selection'], target=False)

            # Scale the selected features
            scaled_features = self.scaler.transform(selected_features)

            # Evaluate the anomaly detection model
            evaluation_metrics = evaluate_anomaly_detection(self.model, scaled_features, self.config['contamination'])

            # Log the evaluation metrics
            logger.info(f"Anomaly detection model evaluation metrics: {evaluation_metrics}")

            return evaluation_metrics
        except Exception as e:
            logger.error(f"Error occurred while evaluating the anomaly detection model: {str(e)}")
            raise e