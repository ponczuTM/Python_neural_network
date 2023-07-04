
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
# definicja jednostki Adaline
class Adaline:
    def __init__(self, input_size):

        self.weights = np.zeros(input_size + 1)
        self.training_errors = [] #historia błędów


    def predict(self, input_vector):
        sum = np.dot(input_vector, self.weights[1:]) + self.weights[0]
        return np.where(sum >= 0.0, 1, -1)
    
    # Jeśli zastosujemy funkcję sigmoidalną to accuracy się zmniejszy
    # Zastosowanie funkcji sigmoidalnej sprawi, że model staje się nieliniowy. 
    # To oznacza, że nie możemy już używać prostego algorytmu uczenia, który był używany wcześniej. 
    # Musielibyśmy zastosować bardziej zaawansowane metody uczenia.
    
    def train(self, input_vector, target, epochs, learning_rate, batch_size=10):
        for _ in range(epochs):
            for batch_index in range(0, input_vector.shape[0], batch_size):
                batch_x = input_vector[batch_index:batch_index + batch_size]
                batch_y = target[batch_index:batch_index + batch_size]

                output = self.predict(batch_x)
                errors = batch_y - output
                self.weights[1:] += learning_rate * np.dot(errors, batch_x)
                self.weights[0] += learning_rate * errors.sum()
                if len(self.training_errors)<10: # interesują nas tylko błędy w pierszych epokach bo potem już się nieznacznie zmieniają
                    self.training_errors.append(np.mean(errors**2))

        return self

# rysowanie wykresu historii błędów dla wszystkich jednostek adaline
def wykres(adalines):
    root = tk.Tk()
    width_px = root.winfo_screenwidth()
    height_px = root.winfo_screenheight()
    root.destroy()
    dpi = 100
    width = width_px / dpi
    height = height_px / dpi
    accuracy = 100.0
    mean = 0
    number = 0
    weight=2
    fig = plt.figure(figsize=(width, height))
    for i, adaline in enumerate(adalines):
        plt.plot(range(1, len(adaline.training_errors) + 1), adaline.training_errors, marker='o', label=f'Adaline {i}')
        for i, error in enumerate(adaline.training_errors):
            plt.annotate(f'{error:.2f}', xy=(i+1, error), ha='center', va='bottom')
            mean = mean + (error * weight)  # Zastosowanie wagi dla błędu
            number = number + 1
    mean = mean / (number)
    accuracy = accuracy - mean
    print(f'Accuracy: {accuracy}%')
    plt.xlabel('Epoki')
    plt.ylabel('Średni błąd')
    plt.legend()
    ax = plt.gca()
    ax.set_xticks(range(1, len(adaline.training_errors) + 1))
    ax.set_xticklabels(range(1, len(adaline.training_errors) + 1))
    plt.show()
    


def ladowanie_danych():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape((x_train.shape[0], -1)) / 255.
    x_test = x_test.reshape((x_test.shape[0], -1)) / 255.
    return x_train, y_train, x_test, y_test

def trening():
    x_train, y_train, _, _ = ladowanie_danych()
    adalines = []
    for i in range(10):
        print (f"Trening jednostki {i}")
        adaline = Adaline(input_size=x_train.shape[1])
        binary_y_train = np.where(y_train == i, 1, -1)   # ta jednostka adaline ma zajmować się tylko liczbą i
        adaline.train(x_train, binary_y_train, epochs=10, learning_rate=0.01)
        adalines.append(adaline)
    return adalines

def testy(adalines):
    print("Testy")
    _, _, x_test, y_test = ladowanie_danych()
    correct_predictions = 0
    for i in range(len(x_test)):
        predictions = [adaline.predict(x_test[i]) for adaline in adalines]
        if np.argmax(predictions) == y_test[i]:
            correct_predictions += 1

adalines = trening()
testy(adalines)
wykres(adalines)