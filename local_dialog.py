import local
from local import *
from Classe_local_technique import *
from Classe_local_normal import *

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot


class Fenetre_local(QtWidgets.QDialog, local.Ui_Fenetre_Local):
    def __init__(self, parent=None):
        super(Fenetre_local, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Local")
        self.Cacher_moitie_droite()
        self.Box_Type.currentIndexChanged.connect(self.on_Box_Type_activated)


    @pyqtSlot()
    def on_Box_Type_activated(self):
        self.Cacher_moitie_droite()
        if self.Box_Type.currentText() == "Normal":
            self.label_nombre_place_table.setVisible(True)
            self.Box_nb_places_table.setVisible(True)
            self.Button_ajouter.setVisible(True)
        elif self.Box_Type.currentText() == "Technique":
            self.Button_ajouter.setVisible(True)
            self.Edit_marque_ordi.setVisible(True)
            self.Box_projecteur.setVisible(True)
            self.label_marque_ordi.setVisible(True)
            self.label_nb_ordi.setVisible(True)
            self.label_projecteur.setVisible(True)
            self.spinBox_nb_ordi.setVisible(True)
        else:
            self.Cacher_moitie_droite()

    @pyqtSlot()
    def on_Button_ajouter_clicked(self):
        type_loc = self.Box_Type.currentText()
        if type_loc == "Normal":
            self.loc_normal()
        elif type_loc == "Technique":
            self.loc_tech()


    def loc_normal(self):
        normal = Local_normal()
        normal.Type_loc = self.Box_Type.currentText()
        normal.lieu_loc = self.Box_Lieu.currentText()
        normal.Num_loc = self.Edit_num_loc.text()
        normal.Dimension_loc = self.Edit_dimension.text()
        normal.Nbr_places = self.spinBox_place.text()
        normal.Nb_place_table = self.Box_nb_places_table.currentText()



    def loc_tech(self):
        tech = Local_Technique()
        tech.Type_loc = self.Box_Type.currentText()
        tech.lieu_loc = self.Box_Lieu.currentText()
        tech.Num_loc = self.Edit_num_loc.text()
        tech.Dimension_loc = self.Edit_dimension.text()
        tech.Nbr_places = self.spinBox_place.text()
        tech.Marque_ordi = self.Edit_marque_ordi.text()
        tech.Nb_ordi = self.spinBox_nb_ordi.text()

        proj = self.Box_projecteur.currentText()
        if proj == "Vrai":
            tech.projecteur = True
        else:
            tech.projecteur = False



    def Cacher_moitie_droite(self):
        self.Box_nb_places_table.setVisible(False)
        self.Button_ajouter.setVisible(False)
        self.Edit_marque_ordi.setVisible(False)
        self.Box_projecteur.setVisible(False)
        self.label_marque_ordi.setVisible(False)
        self.label_nb_ordi.setVisible(False)
        self.label_nombre_place_table.setVisible(False)
        self.label_projecteur.setVisible(False)
        self.spinBox_nb_ordi.setVisible(False)
