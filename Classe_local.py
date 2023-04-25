class Local:
    """

    """
    ls_locaux = []
    def __init__(self, p_type="", p_num="", p_lieu="", p_dimension=0, p_place=0):
        """

        """
        self._type_loc = p_type
        self._num_loc = p_num
        self.lieu_loc = p_lieu
        self._dimension_loc = p_dimension
        self._nbr_places = p_place
        self.ls_locaux.append(self)

    # Propriétées
    # Propriété Type_loc
    def _get_type_loc(self):
        return self._type_loc
    def _set_type_loc(self, valeur):
        if valeur == "Technique" or valeur == "Normal":
            self._type_loc = valeur

    Type_loc = property(_get_type_loc, _set_type_loc)

    # Propriété Num_loc
    def _get_num_loc(self):
        return self._num_loc
    def _set_num_loc(self, valeur):
        ls_loc = []
        nb_car = 0
        for car in valeur:
            ls_loc.append(car)
            nb_car += 1
        a = True
        for elt in ls_loc[2:5]:
            try: int(elt)
            except ValueError:
                a = False
        if ls_loc[0].isalpha and ls_loc[1] == "-" and a == True and nb_car == 5:
            self._num_loc = valeur

    Num_loc = property(_get_num_loc, _set_num_loc)

    # Propriété Dimension_loc
    def _get_dimension_loc(self):
        return self._dimension_loc
    def _set_dimension_loc(self, valeur):
        if valeur > 0:
            self._dimension_loc = valeur

    Dimension_loc = property(_get_dimension_loc, _set_dimension_loc)

    # Propriété Nbr_places
    def _get_nbr_places(self):
        return self._nbr_places
    def _set_nbr_places(self, valeur):
        nb = int(valeur)
        if 0 < nb > 25:
            self._nbr_places = nb

    Nbr_places = property(_get_nbr_places, _set_nbr_places)


