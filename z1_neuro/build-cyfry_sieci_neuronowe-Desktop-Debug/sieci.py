import os
import numpy as np
import random

# Pętla While do GUI
while True:
    
    class Perceptron:
        def __init__(self, input_shape, output_shape):
            # Inicjalizacja wagi i biasu sieci jako losowe wartości z rozkładu normalnego.
            self.weights = np.random.randn(input_shape, output_shape)
            self.biases = np.random.randn(output_shape)
            wew=0

        def activation_function(self, x):
            # Definicja funkcji aktywacji - prosta funkcja skokowa.
            o = 1 * (x >= 0)
            return o

        def forward(self, inputs):
            # Propagacja w przód (feedforward) - obliczenie wyjścia sieci dla danego wejścia.
            linear_output = np.dot(inputs, self.weights) + self.biases
            return self.activation_function(linear_output)

        def train(self, inputs, outputs, learning_rate,epochs):
            # Trenowanie sieci za pomocą algorytmu perceptronu.
            for epoch in range(epochs):
                # Propagacja w przód.
                predictions = self.forward(inputs)
                # Obliczenie błędów dla każdego przypadku treningowego.
                errors = outputs - predictions

                # Aktualizacja wag i biasu.
                self.weights = self.weights + learning_rate * np.dot(inputs.T, errors)
                self.biases = self.biases + learning_rate * np.sum(errors, axis=0)


    class PocketPerceptron:
        def __init__(self, input_shape, output_shape):
            # Inicjalizacja wagi i biasu sieci jako losowe wartości z rozkładu normalnego.
            self.weights = np.random.randn(input_shape, output_shape)
            self.biases = np.random.randn(output_shape)
            # Zapisanie najlepszych wag i biasu.
            self.best_weights = np.copy(self.weights)
            self.best_biases = np.copy(self.biases)
            # Zapisanie najlepszej dokładności.
            self.best_accuracy = 0

        def step_function(self, x):
            # Definicja funkcji aktywacji - prosta funkcja skokowa.
            return 1 * (x >= 0)
            
        def forward(self, inputs):
            # Propagacja w przód (feedforward) - obliczenie wyjścia sieci dla danego wejścia.
            linear_output = np.dot(inputs, self.weights) + self.biases
            return self.step_function(linear_output)

        def train(self, inputs, outputs, learning_rate, epochs):
            # Trenowanie sieci za pomocą algorytmu perceptronu z kieszenią.
            for epoch in range(epochs):
                # Propagacja w przód.
                predictions = self.forward(inputs)
                # Obliczenie błędów dla każdego przypadku treningowego.
                errors = outputs - predictions
                # Aktualizacja wag i biasu.
                self.weights = self.weights + learning_rate * np.dot(inputs.T, errors)
                self.biases = self.biases + learning_rate * np.sum(errors, axis=0)
        
                # Sprawdzenie dokładności modelu.
                accuracy = self.evaluate(inputs, outputs)
                # Jeśli dokładność jest lepsza, zapisujemy najlepsze wagi, bias i dokładność.
                if accuracy > self.best_accuracy:
                    self.best_accuracy = accuracy
                    self.best_weights = np.copy(self.weights)
                    self.best_biases = np.copy(self.biases)
            # Przypisanie najlepszych wag i obciążeń do aktualnych wag i obciążeń
            self.weights = self.best_weights
            self.biases = self.best_biases
        # Metoda obliczająca dokładność modelu na podstawie danych wejściowych i oczekiwanych wyjść
        def evaluate(self, inputs, outputs):
            predictions = self.forward(inputs)
            return np.mean(np.argmax(predictions, axis=1) == np.argmax(outputs, axis=1))

    num_classes = 10
    # Pobranie danych treningowych
    X_train = []
    y_train = []
    for i in range(num_classes):
        directory = f"trening/{i}"
        for filename in os.listdir(directory):

            if filename.endswith(".txt"):
                with open(os.path.join(directory, filename), "r") as f:
                    data = f.read().splitlines()
                digit_array = []
                for line in data:
                    row = [int(x) for x in line.split(",")]
                    digit_array = digit_array + row
                X_train.append(digit_array)
                y_train.append(i)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    y_train = np.eye(num_classes)[y_train]

    # Utworzenie nowego modelu PocketPerceptron
    model = PocketPerceptron(input_shape=X_train.shape[1], output_shape=10)

    epochs = 50
    learning_rate = 0.2

    # Trenowanie modelu na danych treningowych
    model.train(X_train, y_train, learning_rate,epochs)

    input_filename = "input.txt"
    X_test = []
    # Pobranie danych testowych
    with open(input_filename, "r") as f:
        data = f.read().splitlines()
    digit_array = []
    for line in data:
        row = [int(x) for x in line.split(",")]
        digit_array = digit_array + row
    X_test.append(digit_array)

    X_test = np.array(X_test)

    # Obliczenie przewidywanych cyfr dla danych testowych
    predictions = model.forward(X_test)
    predicted_digits = np.argmax(predictions, axis=1)

    # Zapisanie przewidywanych cyfr do pliku output.txt
    with open("output.txt", "w") as f:
        for digit in predicted_digits:
            f.write(str(digit))