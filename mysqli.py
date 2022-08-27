import socket
import csv
import MySQLdb

#database = MySQLdb.connect(host='10.200.10.125', user='spaine', passwd='spaine', db='scat')





con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #intenta conectarse a una url con el socket creado
try:
	con.connect(('www.google.com', 80))

#	database  = MySQLdb.connect(host="remotemysql.com",user="V2ZwygndKS",passwd="KQl2hyRgok",db="V2ZwygndKS")
	#database=MySQLdb.connect("localhost","root","123456","polines")

	database =MySQLdb.connect(host="educatics.org",port=3306,user="educaics_polines",passwd="educaics_polines",db="educaics_polines")
	cursor = database.cursor()

	csv_file = '/home/pi/termica/datas.csv'

	csv_data = csv.reader(file(csv_file))


	for row in csv_data:
		print row
		#cursor.execute('''INSERT INTO ejemplo5 (sensor,fecha,nombre,apellido,condicion,foto,termica) VALUES(%s,%s,%s,%s,%s,%s,%s)''', row)
                cursor.execute('''INSERT INTO resumenes  (id_local,id_nivel,temperatura_polin,temperatura_ambiente,fecha,imagen_termica,imagen_real,estado,created_at,updated_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', row)


	database.commit()  # Make sure data is committed to the database

	database.close()

	with open("/home/pi/termica/datas.csv",'w') as f:
		pass
	con.close()

except:


	print "no se subio los datos reunidos hasta el momento"

#con.close()

