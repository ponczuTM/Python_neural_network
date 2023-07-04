import numpy as np
from tkinter import *
from tkinter import messagebox
import os
from f import draw, square, triangle, circle, vertical_line, cross, star  # Import funkcji z pliku "f.py"

os.system("cls")  # Czyszczenie konsoli

class NN(object):
    def __init__(self, size):
        self.shape = (size, size, 2)  # Przechowywanie kształtu sieci
        ss = np.empty(self.shape)
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                ss[x, y] = [(x + 0.5) / self.shape[0], (y + 0.5) / self.shape[1]]
        self.ss = ss  # Inicjalizacja macierzy ss (punkty na siatce)
        self.sigma = 0.8  # Skupienie punktów
        self.alpha = 0.2  # Przeskoki w 2D
        self.beta = 500  # Wartość beta
        self.data = []  # Przechowywanie danych treningowych

    def train(self, data):
        epochs = 25
        self.data = data.copy()
        for epoch in range(1, epochs):
            idx = np.random.choice(range(len(self.data)))  # Losowy indeks danych treningowych
            list_neurons = []
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    dist = np.linalg.norm(self.data[idx] - self.ss[x, y])  # Obliczanie odległości między danymi treningowymi a punktami siatki
                    list_neurons.append(((x, y), dist))
            list_neurons.sort(key=lambda param: param[1])  # Sortowanie neuronów według odległości
           # od teraz PIERWSZY neuron jest tym "najlepszym"
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    dist = np.linalg.norm(np.array(list_neurons[0][0]) - np.array([x, y]))  # Obliczanie odległości do najlepszego neuronu
                    self.updatecell((x, y), self.data[idx], epoch, dist)  # Aktualizacja komórki

    def updatecell(self, cell, dp, number, dist):
        self.ss[cell] += self.alpha * np.exp(-(number / self.beta)) * np.exp(-dist ** 2 / (2 * self.sigma ** 2))  * (dp - self.ss[cell])  # Aktualizacja komórki sieci
        #self.alpha: Wartość początkowa współczynnika uczenia. Kontroluje, jak szybko wagi komórek sieci będą się aktualizować w trakcie treningu. Im wyższa wartość self.alpha, tym większe będą zmiany wag komórek
        #number: Aktualna iteracja treningu. Wykorzystywana do skalowania współczynnika uczenia wraz ze wzrostem liczby iteracji.
        #self.beta: Parametr kontrolujący tempo spadku wartości współczynnika uczenia wraz ze wzrostem iteracji. Im większa wartość self.beta, tym wolniej będzie maleć współczynnik uczenia.
        #dist: Odległość między aktualną komórką a najlepszym neuronem (najbliższym sąsiadem). Im mniejsza odległość, tym większy wpływ na aktualizację wagi komórki.
        #self.sigma: Parametr kontrolujący skupienie punktów. Im większa wartość self.sigma, tym większy obszar wpływu punktów sąsiadujących na aktualizację komórki.

class Gui(object):
    def __init__(self):
        self.size = 10  # Rozmiar siatki NEURONÓW
        self.window = Tk()  # Inicjalizacja głównego okna
        self.width = 600  # Szerokość okna
        self.height = 600  # Wysokość okna
        self.window.geometry(f"{self.width}x{self.height}")  # Ustawienie rozmiaru okna
        self.canvas = Canvas(self.window, width=self.width, height=self.height, highlightbackground="black", bg="black")  # Inicjalizacja ekranu
        self.inputs = []  # Przechowywanie danych wejściowych
        self.nn = NN(self.size)  # Inicjalizacja sieci neuronowej
        self.build()  # Tworzenie interfejsu
        self.window.mainloop()  # Rozpoczęcie pętli głównego okna

    def build(self):
        response = messagebox.askquestion("Wybór", "Czy chcesz mieć wyświetloną siatkę punktów?")  # Wyświetlenie pytania w okienku dialogowym
        if response == "yes":
            interval = int(600 / self.size)  # Obliczenie interwału na podstawie liczby punktów
            draw(self)  # Wywołanie funkcji draw do rysowania punktów
            for i in range(40, self.width, interval):
                for j in range(40, self.height, interval):
                    self.draw_point([i,j], "yellow", "red")  # Rysowanie punktów siatki
        with open('figure.txt', 'r') as file:
            figure = file.read().strip()  # Odczytanie zawartości pliku "figure.txt" i usunięcie białych znaków

        if figure == "square":
            square(self)  # Wywołanie funkcji do rysowania kwadratu
        elif figure == "triangle":
            triangle(self)  # Wywołanie funkcji do rysowania trójkąta
        elif figure == "circle":
            circle(self)  # Wywołanie funkcji do rysowania okręgu
        elif figure == "vertical_line":
            vertical_line(self)  # Wywołanie funkcji do rysowania linii pionowej
        elif figure == "cross":
            cross(self)  # Wywołanie funkcji do rysowania krzyża
        elif figure == "star":
            star(self)  # Wywołanie funkcji do rysowania gwiazdy
        else:
            print("Zła zawartość pliku figure.txt: ",figure)
            exit(0)  # Wyjście z programu, gdy zawartość pliku figure.txt jest nieprawidłowa

        self.canvas.bind("<ButtonRelease-1>", lambda event: self.kohonen())  # Powiązanie zdarzenia zwolnienia przycisku myszy, które wywołuje self.kohonen()
        self.canvas.grid()  # Wyświetlenie płótna na ekranie

    def kohonen(self):
        self.nn = NN(self.size)  # Inicjalizacja sieci neuronowej
        self.nn.ss *= [self.width, self.height]  # Skalowanie punktów siatki
        while True:
            self.nn.train(np.array(self.inputs))  # Trening sieci neuronowej
            self.canvas.delete("all")  # Usunięcie wszystkich elementów z płótna
            for j in self.inputs:
                self.draw_point(j, "darkgray", "darkgray")  # Rysowanie punktów danych wejściowych
            for i in range(self.size): #rysowanie siatki neuronowej
                for j in range(self.size):
                    if j < self.size - 1:
                        x, y = self.nn.ss[i, j]
                        x2, y2 = self.nn.ss[i, j + 1]
                        offsets = [(0, 0), (0.5, 0), (-0.5, 0), (0, 0.5), (0, -0.5)]
                        for offset in offsets:
                            self.canvas.create_line(x + offset[0], y + offset[1], x2 + offset[0], y2 + offset[1], fill="cyan")  # Rysowanie linii
                    if i < self.size - 1:
                        x, y = self.nn.ss[i, j]
                        x2, y2 = self.nn.ss[i + 1, j]
                        offsets = [(0, 0), (0.5, 0), (-0.5, 0), (0, 0.5), (0, -0.5)]
                        for offset in offsets:
                            self.canvas.create_line(x + offset[0], y + offset[1], x2 + offset[0], y2 + offset[1], fill="cyan")  # Rysowanie linii
                    self.draw_point(self.nn.ss[i, j], "yellow", "red")  # Rysowanie punktów
            self.canvas.update()  # Aktualizacja płótna

    def draw_point(self, point, color, color2):
        x, y = point[0], point[1]
        self.canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill=color, outline=color2)  # Rysowanie punktu

understand = messagebox.askquestion("ROZUMIESZ?", "Możliwy wybór figur w figure.txt to:\n- square\n- triangle\n- circle\n- vertical_line\n- cross\n- star\n\nRozumiesz?")
if understand == "yes":
    Gui()
else:
    exit(0)  # Wyjście z programu, gdy użytkownik nie rozumie