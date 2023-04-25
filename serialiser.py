from Classe_Etudiant import *

etud = Etudiant("1234567", "Hasna", "information")

etud.serialisation("FichierSerialiser1.json")


etud1 = Etudiant()

etud1.deserialisation("FichierSerialiser1.json")

print(etud1)
