# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Prog2\Qt_Exercise_etud\gestion_scolarite.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ajouter.setGeometry(QtCore.QRect(50, 300, 141, 51))
        self.Button_ajouter.setObjectName("Button_ajouter")
        self.Edit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.Edit_nom.setGeometry(QtCore.QRect(50, 130, 221, 41))
        self.Edit_nom.setObjectName("Edit_nom")
        self.label_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_nom.setGeometry(QtCore.QRect(50, 100, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.label_num = QtWidgets.QLabel(self.centralwidget)
        self.label_num.setGeometry(QtCore.QRect(50, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_num.setFont(font)
        self.label_num.setObjectName("label_num")
        self.Edit_num = QtWidgets.QLineEdit(self.centralwidget)
        self.Edit_num.setGeometry(QtCore.QRect(50, 40, 221, 41))
        self.Edit_num.setObjectName("Edit_num")
        self.Browser_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.Browser_message.setGeometry(QtCore.QRect(50, 380, 321, 171))
        self.Browser_message.setObjectName("Browser_message")
        self.label_erreur = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur.setGeometry(QtCore.QRect(330, 30, 421, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur.setFont(font)
        self.label_erreur.setText("")
        self.label_erreur.setObjectName("label_erreur")
        self.label_prgm = QtWidgets.QLabel(self.centralwidget)
        self.label_prgm.setGeometry(QtCore.QRect(50, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_prgm.setFont(font)
        self.label_prgm.setObjectName("label_prgm")
        self.Box_prgm = QtWidgets.QComboBox(self.centralwidget)
        self.Box_prgm.setGeometry(QtCore.QRect(50, 240, 221, 31))
        self.Box_prgm.setObjectName("Box_prgm")
        self.Box_prgm.addItem("")
        self.Box_prgm.setItemText(0, "")
        self.Box_prgm.addItem("")
        self.Box_prgm.addItem("")
        self.Box_prgm.addItem("")
        self.Box_prgm.addItem("")
        self.Box_prgm.addItem("")
        self.Button_supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.Button_supprimer.setGeometry(QtCore.QRect(230, 300, 141, 51))
        self.Button_supprimer.setObjectName("Button_supprimer")
        self.Button_modifier = QtWidgets.QPushButton(self.centralwidget)
        self.Button_modifier.setGeometry(QtCore.QRect(410, 300, 141, 51))
        self.Button_modifier.setObjectName("Button_modifier")
        self.Button_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.Button_sauvegarder.setGeometry(QtCore.QRect(590, 300, 141, 51))
        self.Button_sauvegarder.setObjectName("Button_sauvegarder")
        self.dateEdit_naiss = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_naiss.setGeometry(QtCore.QRect(350, 240, 231, 31))
        self.dateEdit_naiss.setObjectName("dateEdit_naiss")
        self.label_naiss = QtWidgets.QLabel(self.centralwidget)
        self.label_naiss.setGeometry(QtCore.QRect(350, 200, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_naiss.setFont(font)
        self.label_naiss.setObjectName("label_naiss")
        self.Button_list = QtWidgets.QPushButton(self.centralwidget)
        self.Button_list.setGeometry(QtCore.QRect(590, 380, 141, 51))
        self.Button_list.setObjectName("Button_list")
        self.Button_local = QtWidgets.QPushButton(self.centralwidget)
        self.Button_local.setGeometry(QtCore.QRect(410, 380, 141, 51))
        self.Button_local.setObjectName("Button_local")
        self.Button_serialiser = QtWidgets.QPushButton(self.centralwidget)
        self.Button_serialiser.setGeometry(QtCore.QRect(410, 450, 141, 51))
        self.Button_serialiser.setObjectName("Button_serialiser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuGestion_de_scolarit = QtWidgets.QMenu(self.menubar)
        self.menuGestion_de_scolarit.setObjectName("menuGestion_de_scolarit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGestion_de_scolarit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.label_nom.setText(_translate("MainWindow", "Nom de l\'étudiant"))
        self.label_num.setText(_translate("MainWindow", "Numéro étudiant"))
        self.label_prgm.setText(_translate("MainWindow", "Programme"))
        self.Box_prgm.setItemText(1, _translate("MainWindow", "Science humaine"))
        self.Box_prgm.setItemText(2, _translate("MainWindow", "Science nature"))
        self.Box_prgm.setItemText(3, _translate("MainWindow", "Informatique"))
        self.Box_prgm.setItemText(4, _translate("MainWindow", "Biotechnicien"))
        self.Box_prgm.setItemText(5, _translate("MainWindow", "Technique policière"))
        self.Button_supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.Button_modifier.setText(_translate("MainWindow", "Modifier"))
        self.Button_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.dateEdit_naiss.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.label_naiss.setText(_translate("MainWindow", "Date de naissance de l\'étudiant"))
        self.Button_list.setText(_translate("MainWindow", "ListView"))
        self.Button_local.setText(_translate("MainWindow", "Ajouter Local"))
        self.Button_serialiser.setText(_translate("MainWindow", "Sérialiser"))
        self.menuGestion_de_scolarit.setTitle(_translate("MainWindow", "Gestion de scolarité"))
