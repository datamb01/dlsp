# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyse_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_analyse_gui(object):
    def setupUi(self, analyse_gui):
        if not analyse_gui.objectName():
            analyse_gui.setObjectName(u"analyse_gui")
        analyse_gui.resize(1146, 820)
        analyse_gui.setCursor(QCursor(Qt.ArrowCursor))
        analyse_gui.setMouseTracking(False)
        analyse_gui.setAutoFillBackground(False)
        analyse_gui.setStyleSheet(u"background-color: rgb(95, 179, 179);")
        self.actionQuit = QAction(analyse_gui)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionKunden_verwalten = QAction(analyse_gui)
        self.actionKunden_verwalten.setObjectName(u"actionKunden_verwalten")
        self.actionAuftragnehmer_verwalten = QAction(analyse_gui)
        self.actionAuftragnehmer_verwalten.setObjectName(u"actionAuftragnehmer_verwalten")
        self.centralwidget = QWidget(analyse_gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(95, 179, 179);")
        self.lbl_modulname = QLabel(self.centralwidget)
        self.lbl_modulname.setObjectName(u"lbl_modulname")
        self.lbl_modulname.setGeometry(QRect(10, 0, 1071, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_modulname.setFont(font)
        self.lbl_modulname.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.lbl_modulname.setAlignment(Qt.AlignCenter)
        self.lbl_namen_gruppe = QLabel(self.centralwidget)
        self.lbl_namen_gruppe.setObjectName(u"lbl_namen_gruppe")
        self.lbl_namen_gruppe.setGeometry(QRect(30, 820, 361, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.lbl_namen_gruppe.setFont(font1)
        self.lbl_namen_gruppe.setAlignment(Qt.AlignCenter)
        self.lbl_projekttitel = QLabel(self.centralwidget)
        self.lbl_projekttitel.setObjectName(u"lbl_projekttitel")
        self.lbl_projekttitel.setGeometry(QRect(10, 30, 1071, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_projekttitel.setFont(font2)
        self.lbl_projekttitel.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.lbl_projekttitel.setAlignment(Qt.AlignCenter)
        self.lbl_logo = QLabel(self.centralwidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(1100, 650, 41, 131))
        self.lbl_logo.setPixmap(QPixmap(u"Bilder/FH-Logo.PNG"))
        self.lbl_names = QLabel(self.centralwidget)
        self.lbl_names.setObjectName(u"lbl_names")
        self.lbl_names.setGeometry(QRect(740, 780, 401, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.lbl_names.setFont(font3)
        self.lbl_names.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.lbl_names.setFrameShape(QFrame.Box)
        self.lbl_names.setFrameShadow(QFrame.Raised)
        self.lbl_names.setAlignment(Qt.AlignCenter)
        self.Prozessschritte = QFrame(self.centralwidget)
        self.Prozessschritte.setObjectName(u"Prozessschritte")
        self.Prozessschritte.setGeometry(QRect(10, 110, 861, 151))
        self.Prozessschritte.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.Prozessschritte.setFrameShape(QFrame.Box)
        self.Prozessschritte.setFrameShadow(QFrame.Raised)
        self.programmschritte_2 = QVBoxLayout(self.Prozessschritte)
        self.programmschritte_2.setObjectName(u"programmschritte_2")
        self.programmschritte_2.setContentsMargins(9, -1, -1, -1)
        self.prozessschritte = QFrame(self.Prozessschritte)
        self.prozessschritte.setObjectName(u"prozessschritte")
        self.prozessschritte.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.prozessschritte.setFrameShape(QFrame.NoFrame)
        self.prozessschritte.setLineWidth(2)
        self.schritte = QHBoxLayout(self.prozessschritte)
        self.schritte.setObjectName(u"schritte")
        self.schritte.setContentsMargins(9, -1, -1, -1)
        self.daten_sammeln = QFrame(self.prozessschritte)
        self.daten_sammeln.setObjectName(u"daten_sammeln")
        self.daten_sammeln.setMaximumSize(QSize(120, 16777215))
        self.daten_sammeln.setFrameShape(QFrame.NoFrame)
        self.datensammlung = QVBoxLayout(self.daten_sammeln)
        self.datensammlung.setObjectName(u"datensammlung")
        self.datensammlung.setContentsMargins(9, -1, -1, -1)
        self.lbl_bild_datensammlung = QLabel(self.daten_sammeln)
        self.lbl_bild_datensammlung.setObjectName(u"lbl_bild_datensammlung")
        self.lbl_bild_datensammlung.setPixmap(QPixmap(u"Bilder/Datensammlung.PNG"))
        self.lbl_bild_datensammlung.setScaledContents(True)

        self.datensammlung.addWidget(self.lbl_bild_datensammlung)

        self.lbl_prozess1 = QLabel(self.daten_sammeln)
        self.lbl_prozess1.setObjectName(u"lbl_prozess1")
        self.lbl_prozess1.setMinimumSize(QSize(0, 40))
        self.lbl_prozess1.setMaximumSize(QSize(110, 40))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.lbl_prozess1.setFont(font4)
        self.lbl_prozess1.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_prozess1.setFrameShape(QFrame.NoFrame)
        self.lbl_prozess1.setFrameShadow(QFrame.Plain)

        self.datensammlung.addWidget(self.lbl_prozess1)


        self.schritte.addWidget(self.daten_sammeln)

        self.arrow1 = QFrame(self.prozessschritte)
        self.arrow1.setObjectName(u"arrow1")
        self.verticalLayout_4 = QVBoxLayout(self.arrow1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_bild_arrow1 = QLabel(self.arrow1)
        self.lbl_bild_arrow1.setObjectName(u"lbl_bild_arrow1")
        self.lbl_bild_arrow1.setPixmap(QPixmap(u"Bilder/pfeil.PNG"))

        self.verticalLayout_4.addWidget(self.lbl_bild_arrow1)


        self.schritte.addWidget(self.arrow1)

        self.senden_gateway = QFrame(self.prozessschritte)
        self.senden_gateway.setObjectName(u"senden_gateway")
        self.gateway = QVBoxLayout(self.senden_gateway)
        self.gateway.setObjectName(u"gateway")
        self.lbl_bild_gateway = QLabel(self.senden_gateway)
        self.lbl_bild_gateway.setObjectName(u"lbl_bild_gateway")
        self.lbl_bild_gateway.setPixmap(QPixmap(u"Bilder/Gateway2.PNG"))
        self.lbl_bild_gateway.setScaledContents(True)

        self.gateway.addWidget(self.lbl_bild_gateway)

        self.lbl_prozess2 = QLabel(self.senden_gateway)
        self.lbl_prozess2.setObjectName(u"lbl_prozess2")
        self.lbl_prozess2.setMinimumSize(QSize(0, 40))
        self.lbl_prozess2.setMaximumSize(QSize(100, 40))
        self.lbl_prozess2.setFont(font4)
        self.lbl_prozess2.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_prozess2.setFrameShape(QFrame.NoFrame)
        self.lbl_prozess2.setFrameShadow(QFrame.Plain)
        self.lbl_prozess2.setAlignment(Qt.AlignCenter)

        self.gateway.addWidget(self.lbl_prozess2)


        self.schritte.addWidget(self.senden_gateway)

        self.arrow2 = QFrame(self.prozessschritte)
        self.arrow2.setObjectName(u"arrow2")
        self.verticalLayout_6 = QVBoxLayout(self.arrow2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_bild_arrow2 = QLabel(self.arrow2)
        self.lbl_bild_arrow2.setObjectName(u"lbl_bild_arrow2")
        self.lbl_bild_arrow2.setPixmap(QPixmap(u"Bilder/pfeil.PNG"))

        self.verticalLayout_6.addWidget(self.lbl_bild_arrow2)


        self.schritte.addWidget(self.arrow2)

        self.mongo_db = QFrame(self.prozessschritte)
        self.mongo_db.setObjectName(u"mongo_db")
        self.cloud = QVBoxLayout(self.mongo_db)
        self.cloud.setObjectName(u"cloud")
        self.lbl_bild_mongodb = QLabel(self.mongo_db)
        self.lbl_bild_mongodb.setObjectName(u"lbl_bild_mongodb")
        self.lbl_bild_mongodb.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.lbl_bild_mongodb.setPixmap(QPixmap(u"Bilder/MongoDB.PNG"))
        self.lbl_bild_mongodb.setScaledContents(True)

        self.cloud.addWidget(self.lbl_bild_mongodb)

        self.lbl_prozess3 = QLabel(self.mongo_db)
        self.lbl_prozess3.setObjectName(u"lbl_prozess3")
        self.lbl_prozess3.setMinimumSize(QSize(0, 40))
        self.lbl_prozess3.setMaximumSize(QSize(120, 40))
        self.lbl_prozess3.setFont(font4)
        self.lbl_prozess3.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_prozess3.setFrameShape(QFrame.NoFrame)
        self.lbl_prozess3.setFrameShadow(QFrame.Plain)
        self.lbl_prozess3.setAlignment(Qt.AlignCenter)

        self.cloud.addWidget(self.lbl_prozess3)


        self.schritte.addWidget(self.mongo_db)

        self.arrow_3 = QFrame(self.prozessschritte)
        self.arrow_3.setObjectName(u"arrow_3")
        self.verticalLayout_8 = QVBoxLayout(self.arrow_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_bild_arrow3 = QLabel(self.arrow_3)
        self.lbl_bild_arrow3.setObjectName(u"lbl_bild_arrow3")
        self.lbl_bild_arrow3.setPixmap(QPixmap(u"Bilder/pfeil.PNG"))

        self.verticalLayout_8.addWidget(self.lbl_bild_arrow3)


        self.schritte.addWidget(self.arrow_3)

        self.maschinelles_lernen = QFrame(self.prozessschritte)
        self.maschinelles_lernen.setObjectName(u"maschinelles_lernen")
        self.machine_learning = QVBoxLayout(self.maschinelles_lernen)
        self.machine_learning.setObjectName(u"machine_learning")
        self.lbl_bild_ml = QLabel(self.maschinelles_lernen)
        self.lbl_bild_ml.setObjectName(u"lbl_bild_ml")
        self.lbl_bild_ml.setPixmap(QPixmap(u"Bilder/ML.PNG"))
        self.lbl_bild_ml.setScaledContents(True)

        self.machine_learning.addWidget(self.lbl_bild_ml)

        self.lbl_prozess4 = QLabel(self.maschinelles_lernen)
        self.lbl_prozess4.setObjectName(u"lbl_prozess4")
        self.lbl_prozess4.setMinimumSize(QSize(80, 40))
        self.lbl_prozess4.setMaximumSize(QSize(80, 40))
        self.lbl_prozess4.setFont(font4)
        self.lbl_prozess4.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_prozess4.setFrameShape(QFrame.NoFrame)
        self.lbl_prozess4.setFrameShadow(QFrame.Plain)
        self.lbl_prozess4.setAlignment(Qt.AlignCenter)

        self.machine_learning.addWidget(self.lbl_prozess4)


        self.schritte.addWidget(self.maschinelles_lernen)

        self.arow4 = QFrame(self.prozessschritte)
        self.arow4.setObjectName(u"arow4")
        self.verticalLayout_9 = QVBoxLayout(self.arow4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_bild_arrow4 = QLabel(self.arow4)
        self.lbl_bild_arrow4.setObjectName(u"lbl_bild_arrow4")
        self.lbl_bild_arrow4.setPixmap(QPixmap(u"Bilder/pfeil.PNG"))

        self.verticalLayout_9.addWidget(self.lbl_bild_arrow4)


        self.schritte.addWidget(self.arow4)

        self.qt_gui = QFrame(self.prozessschritte)
        self.qt_gui.setObjectName(u"qt_gui")
        self.gui = QVBoxLayout(self.qt_gui)
        self.gui.setObjectName(u"gui")
        self.lbl_bild_qt = QLabel(self.qt_gui)
        self.lbl_bild_qt.setObjectName(u"lbl_bild_qt")
        self.lbl_bild_qt.setMinimumSize(QSize(0, 50))
        self.lbl_bild_qt.setMaximumSize(QSize(110, 50))
        self.lbl_bild_qt.setPixmap(QPixmap(u"Bilder/Qt2.PNG"))
        self.lbl_bild_qt.setScaledContents(False)

        self.gui.addWidget(self.lbl_bild_qt)

        self.lbl_prozess5 = QLabel(self.qt_gui)
        self.lbl_prozess5.setObjectName(u"lbl_prozess5")
        self.lbl_prozess5.setMinimumSize(QSize(0, 40))
        self.lbl_prozess5.setMaximumSize(QSize(110, 40))
        self.lbl_prozess5.setFont(font4)
        self.lbl_prozess5.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_prozess5.setFrameShape(QFrame.NoFrame)
        self.lbl_prozess5.setFrameShadow(QFrame.Plain)
        self.lbl_prozess5.setAlignment(Qt.AlignCenter)

        self.gui.addWidget(self.lbl_prozess5)


        self.schritte.addWidget(self.qt_gui)


        self.programmschritte_2.addWidget(self.prozessschritte)

        self.lbl_ablaufschritte = QLabel(self.centralwidget)
        self.lbl_ablaufschritte.setObjectName(u"lbl_ablaufschritte")
        self.lbl_ablaufschritte.setGeometry(QRect(10, 70, 861, 41))
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.lbl_ablaufschritte.setFont(font5)
        self.lbl_ablaufschritte.setStyleSheet(u"background-color: rgb(214, 111, 177);\n"
"border: 1px solid black")
        self.lbl_ablaufschritte.setFrameShape(QFrame.NoFrame)
        self.lbl_ablaufschritte.setFrameShadow(QFrame.Plain)
        self.lbl_ablaufschritte.setAlignment(Qt.AlignCenter)
        self.lbl_betriebszustand = QLabel(self.centralwidget)
        self.lbl_betriebszustand.setObjectName(u"lbl_betriebszustand")
        self.lbl_betriebszustand.setGeometry(QRect(10, 270, 861, 41))
        self.lbl_betriebszustand.setFont(font5)
        self.lbl_betriebszustand.setStyleSheet(u"background-color: rgb(214, 111, 177);\n"
"border: 1px solid black")
        self.lbl_betriebszustand.setFrameShape(QFrame.NoFrame)
        self.lbl_betriebszustand.setFrameShadow(QFrame.Plain)
        self.lbl_betriebszustand.setAlignment(Qt.AlignCenter)
        self.maschinenzustaende = QFrame(self.centralwidget)
        self.maschinenzustaende.setObjectName(u"maschinenzustaende")
        self.maschinenzustaende.setGeometry(QRect(10, 310, 861, 91))
        self.maschinenzustaende.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.maschinenzustaende.setFrameShape(QFrame.Box)
        self.maschinenzustaende.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.maschinenzustaende)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.vorwaesche = QFrame(self.maschinenzustaende)
        self.vorwaesche.setObjectName(u"vorwaesche")
        self.vorwaesche.setMinimumSize(QSize(0, 0))
        self.vorwaesche.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_13 = QVBoxLayout(self.vorwaesche)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.lbl_zustand1 = QLabel(self.vorwaesche)
        self.lbl_zustand1.setObjectName(u"lbl_zustand1")
        self.lbl_zustand1.setMinimumSize(QSize(140, 30))
        self.lbl_zustand1.setMaximumSize(QSize(160, 30))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.lbl_zustand1.setFont(font6)
        self.lbl_zustand1.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_zustand1.setFrameShape(QFrame.NoFrame)
        self.lbl_zustand1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.lbl_zustand1, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.lbl_bild_zustand1 = QLabel(self.vorwaesche)
        self.lbl_bild_zustand1.setObjectName(u"lbl_bild_zustand1")
        self.lbl_bild_zustand1.setMinimumSize(QSize(25, 25))
        self.lbl_bild_zustand1.setMaximumSize(QSize(25, 25))
        self.lbl_bild_zustand1.setStyleSheet(u"")
        self.lbl_bild_zustand1.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_13.addWidget(self.lbl_bild_zustand1, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.vorwaesche)

        self.abpumpen = QFrame(self.maschinenzustaende)
        self.abpumpen.setObjectName(u"abpumpen")
        self.abpumpen.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_15 = QVBoxLayout(self.abpumpen)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(16, -1, -1, -1)
        self.lbl_zustand2 = QLabel(self.abpumpen)
        self.lbl_zustand2.setObjectName(u"lbl_zustand2")
        self.lbl_zustand2.setMinimumSize(QSize(140, 30))
        self.lbl_zustand2.setMaximumSize(QSize(140, 30))
        self.lbl_zustand2.setFont(font6)
        self.lbl_zustand2.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_zustand2.setFrameShape(QFrame.NoFrame)
        self.lbl_zustand2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lbl_zustand2)

        self.lbl_bild_zustand2 = QLabel(self.abpumpen)
        self.lbl_bild_zustand2.setObjectName(u"lbl_bild_zustand2")
        self.lbl_bild_zustand2.setMinimumSize(QSize(25, 25))
        self.lbl_bild_zustand2.setMaximumSize(QSize(25, 25))
        self.lbl_bild_zustand2.setStyleSheet(u"")
        self.lbl_bild_zustand2.setScaledContents(False)

        self.verticalLayout_15.addWidget(self.lbl_bild_zustand2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.abpumpen)

        self.hauptwaesche = QFrame(self.maschinenzustaende)
        self.hauptwaesche.setObjectName(u"hauptwaesche")
        self.hauptwaesche.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_16 = QVBoxLayout(self.hauptwaesche)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(16, 10, -1, -1)
        self.lbl_zustand3 = QLabel(self.hauptwaesche)
        self.lbl_zustand3.setObjectName(u"lbl_zustand3")
        self.lbl_zustand3.setMinimumSize(QSize(150, 30))
        self.lbl_zustand3.setMaximumSize(QSize(140, 30))
        self.lbl_zustand3.setFont(font6)
        self.lbl_zustand3.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_zustand3.setFrameShape(QFrame.NoFrame)
        self.lbl_zustand3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.lbl_zustand3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.lbl_bild_zustand3 = QLabel(self.hauptwaesche)
        self.lbl_bild_zustand3.setObjectName(u"lbl_bild_zustand3")
        self.lbl_bild_zustand3.setMinimumSize(QSize(25, 25))
        self.lbl_bild_zustand3.setMaximumSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.lbl_bild_zustand3, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.hauptwaesche)

        self.spuelen = QFrame(self.maschinenzustaende)
        self.spuelen.setObjectName(u"spuelen")
        self.spuelen.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_17 = QVBoxLayout(self.spuelen)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(9, -1, -1, -1)
        self.lbl_zustand4 = QLabel(self.spuelen)
        self.lbl_zustand4.setObjectName(u"lbl_zustand4")
        self.lbl_zustand4.setMinimumSize(QSize(140, 0))
        self.lbl_zustand4.setMaximumSize(QSize(140, 30))
        self.lbl_zustand4.setFont(font6)
        self.lbl_zustand4.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_zustand4.setFrameShape(QFrame.NoFrame)
        self.lbl_zustand4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.lbl_zustand4)

        self.lbl_bild_zustand4 = QLabel(self.spuelen)
        self.lbl_bild_zustand4.setObjectName(u"lbl_bild_zustand4")
        self.lbl_bild_zustand4.setMinimumSize(QSize(25, 25))
        self.lbl_bild_zustand4.setMaximumSize(QSize(25, 25))

        self.verticalLayout_17.addWidget(self.lbl_bild_zustand4, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.spuelen)

        self.schleudern = QFrame(self.maschinenzustaende)
        self.schleudern.setObjectName(u"schleudern")
        self.schleudern.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_14 = QVBoxLayout(self.schleudern)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_14.setContentsMargins(12, -1, -1, -1)
        self.lbl_zustand5 = QLabel(self.schleudern)
        self.lbl_zustand5.setObjectName(u"lbl_zustand5")
        self.lbl_zustand5.setMinimumSize(QSize(140, 0))
        self.lbl_zustand5.setMaximumSize(QSize(140, 30))
        self.lbl_zustand5.setFont(font6)
        self.lbl_zustand5.setStyleSheet(u"background-color: rgb(227, 198, 129);\n"
"border: 1px solid black")
        self.lbl_zustand5.setFrameShape(QFrame.NoFrame)
        self.lbl_zustand5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.lbl_zustand5)

        self.lbl_bild_zustand5 = QLabel(self.schleudern)
        self.lbl_bild_zustand5.setObjectName(u"lbl_bild_zustand5")
        self.lbl_bild_zustand5.setMinimumSize(QSize(25, 25))
        self.lbl_bild_zustand5.setMaximumSize(QSize(25, 25))
        self.lbl_bild_zustand5.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.verticalLayout_14.addWidget(self.lbl_bild_zustand5, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.schleudern)

        self.verbindung = QFrame(self.centralwidget)
        self.verbindung.setObjectName(u"verbindung")
        self.verbindung.setGeometry(QRect(899, 70, 181, 191))
        self.verbindung.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.verticalLayout_7 = QVBoxLayout(self.verbindung)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 2, 4, 2)
        self.lbl_verbindung = QLabel(self.verbindung)
        self.lbl_verbindung.setObjectName(u"lbl_verbindung")
        self.lbl_verbindung.setMinimumSize(QSize(175, 40))
        self.lbl_verbindung.setMaximumSize(QSize(175, 60))
        font7 = QFont()
        font7.setFamilies([u"Arial Black"])
        font7.setPointSize(13)
        font7.setBold(True)
        self.lbl_verbindung.setFont(font7)
        self.lbl_verbindung.setStyleSheet(u"background-color: rgb(214, 111, 177);\n"
"border: 1px solid black")
        self.lbl_verbindung.setFrameShape(QFrame.NoFrame)
        self.lbl_verbindung.setFrameShadow(QFrame.Plain)
        self.lbl_verbindung.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_verbindung)

        self.verbinden_microcontroller = QPushButton(self.verbindung)
        self.verbinden_microcontroller.setObjectName(u"verbinden_microcontroller")
        self.verbinden_microcontroller.setMinimumSize(QSize(175, 40))
        self.verbinden_microcontroller.setMaximumSize(QSize(175, 120))
        self.verbinden_microcontroller.setFont(font2)
        self.verbinden_microcontroller.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        icon = QIcon()
        icon.addFile(u"GUI_Qt/Bilder/ESP.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.verbinden_microcontroller.setIcon(icon)
        self.verbinden_microcontroller.setIconSize(QSize(45, 45))

        self.verticalLayout_7.addWidget(self.verbinden_microcontroller)

        self.diagramm = QFrame(self.centralwidget)
        self.diagramm.setObjectName(u"diagramm")
        self.diagramm.setGeometry(QRect(10, 410, 1068, 361))
        self.diagramm.setStyleSheet(u"background-color: rgb(217, 217, 217)")
        self.verticalLayout_10 = QVBoxLayout(self.diagramm)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.lbl_diagramm_titel = QLabel(self.diagramm)
        self.lbl_diagramm_titel.setObjectName(u"lbl_diagramm_titel")
        self.lbl_diagramm_titel.setMinimumSize(QSize(1060, 30))
        self.lbl_diagramm_titel.setMaximumSize(QSize(1060, 30))
        self.lbl_diagramm_titel.setFont(font7)
        self.lbl_diagramm_titel.setFocusPolicy(Qt.TabFocus)
        self.lbl_diagramm_titel.setStyleSheet(u"background-color: rgb(214, 111, 177);\n"
"border: 1px solid black")
        self.lbl_diagramm_titel.setFrameShape(QFrame.NoFrame)
        self.lbl_diagramm_titel.setFrameShadow(QFrame.Plain)
        self.lbl_diagramm_titel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lbl_diagramm_titel)

        self.diagramm_darstellungView = QChartView(self.diagramm)
        self.diagramm_darstellungView.setObjectName(u"diagramm_darstellungView")
        self.diagramm_darstellungView.setMinimumSize(QSize(1060, 320))
        self.diagramm_darstellungView.setMaximumSize(QSize(1060, 320))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        self.diagramm_darstellungView.setFont(font8)
        self.diagramm_darstellungView.setLayoutDirection(Qt.LeftToRight)
        self.diagramm_darstellungView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.diagramm_darstellungView.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_10.addWidget(self.diagramm_darstellungView)

        analyse_gui.setCentralWidget(self.centralwidget)
        self.lbl_modulname.raise_()
        self.lbl_namen_gruppe.raise_()
        self.lbl_projekttitel.raise_()
        self.lbl_logo.raise_()
        self.lbl_names.raise_()
        self.Prozessschritte.raise_()
        self.maschinenzustaende.raise_()
        self.lbl_betriebszustand.raise_()
        self.lbl_ablaufschritte.raise_()
        self.verbindung.raise_()
        self.diagramm.raise_()
        self.statusbar = QStatusBar(analyse_gui)
        self.statusbar.setObjectName(u"statusbar")
        analyse_gui.setStatusBar(self.statusbar)

        self.retranslateUi(analyse_gui)

        QMetaObject.connectSlotsByName(analyse_gui)
    # setupUi

    def retranslateUi(self, analyse_gui):
        analyse_gui.setWindowTitle(QCoreApplication.translate("analyse_gui", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("analyse_gui", u"Quit", None))
        self.actionKunden_verwalten.setText(QCoreApplication.translate("analyse_gui", u"Kunden verwalten", None))
        self.actionAuftragnehmer_verwalten.setText(QCoreApplication.translate("analyse_gui", u"Auftragnehmer verwalten", None))
        self.lbl_modulname.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Erfassung von Beschleunigungsdaten einer Waschmaschine und Klassifizierung der Betriebszust\u00e4nde</span></p></body></html>", None))
        #self.lbl_namen_gruppe.setText(QCoreApplication.translate("analyse_gui", u"Erstellt von Davin Tandrayuana(3551264)", None))
        #self.lbl_projekttitel.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p><span style=\" color:#000000;\">Erfassung von Beschleunigungsdaten einer Waschmaschine und Klassifizierung der Betriebszust\u00e4nde</span></p></body></html>", None))
        self.lbl_logo.setText("")
        self.lbl_names.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p><span style=\" color:#000000;\">Vorleget von Davin Tandrayuana(3551264)</span></p></body></html>", None))
        self.lbl_bild_datensammlung.setText("")
        self.lbl_prozess1.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p align=\"center\">Daten<br/>sammlung</p></body></html>", None))
        self.lbl_bild_arrow1.setText("")
        self.lbl_bild_gateway.setText("")
        self.lbl_prozess2.setText(QCoreApplication.translate("analyse_gui", u"Gateway", None))
        self.lbl_bild_arrow2.setText("")
        self.lbl_bild_mongodb.setText("")
        self.lbl_prozess3.setText(QCoreApplication.translate("analyse_gui", u"Mongo DB", None))
        self.lbl_bild_arrow3.setText("")
        self.lbl_bild_ml.setText("")
        self.lbl_prozess4.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p>Machine<br/>Learning</p></body></html>", None))
        self.lbl_bild_arrow4.setText("")
        self.lbl_bild_qt.setText("")
        self.lbl_prozess5.setText(QCoreApplication.translate("analyse_gui", u"GUI", None))
        self.lbl_ablaufschritte.setText(QCoreApplication.translate("analyse_gui", u"Ablaufschritte:", None))
        self.lbl_betriebszustand.setText(QCoreApplication.translate("analyse_gui", u"Derzeitiger Betriebszustand:", None))
        self.lbl_zustand1.setText(QCoreApplication.translate("analyse_gui", u"Vorw\u00e4sche", None))
        self.lbl_zustand2.setText(QCoreApplication.translate("analyse_gui", u"Abpumpen", None))
        self.lbl_bild_zustand2.setText("")
        self.lbl_zustand3.setText(QCoreApplication.translate("analyse_gui", u"Hauptw\u00e4sche", None))
        self.lbl_bild_zustand3.setText("")
        self.lbl_zustand4.setText(QCoreApplication.translate("analyse_gui", u"Sp\u00fclen", None))
        self.lbl_bild_zustand4.setText("")
        self.lbl_zustand5.setText(QCoreApplication.translate("analyse_gui", u"Schleudern", None))
        self.lbl_bild_zustand5.setText("")
        self.lbl_verbindung.setText(QCoreApplication.translate("analyse_gui", u"<html><head/><body><p>Verbinden mit<br/>Microcontroller:</p></body></html>", None))
        self.verbinden_microcontroller.setText(QCoreApplication.translate("analyse_gui", u"Hier klicken!", None))
        self.lbl_diagramm_titel.setText(QCoreApplication.translate("analyse_gui", u"Visualisierung der Werte:", None))
    # retranslateUi

