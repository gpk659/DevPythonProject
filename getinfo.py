#utilisation du module os pour pouvoir interagir avec le systeme.

import os,sys

#creation d'une classe pour rendre le programme oriente objet
class GetInfo:
    infos = os.uname()
    currentUser = os.getlogin()
    rep_actuel = os.getcwd()
    myDirectory = os.listdir("/Users/")
    scanpath = "Liste de tous les repertoires dans Users : \n"

    def listInfo(self):
        #afficher des informations sur le systeme
        print "Informations du systeme :{} ".format(GetInfo.infos)
        #afficher l'utilisateur actuel
        print "Current user : {} \n".format(GetInfo.currentUser)
        #afficher le path du repertoire actuel
        print "Repertoire actuel : {} \n".format(GetInfo.rep_actuel)

    def scan(self):
        print "Liste de tous les repertoires dans Users/"
        #on liste toutes les directories et sous directories
        for file in GetInfo.myDirectory:
            GetInfo.scanpath += file + "; \n"
        print GetInfo.scanpath



#instance de l'objet GetInfo (creation de l'objet)
GetMyInfo = GetInfo()
# afficage des infos de l'objet
GetMyInfo.listInfo()
GetMyInfo.scan()
