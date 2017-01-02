# ---------------------------------------------------------------------------- #
# coding=utf-8
# ---------------------------------------------------------------------------- #
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=Klebsiella%20pneumoniae%20MGH%2078578
#http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1328388
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
print "BEGIN"
params = urllib.urlencode({'db': 'nuccore','term':'complete sequence[Title] NOT (rna[Title] AND plasmid[Title])'})
conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
conn.request("POST", "/entrez/eutils/esearch.fcgi", params )
r1 = conn.getresponse()
if not r1.status == 200 :
    print "Error en la conexión: " + r1.status + " " + r1.reason 
    exit()
# Lee el contenido de la respuesta
response = r1.read()
docXml = ET.fromstring(response)
save_file = open("ejercicio_c.xml", "w")
save_file.write(response)
save_file.close()
r1.close
conn.close()
#El primero es seleccionado
#http://www.ncbi.nlm.nih.gov/nuccore/1068647189?report=fasta
ident = docXml.find("IdList")[0]
params = urllib.urlencode({'db':'nuccore','id':ident.text,'rettype':'fasta','retmode':'text'})
conn2 = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")

#efetch.fcgi?db=nuccore&id=25026556&rettype=fasta&retmode=text
conn2.request("POST", "/entrez/eutils/efetch.fcgi", params )
rf = conn2.getresponse()
if not rf.status == 200 :
    print "Error en la conexión: " + rf.status + " " + rf.reason 
    exit()
response_efetch = rf.read()

#data = urllib.urlopen("http://www.ncbi.nlm.nih.gov/nuccore/"+ident.text+"?report=fasta").read()
save_file = open("ejercicio_c.fasta", "w")
save_file.write(response_efetch)
save_file.close()
rf.close
conn2.close()
print "END"


