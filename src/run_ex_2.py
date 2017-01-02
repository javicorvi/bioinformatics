# ---------------------------------------------------------------------------- #
# coding=utf-8
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# imports
import httplib, urllib
import xml.etree.ElementTree as ET
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Crea la conexion
#conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
# Hace la consulta
#conn.request("GET", "/entrez/eutils/esearch.fcgi?db=Nuccore&term=HUMAN")

params = urllib.urlencode({'db': 'nuccore','term':'HUMAN'})
conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
conn.request("POST", "/entrez/eutils/esearch.fcgi", params )

# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Obtiene la respuesta
r1 = conn.getresponse()
# Verifica que la respuesta es correcta
if not r1.status == 200 :
    print "Error en la conexión: " + r1.status + " " + r1.reason 
    exit()
# Lee el contenido de la respuesta
response = r1.read()
docXml = ET.fromstring(response)
# Cierra la conexion
conn.close()

print docXml.find("QueryTranslation").text
print docXml.find("Count").text
# Fin de la consulta
#print "{:15} {:45} {:10} ".format(docXml.find("eSearchResult/Count").text, docXml.find("eSearchResult/From").text, docXml.find("eSearchResult/To").text) 

