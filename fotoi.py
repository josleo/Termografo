import telebot
import time
import MySQLdb
import serial
import requests
import socket
from time import sleep
import picamera
from subprocess import call
import random
from os import remove
from ftplib  import  FTP
import os
from datetime import date
from datetime import datetime
import serial
from numpy import *
import matplotlib.pyplot as plt
from pylab import *
from ftplib  import  FTP
import os
from datetime import datetime
import random



con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#habriremos a unestro bot en telegram 
#       943769984:AAGOjMs0T4Vu9-fuGzUcZ1fVU3YQctbupAE"
#bot = telebot.TeleBot("2144733880:AAHzAlgDJ4Vhx0dF03goBcpApbrHwn2EVs4")
from TokenTelegram import tokenAlerta
bot = telebot.TeleBot(tokenAlerta)
#usaremos el id del numero a quien se le enviara 
chat_id="1051367732"
now = datetime.now()
#nom = (str(now)+'.jpg')
#con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#intenta conectarse a una url con el socket creado
try:
    con.connect(('www.wikipedia.org', 80))
#si existe conexion a internet se tomara una foto y se enviara  al telegram y al servidor 
#    os.system('python foto-termica.py')

    #servidor de la apgina oficial
    servidor="ftp.educatics.org"
    user="polinnes@polines.educatics.org"
    passw="Led([967Ku.h"

    #ftp_raiz     = '/htdocs/img' # donde queremos subir el fichero
    ftp_raiz     = '/public/img/fotos_camara/' 

    fichero_origen='/home/pi/termica/imagen.jpg'

    #now = datetime.now()
    nom = (str(now)+'.jpg')
    fichero_foto=('_'.join(nom.split()))

    #print fichero_foto
    try:

	with picamera.PiCamera() as camera:
                camera.capture("/home/pi/termica/imagen.jpg")


        photo = open('/home/pi/termica/imagen.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        s=FTP(servidor)
        s.login(user, passw)


        try:

            f = open(fichero_origen, 'rb')
            s.cwd(ftp_raiz)
            s.storbinary('STOR ' + fichero_foto, f)
            f.close()
            s.quit()
            print  "enviada la foto camara al hosting"

        except:

            print "no se envio la foto al hosting"

    except :

            bot.send_message(chat_id, "Fallo al  arrancar la camara, prueba mas tarde")
	    con.close()

except:
# si no existe una conexion de interne se enviara la foto a una carpeta llamada fotos(fotos/imagenes.jpg)
    print "no hay internet para enviar la foto"

    #now = datetime.now()
    nom = (str(now)+'.jpg')
    fichero_foto=('_'.join(nom.split()))
#    print fichero_foto
    with picamera.PiCamera() as camera:
            camera.capture("/home/pi/termica/fotos/"+fichero_foto)
    #fichero_foto="null"
#    print "no hay no internet"

#con.close()














