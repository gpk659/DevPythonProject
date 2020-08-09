#utilisation du module os pour pouvoir interagir avec le systeme.

import os, sys, platform, getpass

#creation d'une classe pour rendre le programme oriente objet
class GetInfo:
    infos = platform.uname()
    currentUser = getpass.getuser()
    rep_actuel = os.chdir('../')
    myDirectory = os.listdir("C:/Users/Grégory/Documents")
    scanpath = "\nListe de tous les repertoires dans Users : \n"

    def listInfo(self):
        #afficher des informations sur le systeme
        print ("Informations du systeme :\n{} ".format(GetInfo.infos))
        #afficher l'utilisateur actuel
        print ("\nCurrent user :\n{} \n".format(GetInfo.currentUser))
        #afficher le path du repertoire actuel
        print ("\nRepertoire actuel :\n{} \n".format(GetInfo.rep_actuel))

    def scan(self):
        #print ("Liste de tous les repertoires dans Users/")
        #on liste toutes les directories et sous directories
        for file in GetInfo.myDirectory:
            GetInfo.scanpath += file + "; \n"
        print (GetInfo.scanpath)



#instance de l'objet GetInfo (creation de l'objet)
GetMyInfo = GetInfo()
# afficage des infos de l'objet
GetMyInfo.listInfo()
GetMyInfo.scan()
