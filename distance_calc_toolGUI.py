# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distance_calc_tool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_csv_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_csv_button.setGeometry(QtCore.QRect(30, 10, 133, 23))
        self.load_csv_button.setObjectName("load_csv_button")
        self.csv_filepath_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.csv_filepath_lineEdit.setGeometry(QtCore.QRect(170, 10, 594, 20))
        self.csv_filepath_lineEdit.setReadOnly(False)
        self.csv_filepath_lineEdit.setObjectName("csv_filepath_lineEdit")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(30, 140, 133, 23))
        self.run_button.setObjectName("run_button")
        self.latitude_input_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.latitude_input_1.setGeometry(QtCore.QRect(170, 110, 281, 20))
        self.latitude_input_1.setObjectName("latitude_input_1")
        self.longitude_input_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.longitude_input_1.setGeometry(QtCore.QRect(470, 110, 291, 20))
        self.longitude_input_1.setObjectName("longitude_input_1")
        self.lat_label = QtWidgets.QLabel(self.centralwidget)
        self.lat_label.setGeometry(QtCore.QRect(290, 90, 47, 13))
        self.lat_label.setObjectName("lat_label")
        self.lon_label = QtWidgets.QLabel(self.centralwidget)
        self.lon_label.setGeometry(QtCore.QRect(590, 90, 47, 13))
        self.lon_label.setObjectName("lon_label")
        self.txt = QtWidgets.QTextEdit(self.centralwidget)
        self.txt.setGeometry(QtCore.QRect(32, 170, 731, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt.sizePolicy().hasHeightForWidth())
        self.txt.setSizePolicy(sizePolicy)
        self.txt.setAutoFillBackground(False)
        self.txt.setReadOnly(True)
        self.txt.setObjectName("txt")
        self.output_csv_button = QtWidgets.QPushButton(self.centralwidget)
        self.output_csv_button.setGeometry(QtCore.QRect(30, 50, 133, 23))
        self.output_csv_button.setObjectName("output_csv_button")
        self.output_filepath_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.output_filepath_lineEdit.setGeometry(QtCore.QRect(170, 50, 594, 20))
        self.output_filepath_lineEdit.setObjectName("output_filepath_lineEdit")
        self.use_fields_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.use_fields_checkbox.setGeometry(QtCore.QRect(30, 110, 133, 17))
        self.use_fields_checkbox.setChecked(False)
        self.use_fields_checkbox.setObjectName("use_fields_checkbox")
        self.latitude_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.latitude_input_2.setGeometry(QtCore.QRect(170, 140, 281, 20))
        self.latitude_input_2.setObjectName("latitude_input_2")
        self.longitude_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.longitude_input_2.setGeometry(QtCore.QRect(470, 140, 291, 20))
        self.longitude_input_2.setObjectName("longitude_input_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculate distance"))
        self.load_csv_button.setText(_translate("MainWindow", "Load CSV"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.lat_label.setText(_translate("MainWindow", "Latitude"))
        self.lon_label.setText(_translate("MainWindow", "Longitude"))
        self.output_csv_button.setText(_translate("MainWindow", "Output CSV"))
        self.use_fields_checkbox.setText(_translate("MainWindow", "manual input"))

