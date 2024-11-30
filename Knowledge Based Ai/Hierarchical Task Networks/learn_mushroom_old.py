import json
import csv
import numpy as np

class LearningSystem(object):
    def __init__(self, learning_rate=0.01, epochs=30000, hidden_units=32, dropout_rate=0.2):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.hidden_units = hidden_units
        self.dropout_rate = dropout_rate
        self.weights_hidden = None
        self.bias_hidden = None
        self.weights_output = None
        self.bias_output = None
        self.encoded_mapping = None

    def _create_feature_mapping(self, dataset):
        feature_values = {}
        for instance in dataset:
            for key, value in instance.items():
                if key not in feature_values:
                    feature_values[key] = set()
                feature_values[key].add(value)

        encoded_mapping = {}
        for key, values in feature_values.items():
            encoded_mapping[key] = {v: idx for idx, v in enumerate(sorted(values))}
        
        self.encoded_mapping = encoded_mapping

    def _encode_features(self, dataset):
        if self.encoded_mapping is None:
            raise ValueError("Feature mapping not found. Make sure to call _create_feature_mapping first.")
        
        total_encoded_length = sum(len(values) for values in self.encoded_mapping.values())
        encoded_data = []

        for instance in dataset:
            encoded_instance = [0] * total_encoded_length
            current_index = 0
            for key, values in self.encoded_mapping.items():
                if key in instance:
                    value = instance[key]
                    if value in self.encoded_mapping[key]:
                        index = current_index + self.encoded_mapping[key][value]
                        encoded_instance[index] = 1
                current_index += len(self.encoded_mapping[key])
            encoded_data.append(encoded_instance)

        return np.array(encoded_data)

    def _apply_dropout(self, X):
        mask = np.random.rand(*X.shape) > self.dropout_rate
        scale_factor = 1.0 / (1.0 - self.dropout_rate)
        return X * mask * scale_factor

    def _relu(self, X):
        return np.maximum(0, X)

    def _softmax(self, X):
        exp_scores = np.exp(X - np.max(X, axis=1, keepdims=True))  # for numerical stability
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    def fit(self, train_set, train_labels):
        self._create_feature_mapping(train_set)
        X = self._encode_features(train_set)
        y = np.array(train_labels)

        num_features = X.shape[1]
        num_classes = len(set(y))

        # Initialize weights and biases for hidden and output layers
        self.weights_hidden = np.random.randn(num_features, self.hidden_units) * np.sqrt(2 / num_features)  # He initialization
        self.bias_hidden = np.zeros(self.hidden_units)
        self.weights_output = np.random.randn(self.hidden_units, num_classes) * np.sqrt(2 / self.hidden_units)  # He initialization
        self.bias_output = np.zeros(num_classes)

        for epoch in range(self.epochs):
            # Forward pass through the hidden layer
            X_dropout = self._apply_dropout(X)
            hidden_layer_linear = np.dot(X_dropout, self.weights_hidden) + self.bias_hidden
            hidden_layer_activation = self._relu(hidden_layer_linear)  # ReLU activation

            # Forward pass through the output layer
            scores = np.dot(hidden_layer_activation, self.weights_output) + self.bias_output
            probs = self._softmax(scores)  # Softmax activation

            # Compute the loss (cross-entropy)
            correct_logprobs = -np.log(probs[range(len(y)), y])
            loss = np.sum(correct_logprobs) / len(y)

            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")

            # Backpropagation
            dscores = probs
            dscores[range(len(y)), y] -= 1
            dscores /= len(y)

            # Gradients for output layer
            dW_output = np.dot(hidden_layer_activation.T, dscores)
            db_output = np.sum(dscores, axis=0)

            # Backpropagate through ReLU
            dhidden = np.dot(dscores, self.weights_output.T)
            dhidden[hidden_layer_linear <= 0] = 0

            # Gradients for hidden layer
            dW_hidden = np.dot(X_dropout.T, dhidden)
            db_hidden = np.sum(dhidden, axis=0)

            # Update weights and biases with learning rate decay
            self.weights_output -= self.learning_rate * dW_output
            self.bias_output -= self.learning_rate * db_output
            self.weights_hidden -= self.learning_rate * dW_hidden
            self.bias_hidden -= self.learning_rate * db_hidden

    def predict(self, instance):
        X = self._encode_features([instance])

        # Forward pass through hidden layer
        hidden_layer_linear = np.dot(X, self.weights_hidden) + self.bias_hidden
        hidden_layer_activation = self._relu(hidden_layer_linear)  # ReLU activation

        # Forward pass through output layer
        scores = np.dot(hidden_layer_activation, self.weights_output) + self.bias_output
        probs = self._softmax(scores)  # Softmax activation
        return np.argmax(probs)

def define_model():
    return LearningSystem()

def load_training_data(csv_path):
    training_data = []
    training_labels = []
    with open(csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            label = int(row.pop('label'))  # Assuming 'label' column is the class label
            training_labels.append(label)
            training_data.append(row)
    return training_data, training_labels

def align_features(sample_data, training_data):
    sample_keys = set(sample_data[0].keys())
    training_keys = set(training_data[0].keys())
    
    missing_in_sample = training_keys - sample_keys
    extra_in_sample = sample_keys - training_keys

    for instance in sample_data:
        for key in missing_in_sample:
            instance[key] = 'missing'  # Use a default value like 'missing'

    for instance in training_data:
        for key in extra_in_sample:
            if key in instance:
                del instance[key]

if __name__ == "__main__":
    # Load training data from CSV
    train_set, train_labels = load_training_data('mushroom_trainingdataset.csv')

    # Load sample data for testing
    sample_set_data = json.load(open('hw3-sample_set_data.json'))
    sample_set_labels = json.load(open('hw3-sample_set_labels.json'))

    # Align features between training and sample datasets
    align_features(sample_set_data, train_set)

    # Initialize and train the model
    model = define_model()
    model.fit(train_set, train_labels)

    # Test the model on the sample set
    correct = sum([model.predict(sample_set_data[i]) == sample_set_labels[i] for i in range(len(sample_set_data))])
    accuracy = correct / len(sample_set_data)
    print("Accuracy on Sample Set:", accuracy)



# """
# The following codes are for testing with sample data only.
# REMEMBER TO REMOVE THEM BEFORE SUBMISSION.
# =============================================================================
# In this homework, a sample collection of shuffled data is provided.
# You might try with the data provided like in the following before submission:
# """

# def test(model, test_set_data, test_labels):
# 	correct = 0
# 	for i in range(len(test_set_data)):
# 		pred = model.predict(test_set_data[i])
# 		if pred == test_labels[i]:
# 			correct += 1
# 	accuracy = correct / len(test_set_data)
# 	return accuracy

# sample_set_data = json.load(open('hw3-sample_set_data.json'))
# sample_set_labels = json.load(open('hw3-sample_set_labels.json'))

# train_set = sample_set_data[:-500]
# train_labels = sample_set_labels[:-500]
# test_set = sample_set_data[-500:]
# test_labels = sample_set_labels[-500:]

# model = define_model()
# model.fit(train_set, train_labels)
# print("Accuracy:", test(model, test_set, test_labels))




