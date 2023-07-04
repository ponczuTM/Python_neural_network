#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <fstream>
#include <QFile>
#include <QTextStream>
#include <windows.h>
#include <cstdlib>
#include <unistd.h>

int choice = 0;

MainWindow::MainWindow(QWidget * parent): QMainWindow(parent), ui(new Ui::MainWindow) {
    ui -> setupUi(this);

    startX = ui -> frame -> x();
    startY = ui -> frame -> y();

    width = ui -> frame -> width();
    height = ui -> frame -> height();

    img = new QImage(width, height, QImage::Format_RGB32);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::paintEvent(QPaintEvent * ) {
    QPainter p(this);

    p.drawImage(startX, startY, * img);
}

void MainWindow::clean() {}

void MainWindow::drawPixel(int x, int y, unsigned char red, unsigned char green, unsigned char blue) {
    unsigned char * wsk;

    if (x >= 0 && y >= 0 && x < width && y < height) {
        wsk = img -> scanLine(y);

        wsk[4 * x] = blue;
        wsk[4 * x + 1] = green;
        wsk[4 * x + 2] = red;
    }
}

void MainWindow::wpisz() {
    std::ofstream plik("input.txt", std::ios_base::trunc);

    czytajKolorPixela(50, 50);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 50);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 50);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 50);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 50);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 150);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 150);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 150);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 150);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 150);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 250);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 250);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 250);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 250);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 250);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 350);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 350);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 350);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 350);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 350);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 450);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 450);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 450);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 450);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 450);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 550);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 550);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 550);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 550);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 550);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik << "\n";

    czytajKolorPixela(50, 650);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(150, 650);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(250, 650);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(350, 650);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0,";
    } else {
        plik << "1,";
    }

    czytajKolorPixela(450, 650);
    if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
        plik << "0";
    } else {
        plik << "1";
    }

    plik.close();
}

void MainWindow::mousePressEvent(QMouseEvent * event) {
    Qt::MouseButtons mouseButtons = event -> buttons();
    if (mouseButtons == Qt::LeftButton) {
        x0 = event -> pos().x() - startX;
        y0 = event -> pos().y() - startY;
        floodFill(x0, y0);
        wpisz();
        QString filePath = "output.txt"; // ścieżka do pliku
        QFile file(filePath);
        if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
            qWarning() << "Nie udało się otworzyć pliku!";
            return; // albo obsłużyć błąd
        }
        Sleep(150);
        QTextStream in ( & file);
        QString fileContent = in.readAll();
        file.close();
        std::string fileContentStr = fileContent.toStdString();
        update();
        qDebug() << "Widzę cyfrę: " << fileContentStr.c_str() << "\n";
    } else if (mouseButtons == Qt::RightButton) {
        x0 = event -> pos().x() - startX;
        y0 = event -> pos().y() - startY;
        floodFill2(x0, y0);
        Sleep(100);
        wpisz();
        QString filePath = "output.txt"; // ścieżka do pliku
        QFile file(filePath);
        if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
            qWarning() << "Nie udało się otworzyć pliku!";
            return; // albo obsłużyć błąd
        }

        QTextStream in ( & file);
        QString fileContent = in.readAll();
        file.close();
        std::string fileContentStr = fileContent.toStdString();
        update();
        qDebug() << "Widzę cyfrę: " << fileContentStr.c_str() << "\n";
    }

    std::ifstream inputFile("output.txt"); // otwarcie pliku do odczytu
    int show; // zmienna, do której zostanie zapisana liczba całkowita

    if (inputFile.is_open()) {
        std::string fileContentStr;
        getline(inputFile, fileContentStr); // odczytanie zawartości pliku do łańcucha znaków
        show = std::stoi(fileContentStr); // konwersja łańcucha znaków na liczbę całkowitą
    }

    inputFile.close(); // zamknięcie pliku

    ui -> horizontalSlider -> setValue(show);
}

void MainWindow::czytajKolorPixela(int x, int y) {
    unsigned char * wsk;
    if (x >= 0 && y >= 0 && x < width && y < height) {
        wsk = img -> scanLine(y);

        blueCZYTAJ = wsk[4 * x];
        greenCZYTAJ = wsk[4 * x + 1];
        redCZYTAJ = wsk[4 * x + 2];
    }
}

