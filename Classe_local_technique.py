from Classe_local import *

class Local_Technique(Local):
    """

    """
    def __init__(self, p_marque_ordi="", p_nb_ordi=0, p_projecteur=False,p_type="", p_num="", p_lieu="", p_dimension=0, p_place=0):
        """
        """
        Local.__init__(self, p_type, p_num, p_lieu, p_dimension, p_place)
        self._marque_ordi = p_marque_ordi
        self._nb_ordi = p_nb_ordi
        self.projecteur = p_projecteur

    # Propriétées
    # Propriété Marque_ordi
    def _get_marque_ordi(self):
        return self._marque_ordi
    def _set_marque_ordi(self, valeur):
        if len(valeur) < 100:
            self._marque_ordi = valeur

    Marque_ordi = property(_get_marque_ordi, _set_marque_ordi)

    # Propriété Nb_ordi
    def _get_nb_ordi(self):
        return self._nb_ordi
    def _set_nb_ordi(self, valeur):
        nb = int(valeur)
        if 0 < nb < 25:
            self._nb_ordi = nb

    Nb_ordi = property(_get_nb_ordi, _set_nb_ordi)
