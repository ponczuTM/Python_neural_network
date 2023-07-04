#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QImage>
#include <QPainter>
#include <QMouseEvent>
#include <QStack>
#include <QDebug>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_exitButton_clicked();
    void on_cleanButton_clicked();
    void paintEvent(QPaintEvent*);
    void mousePressEvent(QMouseEvent *event);

    void on_pushButton_clicked();

    void on_horizontalSlider_valueChanged(int value);

    //void on_testowy_clicked();

private:
    Ui::MainWindow *ui;

    QImage *img;

    int width, height;

    int startX, startY;
    double x0,y0,x1,y1;
    unsigned char redCZYTAJ; unsigned char greenCZYTAJ; unsigned char blueCZYTAJ;

    int funkcja=123;
    void clean();
    void wpisz();
    void drawPixel(int x, int y, unsigned char red = 255, unsigned char green = 255, unsigned char blue = 255);
    void rysuj8punktow(int x, int y);
    void rysujOkrag(double x0, double y0, double x1, double y1);
    void rysuj_odcinek(double p,double m, double o, double e);
    void floodFill(int x0,int y0);
    void floodFill2(int x0,int y0);
    void czytajKolorPixela(int x, int y);
    struct wspolrzednePunktu{
        int wspX;
        int wspY;
    };


};
#endif // MAINWINDOW_H
