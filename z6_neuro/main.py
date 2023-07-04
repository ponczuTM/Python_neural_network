import os
import numpy as np
from PIL import Image as img_reader
from tkinter import *
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
import random
os.system("cls")

class HopfieldNetwork(object):
    def __init__(self):
        # Inicjalizacja sieci Hopfielda
        self.size = 2500  # Liczba neuronów w sieci = 50x50
        self.weights = np.zeros((self.size, self.size))  # Macierz wag pomiędzy neuronami
        self.num_patterns = 0  # Liczba wzorców uczących
        self.iterations = 500  # Liczba iteracji dla algorytmu Glaubera
        self.e = 0  # Energia aktualnego stanu sieci

    def glauber_dynamic(self, state):
        # Algorytm Glaubera dla dynamicznego modelu sieci Hopfielda
        self.e = self.energy(state)  # Obliczenie energii początkowego stanu sieci
        for _ in range(self.iterations):
            for _ in range(self.iterations):
                random_neuron = np.random.randint(0, self.size)  # Losowy wybór neuronu do aktualizacji
                state[random_neuron] = np.sign(np.dot(self.weights[random_neuron], state))  # Aktualizacja stanu neuronu
            e_after = self.energy(state)  # Obliczenie energii po aktualizacji
            if e_after == self.e:  # Sprawdzenie, czy osiągnięto stabilny stan
                return state
            self.e = e_after
            #print(self.e)
        return state

    def plot_weights(self):
        plt.figure(figsize=(5, 5)) #nowa figura
        plt.colorbar(plt.imshow(self.weights, cmap=cm.coolwarm)) #  pasek kolorów do wykresu, który wizualizuje wagi
        plt.tight_layout() # Dostosowanie układu wykresu
        #plt.savefig("weights.png")
        plt.show()

    def energy(self, state):
        return state.dot(self.weights).dot(state)
        # Obliczanie energii w sieci Hopfielda
        # Obliczamy iloczyn skalarny stanu (state) i macierzy wag (self.weights)
        # dot(state, self.weights) - wykonuje iloczyn skalarny między stanem a macierzą wag
        # dot(self.weights, state) - wykonuje iloczyn skalarny między transponowaną macierzą wag a stanem
        # dot(state, self.weights).dot(state) - wykonuje dwukrotne przemnożenie iloczynu skalarnego
        # stanu i macierzy wag przez siebie samego

    def training(self, training_data):
        # Trenowanie sieci Hopfielda
        self.num_patterns = len(training_data)  # Liczba wzorców treningowych
        weight_matrix = np.zeros((self.size, self.size))  # Inicjalizacja macierzy wag
        rho = np.sum([np.sum(pattern) for pattern in training_data]) / (self.num_patterns * self.size)
        # Obliczenie współczynnika rho, który jest średnią sumą wartości pikseli we wszystkich wzorcach treningowych
        # Reguła Hebba
        for i in range(self.num_patterns):
            training_pattern = training_data[i] - rho  # Skorygowanie wzorca treningowego o wartość rho
            weight_matrix += np.outer(training_pattern, training_pattern)  # Obliczenie zewnętrznego iloczynu wzorca treningowego z samym sobą i dodanie go do macierzy wag
        diagW = np.diag(np.diag(weight_matrix))
        # Diagonalna macierz wag
        weight_matrix = weight_matrix - diagW
        # Odjęcie diagonali od macierzy wag
        weight_matrix /= self.num_patterns
        # Podzielenie macierzy wag przez liczbę wzorców treningowych
        self.weights = weight_matrix.copy()
        # Przypisanie zaktualizowanej macierzy wag do atrybutu weights w sieci Hopfielda



