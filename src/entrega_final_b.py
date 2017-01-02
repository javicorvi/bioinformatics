# imports
import urllib

#1352933
#Klebsiella pneumoniae LCT-KP289
print "INICIO"
data2 = urllib.urlopen("http://www.uniprot.org/uniprot/?query=1352933&format=fasta").read()
save_file2 = open("ejercicio_b.fasta", "w")
save_file2.write(data2)
save_file2.close()
print "FIN"