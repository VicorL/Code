import gestion_scolarite
from listview_dialog import *
from Classe_Etudiant import *
from local_dialog import *

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *


class MaFenetre(QtWidgets.QMainWindow, gestion_scolarite.Ui_MainWindow):

    def __init__(self, parent=None):
        """

        :param parent:
        """
        super(MaFenetre,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_Button_ajouter_clicked(self):
        self.label_erreur.clear()
        etud = Etudiant()
        etud.Nb_etudiant = self.Edit_num.text()
        etud.Nom = self.Edit_nom.text()
        etud.prgm = self.Box_prgm.currentText()
        etud.Naiss = self.dateEdit_naiss.date()
        if etud.Nb_etudiant == "":
            self.label_erreur.setText("Attention: Le numéro étudiant entré est incorrecte !")
            self.Edit_num.clear()
        elif etud.Nb_etudiant == "deja":
            self.label_erreur.setText("Attention: Ce numéro est déjà utilisé !")
            self.Edit_num.clear()
        elif etud.Nom == "":
            self.label_erreur.setText("Attention: Le nom entré est incorrecte !")
            self.Edit_nom.clear()
        elif etud.prgm == "":
            self.label_erreur.setText("Attention: Le programme entré est incorrecte !")
        elif etud.age(etud.Naiss) == 0:
            self.label_erreur.setText("Attention: L'étudiant est trop jeune !")
        else:
            Etudiant.ls_etudiants.append(etud)
            self.Browser_message.append(etud.__str__())


    @pyqtSlot()
    def on_Button_modifier_clicked(self):
        mat = self.Edit_num.text()
        nom = self.Edit_nom.text()
        prgm = self.Box_prgm.currentText()

        for etudiant in Etudiant.ls_etudiants:
            num = etudiant.nb_etudiant
            if mat == num:
                etudiant.Nom = nom
                if etudiant.Nom != nom:
                    self.Edit_nom.clear()
                    self.label_erreur.setText("Attention: Le nouveau nom entré est incorrecte !")
                    break
                if prgm == "":
                    self.label_erreur.setText("Attention: Le programme entré est incorrecte !")
                    break
                etudiant.Naiss = self.dateEdit_naiss.date()
                etudiant.prgm = prgm
                self.Browser_message.append(etudiant.__str__())
                break

    @pyqtSlot()
    def on_Button_supprimer_clicked(self):
        mat = self.Edit_num.text()
        for etudiant in Etudiant.ls_etudiants:
            num = etudiant.nb_etudiant
            if mat == num:
                self.Browser_message.append(f"L'étudiant, {etudiant.nom}, attribué le maticule {etudiant.nb_etudiant} a été supprimer.")
                Etudiant.ls_etudiants.remove(etudiant)
                break

    @pyqtSlot()
    def on_Button_sauvegarder_clicked(self):
        chaine = ""
        for etudiant in Etudiant.ls_etudiants:
            chaine += etudiant.__str__()
        with open(file="Sauvegarde.txt", mode="w", encoding="windows-1252") as f:
            f.write(chaine)

    @pyqtSlot()
    def on_Button_list_clicked(self):
        dialog = Fenetre_listview()

        model = QStandardItemModel()

        for e in Etudiant.ls_etudiants:
            item = QStandardItem(e.Nb_etudiant + " " + e.Nom)
            model.appendRow(item)
        dialog.View_etudiants.setModel(model)
        dialog.setModal(True)
        dialog.show()
        dialog.exec()

    @pyqtSlot()
    def on_Button_local_clicked(self):
        dialog = Fenetre_local()
        dialog.setModal(True)
        dialog.show()
        dialog.exec()


def main():
    """

    :return:
    """
    mon_app = QtWidgets.QApplication(sys.argv)
    mon_form = MaFenetre()
    mon_form.show()
    mon_app.exec()


if __name__ == "__main__":
    main()
