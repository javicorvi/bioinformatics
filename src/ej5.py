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

params = urllib.urlencode({'db': 'nuccore','term':'Junin+Virus[orgn]','retmax':1000})
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
print response
docXml = ET.fromstring(response)
for f in docXml.find("IdList").findall("Id") :
        print "ID {:15} ".format(f.text)
        params = urllib.urlencode({'db':'nuccore','retmode':'xml','id':f.text})
        conn2 = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
        conn2.request("POST", "/entrez/eutils/efetch.fcgi", params )
        rf = conn2.getresponse()
        if not rf.status == 200 :
            print "Error en la conexión: " + rf.status + " " + rf.reason 
            exit()
        response_efetch = rf.read()
        print response_efetch
        docXml_f = ET.fromstring(response_efetch) 
        pubMed = docXml_f.find("GBSeq/GBSeq_references/GBReference/GBReference_pubmed").text
        print pubMed
        params = urllib.urlencode({'db':'pubmed','rettype':'abstract','retmode':'txt','id':pubMed})
        conn3 = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
        conn3.request("POST", "/entrez/eutils/efetch.fcgi", params )
        rpub = conn3.getresponse()
        if not rpub.status == 200 :
            print "Error en la conexión: " + rpub.status + " " + rpub.reason 
            exit()
        response_pubmed = rpub.read()
        print response_pubmed
        
        rpub.close
        conn3.close()
        
        rf.close
        conn2.close()
save_file = open("my_junin_virus.xml", "w")
save_file.write(response)
save_file.close()
r1.close
# Cierra la conexion
conn.close()


#print docXml.find("Count").text
# Fin de la consulta
#print "{:15} {:45} {:10} ".format(docXml.find("eSearchResult/Count").text, docXml.find("eSearchResult/From").text, docXml.find("eSearchResult/To").text) 

