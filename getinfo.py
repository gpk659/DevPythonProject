#utilisation du module os pour pouvoir interagir avec le systeme.

import os
from pathlib import Path

#afficher des informations sur le systeme
infoos = os.uname()
print "Informations du systeme :\n {} \n".format(infoos)

#afficher l'utilisateur actuel
currentUser = os.getlogin()
print "Current user :\n {} \n".format(currentUser)

#afficher le path du repertoire actuel
rep_actuel = os.getcwd()
print "Repertoire actuel :\n {} \n".format(rep_actuel)


myDirectory="C:/Users/"
p = Path(myDirectory)
for x in os.scandir(p):
    print(x)
