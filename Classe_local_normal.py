from Classe_local import *

class Local_normal(Local):
    """

    """
    def __init__(self, p_nb_place_table=0, p_type="", p_num="", p_lieu="", p_dimension=0, p_place=0):
        """
        """
        Local.__init__(self, p_type, p_num, p_lieu, p_dimension, p_place)
        self._nb_place_table = p_nb_place_table

    # Propriété
    def _get_nb_place_table(self):
        return self._nb_place_table
    def _set_nb_place_table(self, valeur):
        if valeur == "1" or valeur == "2":
            self._nb_place_table = int(valeur)

    Nb_place_table = property(_get_nb_place_table, _set_nb_place_table)
