
import numpy as np
class Neuron:
    def __init__(self, weights, bias, func):
        self.weights = np.array(weights)
        self.bias = bias

        self.activation_function = func

        if self.activation_function not in ["relu", "sigmoid", "tanh"]:
            raise ValueError("Función de activación no válida.")

        self.activation_functions = {
            "relu": self._relu,
            "sigmoid": self._sigmoid,
            "tanh": self._tanh
        }

    @staticmethod
    def _relu(x):
        return np.maximum(0, x)

    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def _tanh(x):
        return np.tanh(x)

    def _activate(self, x):
        activation_function = self.activation_functions.get(self.activation_function)
        if activation_function is not None:
            return activation_function(x)
        else:
            raise ValueError("Función de activación no válida.")

    def run(self, input_data):
        weighted_sum = np.dot(self.weights, input_data) + self.bias
        output = self._activate(weighted_sum)
        return output

    def change_weights(self, new_weights):
        self.weights = np.array(new_weights)

    def change_bias(self, new_bias):
        self.bias = new_bias