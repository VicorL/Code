import liste_etude
from Classe_Etudiant import *

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot


class Fenetre_listview(QtWidgets.QDialog, liste_etude.Ui_FenetreListView):
    def __init__(self, parent=None):
        super(Fenetre_listview, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste d'étudiant.e.s")

    @pyqtSlot()
    def on_Button_quitter_clicked(self):
        self.close()
