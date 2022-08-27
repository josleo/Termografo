
#import  mysq
import MySQLdb


database =MySQLdb.connect(host="educatics.org",port=3306,user="educaics_polines",passwd="educaics_polines",db="educaics_polines")
cursor = database.cursor()
cursor.execute("select temperatura_polin  from resumenes order by  id_resumen  DESC  limit 1")
for base in cursor:
    print str(base)
print base 
database.close()
print base