class Gui(object):
    def __init__(self):
        self.hn = HopfieldNetwork()
        # Inicjalizacja obiektu sieci Hopfielda o rozmiarze 50x50 (2500 neuronów)
        self.data = self.read_images()
        # Wczytanie danych obrazów, które będą wykorzystane do trenowania sieci
        self.root = Tk()
        # Inicjalizacja głównego okna interfejsu GUI
        self.buttons = {}
        # Inicjalizacja słownika przycisków
        self.array = np.zeros((50, 50)) - 1
        # Inicjalizacja tablicy o wymiarach 50x50, która będzie przechowywać stan pikseli
        self.build_buttons()
        # Utworzenie przycisków w interfejsie GUI
        self.canvas = Canvas(self.root, width=300, height=300, highlightthickness=1, highlightbackground="black")
        # Utworzenie płótna na którym będą wyświetlane wyniki
        self.canvas.grid(row=0, column=0, columnspan=100)
        # Umieszczenie płótna w oknie GUI
        self.clear()
        # Inicjalizacja stanu płótna (wyczyszczenie pikseli)
        self.root.mainloop()
        # Uruchomienie głównej pętli interfejsu GUI

    def learn_all_patterns(self):
        for picture in range (8):
            self.set(picture)
            #for _ in range (5):
            self.train()
        self.clear()
        
    def train(self):
        # Wyczyszczenie ekranu (dotyczy systemu Windows)
        self.hn = HopfieldNetwork()
        # Inicjalizacja obiektu sieci Hopfielda o rozmiarze 50x50 (2500 neuronów)
        training_data = [np.reshape(i, (50 * 50)) for i in self.data]
        # Przekształcenie danych treningowych na odpowiedni format (tablica 1D) wymagany przez sieć Hopfielda
        self.hn.training(training_data)
        # Trenowanie sieci Hopfielda na podstawie danych treningowych

    def glauber(self):
        for _ in range (30):
            test_input = np.reshape(self.array, (50 * 50))
            # Przekształcenie stanu tablicy na format 1D, który może być użyty jako wejście dla sieci Hopfielda
            test_output = self.hn.glauber_dynamic(test_input)
            # Wykonanie procesu dynamicznego Glaubera na podstawie wejścia i otrzymanie wynikowego stanu
            self.array = np.reshape(test_output, (50, 50))
            # Przekształcenie wynikowego stanu z powrotem na format 2D (50x50)
            self.color()
            # Aktualizacja wyglądu graficznego na podstawie wynikowego stanu tablicy
            time.sleep(0.5)

    def draw_point(self, point, color):
        x0 = point[0] * 300 / 50
        y0 = point[1] * 300 / 50
        x1 = x0 + 300 / 50
        y1 = y0 + 300 / 50
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        # Tworzenie prostokąta na płótnie o podanych współrzędnych i kolorze.
        # Ta metoda służy do rysowania punktów (kwadratów) na płótnie w celu wizualizacji stanu tablicy


    def build_buttons(self):
        self.buttons[0] = Button(self.root, text="Clear canvas", width=16, height=2, bg="white", command=lambda: self.clear())
        self.buttons[0].grid(row=1, column=0)
        self.buttons[1] = Button(self.root, text="Negative canvas", width=16, height=2, bg="white", command=lambda: self.neg())
        self.buttons[1].grid(row=1, column=1)
        self.buttons[3] = Button(self.root, text="Learn all patterns", width=16, height=2, bg="white", command=lambda: self.learn_all_patterns())
        self.buttons[3].grid(row=1, column=3)
        self.buttons[4] = Button(self.root, text="Glauber", width=16, height=2, bg="white", command=lambda: self.glauber())
        self.buttons[4].grid(row=1, column=4)
        self.buttons[5] = Button(self.root, text="-----------------", width=16, height=2, bg="white")
        self.buttons[5].grid(row=3, column=2)
        self.buttons[6] = Button(self.root, text="Robot", width=16, height=2, bg="white", command=lambda picture=0: self.set(picture))
        self.buttons[6].grid(row=4, column=0)
        self.buttons[7] = Button(self.root, text="+", width=16, height=2, bg="white", command=lambda picture=1: self.set(picture))
        self.buttons[7].grid(row=4, column=1)
        self.buttons[8] = Button(self.root, text="Góry", width=16, height=2, bg="white", command=lambda picture=2: self.set(picture))
        self.buttons[8].grid(row=4, column=2)
        self.buttons[9] = Button(self.root, text="X", width=16, height=2, bg="white", command=lambda picture=3: self.set(picture))
        self.buttons[9].grid(row=4, column=3)
        self.buttons[10] = Button(self.root, text="Zegar", width=16, height=2, bg="white", command=lambda picture=4: self.set(picture))
        self.buttons[10].grid(row=4, column=4)
        self.buttons[11] = Button(self.root, text="Kapelusz", width=16, height=2, bg="white", command=lambda picture=5: self.set(picture))
        self.buttons[11].grid(row=5, column=1)
        self.buttons[12] = Button(self.root, text="Kubek", width=16, height=2, bg="white", command=lambda picture=6: self.set(picture))
        self.buttons[12].grid(row=5, column=2)
        self.buttons[13] = Button(self.root, text="Snake", width=16, height=2, bg="white", command=lambda picture=7: self.set(picture))
        self.buttons[13].grid(row=5, column=3)
        self.buttons[14] = Button(self.root, text="Noise image", width=16, height=2, bg="white", command=lambda: self.noise())
        self.buttons[14].grid(row=2, column=1)
        self.buttons[15] = Button(self.root, text="show plot", width=16, height=2, bg="white", command=lambda: self.plot_show())
        self.buttons[15].grid(row=2, column=3)

    def color(self):
        self.canvas.delete("all")
        # Usunięcie wszystkich elementów z płótna, aby odświeżyć wygląd
        for j in range(50):
            for i in range(50):
                if self.array[i, j] == -1:
                    # Jeśli wartość piksela w tablicy to -1, oznacza to brak koloru (biały)
                    self.draw_point([i, j], "white")
                else:
                    # Jeśli wartość piksela to inna liczba, oznacza to obecność koloru (czarny)
                    self.draw_point([i, j], "black")
                self.canvas.update()
        # Przejście przez wszystkie piksele tablicy, rysowanie odpowiedniego koloru dla każdego piksela
        # Wywołanie metody draw_point dla każdego piksela w celu rysowania kwadratu na płótnie
        # Odświeżenie płótna, aby wyświetlić zmiany

    def read_images(self):
        images = []
        # Inicjalizacja listy, która będzie przechowywać wczytane obrazy
        for i in range(8):
            name = f"{i}.png"
            # Nazwa pliku obrazu do wczytania
            image = img_reader.open('Images/' + name)
            # Wczytanie obrazu z pliku
            resized_image = image.resize((50, 50)) #, img_reader.ANTIALIAS
            # Zmiana rozmiaru obrazu na 50x50 pikseli
            image_array = np.array(resized_image)
            # Konwersja obrazu na tablicę NumPy
            points = np.zeros((50, 50)) - 1
            # Inicjalizacja tablicy, która będzie przechowywać informacje o punktach obrazu
            for y in range(len(image_array)):
                for x in range(len(image_array[y])):
                    if (image_array[x][y] == 0).any():
                        # Jeśli jakakolwiek wartość piksela w kanale koloru (RGB) jest równa 0,
                        # oznacza to, że piksel ma kolor i należy go zaznaczyć jako 1 w tablicy punktów
                        points[x][y] = 1
            images.append(points)
        # Przetworzenie obrazu na tablicę punktów, w której 1 oznacza piksel kolorowy, a -1 oznacza piksel biały
        return images
        # Zwrócenie listy wczytanych obrazów jako tablic punktów


    def noise(self):
        for i in range(50):
            for j in range(50):
                noise = random.randint(5, 60)
                if ((i + j) % noise == 0) and i>1 and j>1:
                    self.array[i, j] *= -1
        self.color()

    def neg(self):
        for j in range(50):
            for i in range(50):
                self.array[i, j] *= (-1)
        self.color()

    def set(self, picture):
        self.array = np.array(self.data[picture])
        self.color()

    def clear(self):
        self.array = np.zeros((50, 50)) - 1
        self.color()

    def plot_show(self):
        self.hn.plot_weights()

gui = Gui()