void MainWindow::floodFill(int x0, int y0) {
    wspolrzednePunktu punkt;
    punkt.wspX = x0;
    punkt.wspY = y0;
    QStack < wspolrzednePunktu > stos;
    stos.push(punkt);

    while (!stos.isEmpty()) {
        punkt = stos.pop();

        if ((punkt.wspX >= 0) && (punkt.wspY >= 0) && (punkt.wspX < width) && (punkt.wspY < height)) {
            czytajKolorPixela(punkt.wspX, punkt.wspY);
            if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
                drawPixel(punkt.wspX, punkt.wspY, 255, 0, 0);

                punkt.wspX = punkt.wspX + 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX - 1;

                punkt.wspY = punkt.wspY + 1;
                stos.push(punkt);

                punkt.wspY = punkt.wspY - 1;

                punkt.wspX = punkt.wspX - 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX + 1;

                punkt.wspY = punkt.wspY - 1;
                stos.push(punkt);
            }
        }
    }

    update();
}

void MainWindow::floodFill2(int x0, int y0) {
    wspolrzednePunktu punkt;
    punkt.wspX = x0;
    punkt.wspY = y0;
    QStack < wspolrzednePunktu > stos;
    stos.push(punkt);

    while (!stos.isEmpty()) {
        punkt = stos.pop();

        if ((punkt.wspX >= 0) && (punkt.wspY >= 0) && (punkt.wspX < width) && (punkt.wspY < height)) {
            czytajKolorPixela(punkt.wspX, punkt.wspY);
            if (blueCZYTAJ == 0 && greenCZYTAJ == 0 && redCZYTAJ == 255) {
                drawPixel(punkt.wspX, punkt.wspY, 255, 255, 255);

                punkt.wspX = punkt.wspX + 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX - 1;

                punkt.wspY = punkt.wspY + 1;
                stos.push(punkt);

                punkt.wspY = punkt.wspY - 1;

                punkt.wspX = punkt.wspX - 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX + 1;

                punkt.wspY = punkt.wspY - 1;
                stos.push(punkt);
            }
        }
    }

    update();
}

void MainWindow::on_cleanButton_clicked() {
    unsigned char * wsk;

    for (int i = 0; i < height; i++) {
        wsk = img -> scanLine(i);

        for (int j = 0; j < width; j++) {
            wsk[4 * j] = 255;
            wsk[4 * j + 1] = 255;
            wsk[4 * j + 2] = 255;
        }
    }

    for (int i = 0; i < 550; i++) {
        for (int j = 0; j < 750; j++) {
            if (i % 100 == 0) {
                drawPixel(i, j, 0, 0, 0);
                drawPixel(i + 1, j, 0, 0, 0);
                drawPixel(i - 1, j, 0, 0, 0);
            }

            if (j % 100 == 0) {
                drawPixel(i, j, 0, 0, 0);
                drawPixel(i, j - 1, 0, 0, 0);
                drawPixel(i, j + 1, 0, 0, 0);
            }

            if ((i >= 0 && i < 3) || (i > 497 && i <= 500)) {
                drawPixel(i, j, 0, 0, 0);
                drawPixel(i, j - 1, 0, 0, 0);
                drawPixel(i, j + 1, 0, 0, 0);
            }

            if ((j >= 0 && j < 3) || (j > 697 && j <= 700)) {
                drawPixel(i, j, 0, 0, 0);
                drawPixel(i, j - 1, 0, 0, 0);
                drawPixel(i, j + 1, 0, 0, 0);
            }
        }
    }

    update();
}

void MainWindow::on_exitButton_clicked() {
    qApp -> quit();
}

void MainWindow::on_pushButton_clicked() {
    wspolrzednePunktu punkt;
    punkt.wspX = x0;
    punkt.wspY = y0;
    QStack < wspolrzednePunktu > stos;
    stos.push(punkt);

    while (!stos.isEmpty()) {
        punkt = stos.pop();

        if ((punkt.wspX >= 0) && (punkt.wspY >= 0) && (punkt.wspX < width) && (punkt.wspY < height)) {
            czytajKolorPixela(punkt.wspX, punkt.wspY);
            if (blueCZYTAJ == 255 && greenCZYTAJ == 255 && redCZYTAJ == 255) {
                drawPixel(punkt.wspX, punkt.wspY, 255, 0, 0);

                punkt.wspX = punkt.wspX + 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX - 1;

                punkt.wspY = punkt.wspY + 1;
                stos.push(punkt);

                punkt.wspY = punkt.wspY - 1;

                punkt.wspX = punkt.wspX - 1;
                stos.push(punkt);

                punkt.wspX = punkt.wspX + 1;

                punkt.wspY = punkt.wspY - 1;
                stos.push(punkt);
            }
        }
    }

    update();
}
