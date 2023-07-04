/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QFrame *frame;
    QGroupBox *groupBox;
    QPushButton *cleanButton;
    QPushButton *exitButton;
    QPlainTextEdit *plainTextEdit;
    QSlider *horizontalSlider;
    QPushButton *pushButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(928, 778);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        frame = new QFrame(centralwidget);
        frame->setObjectName("frame");
        frame->setGeometry(QRect(20, 20, 500, 700));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName("groupBox");
        groupBox->setGeometry(QRect(570, 430, 321, 141));
        QFont font;
        font.setPointSize(18);
        groupBox->setFont(font);
        groupBox->setStyleSheet(QString::fromUtf8(""));
        cleanButton = new QPushButton(groupBox);
        cleanButton->setObjectName("cleanButton");
        cleanButton->setGeometry(QRect(30, 60, 111, 51));
        QFont font1;
        font1.setPointSize(18);
        font1.setBold(true);
        cleanButton->setFont(font1);
        exitButton = new QPushButton(groupBox);
        exitButton->setObjectName("exitButton");
        exitButton->setGeometry(QRect(170, 60, 111, 51));
        exitButton->setFont(font1);
        plainTextEdit = new QPlainTextEdit(centralwidget);
        plainTextEdit->setObjectName("plainTextEdit");
        plainTextEdit->setGeometry(QRect(550, 20, 361, 371));
        QFont font2;
        font2.setPointSize(12);
        font2.setBold(true);
        plainTextEdit->setFont(font2);
        horizontalSlider = new QSlider(centralwidget);
        horizontalSlider->setObjectName("horizontalSlider");
        horizontalSlider->setGeometry(QRect(560, 199, 331, 121));
        horizontalSlider->setMaximum(9);
        horizontalSlider->setOrientation(Qt::Horizontal);
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(560, 225, 341, 151));
        pushButton->setStyleSheet(QString::fromUtf8("\n"
"    background-color: white;\n"
"    border: 0px;"));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 928, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "PGK", nullptr));
        groupBox->setTitle(QCoreApplication::translate("MainWindow", "Sterowanie", nullptr));
        cleanButton->setText(QCoreApplication::translate("MainWindow", "Start", nullptr));
        exitButton->setText(QCoreApplication::translate("MainWindow", "Wyj\305\233cie", nullptr));
        plainTextEdit->setPlainText(QCoreApplication::translate("MainWindow", "START - rozpocz\304\231cie programu\n"
"LMB/LPM - zamalowanie na czerwono\n"
"RMB/PPM - zamalowanie na bia\305\202o\n"
"WYJ\305\232CIE - zako\305\204czenie dzia\305\202ania programu\n"
"\n"
"           \n"
"                   przewidywana cyfra:\n"
" 0      1      2      3      4      5      6      7      8      9\n"
"", nullptr));
        pushButton->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
