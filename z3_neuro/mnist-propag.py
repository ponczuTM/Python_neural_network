from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import os
import time
os.system("cls")

def ladowanie_danych():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape((x_train.shape[0], -1)) / 255.
    x_test = x_test.reshape((x_test.shape[0], -1)) / 255.
    return x_train, y_train, x_test, y_test

# definicja funkcji aktywacji
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# definicja pochodnej funkcji aktywacji do obliczania propagacji wstecznej
def sigmoid_derivative(x):
    return x * (1 - x)

def train(x_train, y_train, batch_size, hidden_layer_size, learning_rate, epochs):
    input_size = x_train.shape[1]
    output_size = len(np.unique(y_train))

    # Inicjalizacja wag warstw ukrytej i wyjściowej
    w1 = np.random.randn(input_size, hidden_layer_size)
    w2 = np.random.randn(hidden_layer_size, output_size)

    # Kodowanie wartości y metodą one hot encoding
    y_train_encoded = OneHotEncoder().fit_transform(y_train.reshape(-1, 1)).toarray()

    # Trenowanie sieci w oparciu o batche
    start_time = time.time()  # Początkowy czas
    for epoch in range(epochs):
        #if(epoch ==20 ):
        #    learning_rate = 0.001
        print(f"Epoka {epoch+1}")
        for i in range(0, x_train.shape[0], batch_size):
            x_batch = x_train[i:i+batch_size]
            y_batch = y_train_encoded[i:i+batch_size]

            #obliczanie wag i wyjść warstw ukrytej i wyjściowej
            hidden_layer_input = np.dot(x_batch, w1)
            hidden_layer_output = sigmoid(hidden_layer_input)
            output_layer_input = np.dot(hidden_layer_output, w2)
            output_layer_output = sigmoid(output_layer_input)

            # Błąd
            error = y_batch - output_layer_output

            # Wsteczna propagacja
            delta_output = error * sigmoid_derivative(output_layer_output)
            delta_hidden = np.dot(delta_output, w2.T) * sigmoid_derivative(hidden_layer_output)

            # Aktualizacja wag
            w2 += np.dot(hidden_layer_output.T, delta_output) * learning_rate
            w1 += np.dot(x_batch.T, delta_hidden) * learning_rate

        # obliczamy skuteczność po każdej epoce
        y_pred = predict(x_train, w1, w2)
        train_accuracy = accuracy_score(y_train, y_pred)
        print(f"Train accuracy: {train_accuracy:.2f}")
    end_time = time.time()  # Końcowy czas
    duration = end_time - start_time  # Obliczanie czasu trwania uczenia
    print(f"Training duration: {duration:.2f} seconds")
    return w1, w2

# fukcja do obliczania wyjścia naszej sieci
def predict(x, w1, w2):
    hidden_layer_input = np.dot(x, w1)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, w2)
    output_layer_output = sigmoid(output_layer_input)
    return np.argmax(output_layer_output, axis=1)

#ładujemy dane
x_train, y_train,x_test, y_test = ladowanie_danych()

# przeprowadzamy trening
w1, w2 = train(x_train, y_train, batch_size=32, hidden_layer_size=64, learning_rate=0.02, epochs=40)

# testujemy sieć
y_pred = predict(x_test, w1, w2)
test_accuracy = accuracy_score(y_test, y_pred)
print(f'Test accuracy: {test_accuracy*100:.2f}%')