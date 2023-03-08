# Importieren von notwendigen Bibliotheken

import datetime
import time

import usocket as socket

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads

import PySide6
import sys
from analyse_gui import *

from PySide6.QtGui import Qt
from PySide6 import QtCharts

from PySide6.QtWidgets import (QApplication, QMainWindow,)

from analyse_gui import Ui_analyse_gui

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier



class analysis_washing(QMainWindow, Ui_analyse_gui):
    def __init__(self):
        # Initialisierung der Klasse für die GUI-Oberfläche
        super().__init__()
        self.setupUi(self)
        # Einstellungen der Größe und Bezeichung des Fensters
        self.setGeometry(0, 0, 1150, 800)
        self.setWindowTitle("Analyse der Waschmaschinenzustände")

        # Initiialisierung des Liniendiagramms
        self.create_line_chart()

        # Einstellung des Push-Buttons
        self.verbinden_microcontroller.clicked.connect(self.start_process)

    def create_line_chart(self): # Erstellung des Liniendiagramms
        self.axSeries = QtCharts.QLineSeries()
        self.aySeries = QtCharts.QLineSeries()
        self.azSeries = QtCharts.QLineSeries()

        self.axSeries.setName("Ax")
        self.aySeries.setName("Ay")
        self.azSeries.setName("Az")

        self.diagramm_darstellung = QtCharts.QChart()
        self.diagramm_darstellung.legend().setVisible(True)
        self.diagramm_darstellung.legend().setAlignment(Qt.AlignBottom)
        self.diagramm_darstellung.addSeries(self.axSeries)
        self.diagramm_darstellung.addSeries(self.aySeries)
        self.diagramm_darstellung.addSeries(self.azSeries)
        self.diagramm_darstellung.createDefaultAxes()
        self.diagramm_darstellung.setTitle("Beschleunigungsdaten")
        self.diagramm_darstellung.axisX().setTitleText("Zeit in Sekunden")
        self.diagramm_darstellung.axisX().setTitleFont("Arial")
        self.diagramm_darstellung.axisY().setTitleText("Beschleunigungen")
        self.diagramm_darstellung.axisY().setTitleFont("Arial")

        self.diagramm_darstellungView.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        self.diagramm_darstellungView.setChart(self.diagramm_darstellung)

    def remove_content(self): # Bereinigung des Liniendiagramms
        self.axSeries.clear()
        self.aySeries.clear()
        self.azSeries.clear()

        self.diagramm_darstellung.addSeries(self.axSeries)
        self.diagramm_darstellung.addSeries(self.aySeries)
        self.diagramm_darstellung.addSeries(self.azSeries)

        self.diagramm_darstellung.createDefaultAxes()

        self.diagramm_darstellungView.repaint()

    def plot_chart(self, a_x, a_y, a_z, x_time): # Darstellung der gesammelten Beschleunigungsdaten auf dem erstellten Liniendiagramm
        self.axSeries.clear()
        self.aySeries.clear()
        self.azSeries.clear()

        time.sleep(0.003)

        for i in range(0, len(a_x)):
            self.axSeries.append(x_time[i], a_x[i])
        for i in range(0, len(a_y)):
            self.aySeries.append(x_time[i], a_y[i])
        for i in range(0, len(a_z)):
            self.azSeries.append(x_time[i], a_z[i])

        self.diagramm_darstellung.addSeries(self.axSeries)
        self.diagramm_darstellung.addSeries(self.aySeries)
        self.diagramm_darstellung.addSeries(self.azSeries)

        self.diagramm_darstellung.axisX().setRange(0, 7)
        self.diagramm_darstellung.axisY().setRange(-1, 1)

        self.diagramm_darstellungView.repaint()

    def calcFFT(self, accel, nrsamples): # Fast Fourier Transformation der erfassten Beschleunigungsdaten
        accel_without_mean = accel - np.mean(accel)
        freq = np.fft.rfft(accel_without_mean, nrsamples, norm='ortho')
        freq = np.abs(freq)
        freq = freq / nrsamples
        return freq

    def classification(self, df): # Trainieren eines Modells zur Klassifizierung der gesammelten Daten
        self.ml_classifier = MLPClassifier(alpha=0.0001, max_iter=800, verbose=False, early_stopping=False)
        self.sc = StandardScaler()
        df = pd.read_csv(
            r'C:\Users\dav11\OneDrive - Fachhochschule Aachen\Dokumente\01_For_University\02_FH_Aachen\DLsP\Davin_Projekt\Machine Learning/Maschine_learning_training_data.csv')
        X = df.iloc[:, 1:].values
        y = df.iloc[:, 0].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
        self.sc.fit(X_train)

        X_train_std = self.sc.transform(X_train)
        self.ml_classifier.fit(X_train_std, y_train)

        time.sleep(0.003)

        # Klassifizierung der erfassten in MongoDB gespeicherten Daten

        StartSample = 0
        LengthSample = 200
        EndSample = StartSample + LengthSample

        a_x = df.iloc[StartSample:EndSample, 0].values
        a_y = df.iloc[StartSample:EndSample, 1].values
        a_z = df.iloc[StartSample:EndSample, 2].values

        a_abs = np.sqrt(a_x * a_x + a_y * a_y + a_z * a_z)
        aabs_freq = self.calcFFT(a_abs, LengthSample)

        aabs_freq = np.delete(aabs_freq, 0)
        aabs_freq = aabs_freq.reshape(1, -1)

        aabs_freq_std = self.sc.transform(aabs_freq)

        predicted = self.ml_classifier.predict(aabs_freq_std)
        probabilities = self.ml_classifier.predict_proba(aabs_freq_std)

        prediction = predicted[0]
        max_probability=max(probabilities[0])

        # Indikation des identifizierten Zustands in dem GUI

        if prediction==0 and max_probability==probabilities[0][0]:
            self.lbl_zustand1.setEnabled(True)
            self.lbl_bild_zustand1.setStyleSheet(u"background-color: rgb(0, 128, 0);\n""border-radius: 10px;")
        elif prediction==1 and max_probability==probabilities[0][1]:
            self.lbl_zustand2.setEnabled(True)
            self.lbl_bild_zustand2.setStyleSheet(u"background-color: rgb(0, 128, 0);\n""border-radius: 10px;")
        elif prediction==2 and max_probability==probabilities[0][2]:
            self.lbl_zustand3.setEnabled(True)
            self.lbl_bild_zustand3.setStyleSheet(u"background-color: rgb(0, 128, 0);\n""border-radius: 10px;")
        elif prediction==3 and max_probability==probabilities[0][3]:
            self.lbl_zustand4.setEnabled(True)
            self.lbl_bild_zustand4.setStyleSheet(u"background-color: rgb(0, 128, 0);\n""border-radius: 10px;")
        elif prediction==4 and max_probability==probabilities[0][4]:
            self.lbl_zustand5.setEnabled(True)
            self.lbl_bild_zustand5.setStyleSheet(u"background-color: rgb(0, 128, 0);\n""border-radius: 10px;")

    def concDataSet(self, data_string): # Trennung der erfassten Datastrings und Speicherung in Listen
        ax = []
        ay = []
        az = []
        total_data = []

        for chunk in data_string:
            data_set = chunk.split('\n')
            print("Data chunk:", data_set)

            for record in data_set:
                total_data = record.split(',')
                data_length = len(total_data)

                if data_length > 0:
                    if len(total_data[0]) > 1:
                        ax.append(float(total_data[0]))
                        total_data.append(float(total_data[0]))
                if data_length > 1:
                    if len(total_data[1]) > 1:
                        ay.append(float(total_data[1]))
                        total_data.append(float(total_data[1]))
                if data_length > 2:
                    if len(total_data[2]) > 1:
                        az.append(float(total_data[2]))
                        total_data.append(float(total_data[2]))

        return ax, ay, az, total_data

    def send_in_mdb(self, time, accel_x, accel_y, accel_z): # Senden die gesammelten Daten in MongoDB Atlas.
        #client = MongoClient ("localhost:27017") # Lokale Speicherung
        client = pymongo.MongoClient ("mongodb+srv://<benutzer>:<passwort>@cluster0.x7rthqc.mongodb.net/?retryWrites=true&w=majority") # Speicherung auf MongoDB Cloud
        db = client.MPU_data

        for i in range(0, len(accel_x)):
            collected_data = [{"time": time[i], "Ax": accel_x[i], "Ay": accel_y[i], "Az": accel_z[i], "date": str(datetime.datetime.now())}]
            result = db.acceleration_data.insert_many(collected_data)

    def visualize_data(self, accel_x): # Visualisierung der Beschleunigungs- und FFT-tranformierten Daten mit Matplotlib
        #client = MongoClient("localhost:27017") # Lokale Speicherung
        client = pymongo.MongoClient ("mongodb+srv://<benutzer>:<passwort>@cluster0.x7rthqc.mongodb.net/?retryWrites=true&w=majority") # Speicherung auf MongoDB Cloud
        db = client.MPU_data
        data_cleaned = db.acceleration_data.find({'Ax': {'$lt': 2}})

        a_x = [0]
        a_y = [0]
        a_z = [0]

        a_x = np.array(a_x)
        a_y = np.array(a_y)
        a_z = np.array(a_z)

        for data in data_cleaned:
            dict = dumps(data)
            obj = loads(dict)
            ax = obj['Ax']
            ay = obj['Ay']
            az = obj['Az']
            a_x = np.append(a_x, ax)
            a_y = np.append(a_y, ay)
            a_z = np.append(a_z, az)

        a_x = np.delete(a_x, 0)
        a_y = np.delete(a_y, 0)
        a_z = np.delete(a_z, 0)

        LengthSample = len(accel_x)
        fs = 200.0
        SampleNr = LengthSample
        Period = 1 / fs

        Ax = a_x
        Ay = a_y
        Az = a_z

        x_time = np.linspace(0.0, Period * SampleNr, SampleNr)
        x_freq = np.linspace(0.0, fs / 2.0, int(SampleNr / 2) + 1)

        ax_freq = self.calcFFT(Ax, SampleNr)
        ay_freq = self.calcFFT(Ay, SampleNr)
        az_freq = self.calcFFT(Az, SampleNr)

        plt.subplot(311)
        plt.title("Beschleunigungsdaten vom Sensor")
        plt.plot(x_time, Ax)
        plt.plot(x_time, Ay)
        plt.plot(x_time, Az)
        plt.subplot(312)
        plt.plot(x_freq, ax_freq)  # plot FFT for x-accel
        plt.plot(x_freq, ay_freq)  # plot FFT for y-accel
        plt.plot(x_freq, az_freq)  # plot FFT for z-accel
        plt.subplot(313)
        plt.psd(Ax, NFFT=LengthSample, Fs=fs, window=np.blackman(LengthSample))  # plot all axis as PSD
        plt.psd(Ay, NFFT=LengthSample, Fs=fs, window=np.blackman(LengthSample))  # plot ay-PSD
        plt.psd(Az, NFFT=LengthSample, Fs=fs, window=np.blackman(LengthSample))  # plot az-PSD
        plt.show()

    def start_process(self): # Initiieren der Programmausführung.
        self.remove_content()

        self.lbl_bild_zustand1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lbl_bild_zustand2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lbl_bild_zustand3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lbl_bild_zustand4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lbl_bild_zustand5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        TCP_IP = '192.168.1.107'
        TCP_PORT = 8000
        BUFFER_SIZE = 20480
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        print("Waiting for Connection...")
        s.listen(1)

        conn, addr = s.accept()
        print('Connection address:', addr)

        data_string = []
        defined_number = 5
        ax_data_res = 0
        ay_data_res = 0
        az_data_res = 0
        x_time_res = 0

        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            data_string.append(data.decode())
            print("Received data:", data_string)

            ax_single, ay_single, az_single, total_data = self.concDataSet(data_string)

            ax_data = []
            ay_data = []
            az_data = []

            length_ax_s = len(ax_single)
            length_ay_s = len(ay_single)
            length_az_s = len(az_single)

            if length_ax_s != length_ay_s or length_ax_s != length_az_s or length_ay_s != length_az_s:
                for value in ax_single:
                    ax_data.append(value)
                for value in ay_single:
                    ay_data.append(value)
                for value in az_single:
                    az_data.append(value)

            else:
                ax_data = ax_single
                ay_data = ay_single
                az_data = az_single

            LengthSample = len(ax_single)
            fs = 200.0
            Period = 1 / fs
            x_time = np.linspace(0.0, Period * LengthSample, LengthSample)

            if LengthSample > defined_number:
                ax_data_set = [ax_data[i] for i in range(-1 * (LengthSample - ax_data_res), 0)]
                ax_data_res = LengthSample

                ay_data_set = [ay_data[i] for i in range(-1 * (LengthSample - ay_data_res), 0)]
                ay_data_res = LengthSample

                az_data_set = [az_data[i] for i in range(-1 * (LengthSample - az_data_res), 0)]
                az_data_res = LengthSample

                x_time_set = [x_time[i] for i in range(-1 * (LengthSample - x_time_res), 0)]
                x_time_res = LengthSample

                defined_number = len(ax_data) + 5

                self.plot_chart(ax_data, ay_data, az_data, x_time)

                time.sleep(0.02)

                self.send_in_mdb(x_time_set, ax_data_set, ay_data_set, az_data_set)

                client = pymongo.MongoClient(
                    "mongodb+srv://<benutzer>:<passwort>@cluster0.x7rthqc.mongodb.net/?retryWrites=true&w=majority")  # Speicherung auf MongoDB Cloud
                db = client.MPU_data
                dataset = db.acceleration_data.find({'Ax': {'$lt': 2}})
                self.classification(dataset)

            #self.visualize_data(x_time) # Optional können die gesammelten Daten mit Matplotlib visualisiert werden

        conn.close()

        print("Done sampling")
        self.verbinden_microcontroller.setEnabled(True)

app = QApplication()
formular_main = analysis_washing()
formular_main.show()
sys.exit(app.exec())