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
conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
# Hace la consulta
conn.request("GET", "/entrez/eutils/einfo.fcgi")
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
# Fin de la consulta

# Convierte el contenido en un documento XML y Busca los nodos DbName
for e in docXml.find("DbList").findall("DbName") :

    # Extrae el ID de la base de datos
    dbId = e.text

    # Hace una nueva consulta para buscar los datos espec�ficos de esa base de
    # datos
    params = urllib.urlencode({'db': dbId})
    conn = httplib.HTTPSConnection("eutils.ncbi.nlm.nih.gov")
    conn.request("POST", "/entrez/eutils/einfo.fcgi/", params )
    r1 = conn.getresponse()
    # Verifica que la respuesta es correcta
    if not r1.status == 200 :
        print "Error en la conexión: " + str(r1.status) + " " + r1.reason 
        exit()
    response = r1.read()
    conn.close()
    # Fin de la consulta
    
    # Convierte la respuesta en un documento XML
    dbDocXml = ET.fromstring(response)

    # Estrae los datos requeridos
    name = dbDocXml.find("DbInfo/DbName").text
    count = dbDocXml.find("DbInfo/Count").text
    desc = dbDocXml.find("DbInfo/Description").text
    lastUpdate = dbDocXml.find("DbInfo/LastUpdate").text
    dbBuild = dbDocXml.find("DbInfo/DbBuild").text
    # Imprime los datos formateados a stdout.
    print "{:15} {:45} {:10} {:20} {:20}".format(name, desc, count, lastUpdate, dbBuild)
    
    for f in dbDocXml.find("DbInfo/FieldList").findall("Field") :
        fieldName = f.find("Name").text
        print "{:15} ".format(fieldName)
        
# ---------------------------------------------------------------------------- #
