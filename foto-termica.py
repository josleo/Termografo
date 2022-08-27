import serial
from numpy import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from datetime import date

today = date.today()


ser = serial.Serial('/dev/ttyACM0',9600)
#ser = serial.Serial('/dev/ttyUSB0')

read = 0
element = 0
counter = 0

w, h = 8, 8;
Matrix = [[0 for x in range(w)] for y in range(h)] 

x = 0;
y = 0;



while 1:
	while 1:
		char = ser.read()
                
		if read==1:
			if char==",":
						
				Matrix[x][y]=element
				x=x+1
				element = 0
				counter = 0
				ser.read()
			elif ord(char)==13:
				y=y+1
				x=0
				element = 0
				counter = 0
				ser.read()
			elif char == "]":
				read=0
#				print Matrix
				#print "Done"
				x=0
				y=0
				break
			elif char!=".":

#				print element
				element = element + int(char)*pow(10, 1-counter)
				counter = counter+1
#				print  counter                                
		if char == "[":
			read=1

	
	matriz = np.array( Matrix)
	 #matriz[2::].max()

        plt.figure()

        conf_arr = np.array(Matrix)
        #plt.plot(y)
        #plt.matshow(conf_arr,)
        plt.matshow(conf_arr,cmap = plt.get_cmap('jet'),interpolation='nearest')
#       plt.figure()
        #plt.imshow(conf_arr,cmap = plt.get_cmap('jet'), vmin=10, vmax=30)

        #im = plt.imshow(conf_arr,cmap = plt.get_cmap('jet'))
        #plt.colorbar(im)

        plt.colorbar()
	plt.title(today.strftime("%B %d, %Y"+'\n' + time.strftime("%X") +'\n' ))
        #plt.title("..................")

	plt.xlabel(matriz[4::].max(), family='serif', color='r', weight='normal',size = 16,labelpad = 6)
        plt.savefig('/home/pi/termica/termica.png', format='png')
	plt.show()
        print "ejecutado camara termica de arduino puerto serial"
        break
        sys.exit()
