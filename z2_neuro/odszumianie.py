import os
import numpy as np
import cv2
import time
import pyautogui

# Czyszczenie ekranu konsoli
os.system("cls")

# Katalog, w którym znajdują się obrazki
img_dir = "obrazki"

# Klasa sieci neuronowej z pojedynczą warstwą liniową
class LinearNeuralNetwork:
    def __init__(self, input_size, output_size):
        # Inicjalizacja wag i biasu
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.bias = np.zeros(output_size)
        # Stała szybkości uczenia się
        self.learning_rate = 0.001

    # Metoda przepływu w przód
    def forward(self, x):
        return np.dot(x, self.weights) + self.bias

    # Metoda wstecznej propagacji
    def backprop(self, x, y_true, y_pred):
        errors = 2 * (y_pred - y_true)
        weights_d = np.outer(x, errors)
        bias_d = errors
        return weights_d, bias_d

    # Metoda aktualizacji wag
    def update_weights(self, grad_weights, grad_bias):
        self.weights = self.weights - self.learning_rate * grad_weights
        self.bias = self.bias - self.learning_rate * grad_bias

# Funkcja dodająca szum gaussowski do obrazka
def apply_noise(img):
    indices = np.random.choice(img.shape[0], 50, replace=False)
    noised_img = img.copy()
    noised_img[indices] = 1
    return noised_img

# Funkcja testująca sieć
# Funkcja wczytuje obrazek o numerze i, zaszumia go i zapisuje odszumiony obrazek
def test(i,epoch=-1):
    # Wczytuje obrazek i przekształca go do jednowymiarowej tablicy wartości pikseli
    img = cv2.imread(f"{img_dir}/img{i}.jpg", cv2.IMREAD_GRAYSCALE)
    img = img / 255
    img = img.flatten()

    # Dodaje szum do obrazka
    noised_image = apply_noise(img)

    # Oblicza wyjście sieci dla zaszumionego obrazka
    v = nn.forward(noised_image)

    # Proguje wyjście i przekształca do formatu obrazka
    v = np.where(v < 0.5, 0, v)  
    v = np.where(v >= 0.5, 1, v)
    v = v.reshape(50, 50) * 255    
    noised_image = noised_image.reshape(50, 50) * 255
    
    # Zapisuje obrazki
    cv2.imwrite(f"{img_dir}/noised{i}.jpg", noised_image)
    if epoch >= 0:
        filename = f"{img_dir}/denoised{i}_epoch{epoch}.jpg"
    else:
        filename = f"{img_dir}/denoised{i}.jpg"

    # Wyświetla przetworzony obrazek
    cv2.imwrite(filename, cv2.resize(v, (50, 50)))
    cv2.imshow("Denoised Image", cv2.resize(v, (500, 500)))
    cv2.waitKey(1500)
    cv2.destroyAllWindows()

# Wyświetla menu wyboru obrazka
print("1. domek")
print("2. gwiazda")
print("3. okrąg")
print("4. komputer")
print("5. X")
# Wczytuje obrazki
num = int(input("Wybierz numer obrazka: "))
if(num < 1 or num > 5):
    print("zastanow sie co robisz")
    exit(0)
images = []
noised_images = []

# Wczytuje wybrane obrazki do listy i równocześnie tworzy listę zaszumionych obrazków do treningu
for i in range(1,6):
    img = cv2.imread(f'{img_dir}/img{i}.jpg', cv2.IMREAD_GRAYSCALE)
    img = img / 255
    img = img.flatten()
    images.append(img)
    noised_images.append(apply_noise(img))

images = np.array(images)
noised_images = np.array(noised_images)

#Tworzy sieć neuronową
nn = LinearNeuralNetwork(50*50, 50*50)

#Ustawia rozmiar batcha i dzieli dane na partie
batch_size = 2
batches = range(0, len(images), batch_size)

#Uczy sieć przez 30 epok
for epoch in range(30):  
    epoch_losses = []
    for batch_start in batches:
        batch_end = min(batch_start + batch_size, len(images))
        batch_noised = noised_images[batch_start:batch_end]
        batch_images = images[batch_start:batch_end]

        batch_grad_weights = np.zeros_like(nn.weights)
        batch_grad_bias = np.zeros_like(nn.bias)

        # Przeprowadza wsteczną propagację i oblicza gradienty
        for i in range(len(batch_noised)):
            output = nn.forward(batch_noised[i])
            grad_weights, grad_bias = nn.backprop(batch_noised[i], batch_images[i], output)
            batch_grad_weights += grad_weights
            batch_grad_bias += grad_bias
            loss = np.mean((output - batch_images[i])**2)
            epoch_losses.append(loss)

        # Aktualizacja wag po każdym batchu
        nn.update_weights(batch_grad_weights/len(batch_noised), batch_grad_bias/len(batch_noised))

    epoch_loss = np.mean(epoch_losses)
    print(f'Epoka {epoch+1}, błąd: {epoch_loss}')
    if epoch%5==0:
        test(num,epoch)

#Testuje sieć na wybranym obrazku
test(num) 
