import socket
import subprocess

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
# avec un nombre maximum de connexions qu'il peut recevoir sur ce port sans les accepter
s.listen(5)
print "socket is listening"

# on etabli la connection avec le client
client, addr = s.accept()
print 'Got connection from', addr
cmdlet = client.recv(2048).decode()

# gestion des erreurs
while cmdlet!='quit':

    print(cmdlet)
    # convertion en chaine de caractere
    cmdlet=str(cmdlet)
    # on execute la commande passee via le remote shell
    # avec un subprocess, le parametre TRUE signifie que cela sera fait dans un autre shell
    # on affiche ensuite le resultat avec un print()
    resultat = subprocess.check_output(cmdlet,shell=True)
    print(resultat)
    # on envoie le resultat de la commande.
    client.send(resultat)
    cmdlet = client.recv(2048).decode()

# on ferme les connections
cmdlet.close()
s.close()
