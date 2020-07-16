#utilisation du module os pour pouvoir interagir avec le systeme.

import os


#creation d'une classe pour rendre le programme oriente objet
class GetInfo:
    infos = os.uname()
    currentUser = os.getlogin()
    rep_actuel = os.getcwd()

    def listInfo(self):
        #afficher des informations sur le systeme
        print "Informations du systeme :{} ".format(GetInfo.infos)
        #afficher l'utilisateur actuel
        print "Current user : {} \n".format(GetInfo.currentUser)
        #afficher le path du repertoire actuel
        print "Repertoire actuel : {} \n".format(GetInfo.rep_actuel)


    def scan():
        myDirectory="C:/Users/"
        p = Path(myDirectory)
        for x in os.scandir(p):
            print(x)


#instance de l'objet GetInfo (creation de l'objet)
GetMyInfo = GetInfo()

GetMyInfo.listInfo()
