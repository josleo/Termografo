
import socket
import os
from TokenTelegram import * #improtamos las variables de tokentelgram.py para mejor manejo

#con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #intenta conectarse a una url con el socket creado
try:

	con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        con.connect(('www.google.com', 80))

	##importamos los modulos que vamos a utilizar
	#from ftplib import FT
	from ftplib import FTP
	#import remove
	#import ftputil
	import os
	from os import remove
#	from TokenTelegram import * #improtamos las variables de tokentelgram.py para mejor manejo

	##definimos las varialbes de trabajo

## basepath: la ruta de destino dentro del servidor ftp
#basepath = "/htdocs/python/"
	basepath ='/public/img/fotos_camara/'
#base : ruta de origen en nuestro equipo local
	base = "/home/pi/termica/fotos/"
## relativa: ruta de salida al iniciar el recorrido
##por el arbol de directorios
	relativa = "./"

##datos de conexion al ftp extralemos todos estos datos de tokentelgram.py para mejor manejo
#
#	print ftphost
#	ftphost="ftp.soft.pe"
#	ftpuser="polines@polines.soft.pe"
#	ftppass="innova_polines"
#	ftphost="ftp.educatics.org"
#	ftpuser="polinnes@polines.educatics.org"
#	ftppass="Led([967Ku.h"


# filtro: nos permite discriminar que tipos
#de ficheros queremos subir en cada momento,
#ahorraremos tiempo evitando hacer comprobaciones
#sobre ficheros que sabemos que no es necesario
#subir en este momento
	filtro=('.jpg')
##filtro=('.png')'''
##filtro=('image.php','imagen.php','logo.png')

## nos creamos una funcion para recorrer el
##arbol de directorios de forma recursiva
	print "hasta aqui"

	def recorrer(base,relativa):
    	    global ftp
            global basepath
#obtenemos la lista de directorios y
#ficheros del directorio actual
    	    namesl = os.listdir(base+relativa)
 ##    recorremos la lista de elementos
    	    for namel in namesl:
      ##   si es un fichero
        	if  os.path.isfile(base+relativa+namel):
            	    if namel.lower().endswith(filtro):
                ## si la version local es mas nueva que la del servidor, lo subimos
                #if ftp.upload_if_newer(base+relativa+namel, basepath+relativa+namel,'b') == True:
                	if ftp.storbinary('STOR ' +  basepath+namel, open(base+namel, 'rb')):
## informamos de que un fichero se ha subido
                        	print "Actualizado:"+base+namel+" -> "+basepath+namel
                        	remove(base+namel)

        ## si es un directorio llamamos de nuevo
        ## si es un directorio llamamos de nuevo
##a la funcion para recorrerlo
##(bajamos un nivel, como en Origen)
	        if os.path.isdir(base+relativa+namel):
        	    if namel!=".":
                	if namel!="..":
                    	    recorrer(base,relativa+namel+"/")


#Ahora ya lo tenemos todo definido, empieza la ejecucion del script.
##abrimos conexion ftp
#ftp = ftputil.FTPHost(ftphost, ftpuser, ftppass)
## nos situamos en el directorio remoto adecuado
	ftp = FTP(ftphost)
	ftp.login(ftpuser,ftppass)
## iniciamos recorrido por el arbol de directorios local,
###ejecutamos la funcion que definimos arriba.
	recorrer(base, relativa)

## cerramos la conexion
	ftp.close()

	print  " disparador  envio  las fotos de la camara ftp"

	con.close()

except:


        print "disparador - no envio nungun foto de la camara  al servidor- "

#con.close()

