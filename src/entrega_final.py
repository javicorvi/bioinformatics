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

params = urllib.urlencode({'db': 'taxonomy','term':'Klebsiella pneumoniae [Orgn]','retmax':1000})
conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
conn.request("POST", "/entrez/eutils/esearch.fcgi", params)

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
#print response
docXml = ET.fromstring(response)
save_file = open("ejercicio_a.xml", "w")
for f in docXml.find("IdList").findall("Id") :
    print "ID {:15} ".format(f.text)
    params = urllib.urlencode({'db':'taxonomy','retmode':'xml','id':f.text})
    conn2 = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
    conn2.request("POST", "/entrez/eutils/efetch.fcgi", params )
    rf = conn2.getresponse()
    if not rf.status == 200 :
        print "Error en la conexión: " + rf.status + " " + rf.reason 
        exit()
    response_efetch = rf.read()
    docXml_f = ET.fromstring(response_efetch) 
    print response_efetch
    TaxId = docXml_f.find("Taxon/TaxId")
    Name = docXml_f.find("Taxon/ScientificName")
    save_file.write("TaxId {:15} ".format(TaxId.text))
    save_file.write("ScientificName {:15} ".format(Name.text))
    rf.close
    conn2.close()
save_file.close()
r1.close
conn.close()



#print docXml.find("Count").text
# Fin de la consulta
#print "{:15} {:45} {:10} ".format(docXml.find("eSearchResult/Count").text, docXml.find("eSearchResult/From").text, docXml.find("eSearchResult/To").text) 

