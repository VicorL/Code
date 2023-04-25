import datetime
import json


class Etudiant:
    """
    Classe Etudiant.
    """
    ls_etudiants = []

    def __init__(self, p_nb_etudiant="", p_nom="", p_prgm="", p_naiss=datetime.date.today()):
        """
        Constructeur de la classe Etudiant.
        :param p_nb_etudiant:
        :param p_nom:
        :param p_naiss:
        :param p_prgm:
        """
        self.prgm = p_prgm
        self.nb_etudiant = p_nb_etudiant
        self.nom = p_nom
        self.naiss = p_naiss

    ## Propriétés
    # Propriété Nb_etudiant
    def _get_nb_etudiant(self):
        return self.nb_etudiant

    def _set_nb_etudiant(self, valeur):
        while True:
            try:
                int(valeur)
            except ValueError:
                a = False
                break
            else:
                a = True
                break
        b = True
        for etudiant in Etudiant.ls_etudiants:
            num = etudiant.nb_etudiant
            if valeur == num:
                b = False
        if a == True and b == True:
            self.nb_etudiant = valeur
        elif not b:
            self.nb_etudiant = "deja"

    Nb_etudiant = property(_get_nb_etudiant, _set_nb_etudiant)

    # Propriété Nom
    def _get_nom(self):
        return self.nom

    def _set_nom(self, nouv_nom):
        validation = nouv_nom.isalpha()
        if validation == True:
            self.nom = nouv_nom

    Nom = property(_get_nom, _set_nom)

    def _get_naiss(self):
        return self.naiss

    def _set_naiss(self, p_naiss):
        if self.age(p_naiss) >= 17:
            self.naiss = p_naiss

    Naiss = property(_get_naiss, _set_naiss)

    def age(self, p_date):
        maintenant = datetime.date.today()
        age = maintenant.year - p_date.year() - ((maintenant.month, maintenant.day) < (p_date.month(), p_date.day()))
        return age


    # Méthode string
    def __str__(self):
        return f"""
*************************
    Numéro étudiant : {self.Nb_etudiant}
    Nom : {self.Nom}
    Âge : {self.age(self.Naiss)}
    Programme : {self.prgm}
*************************
"""

    def serialisation(self, p_fichier):
        self.__dict__["_Etudiant__date_naiss"]=str(self.Naiss)

        try:
            with open(p_fichier, "w") as f:
                json.dump(self.__dict__, f)

        except:
            return 0

        else:
            return 1

    def deserialisation(self, p_fichier):

        try:
            with open(p_fichier, "r") as f :
                self.__dict__ = json.load(f)
        except:
            return 0
        else:
            return 1
