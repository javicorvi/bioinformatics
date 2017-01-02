from Bio.Blast import NCBIWWW
fasta_string = open("virus.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
#result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
save_file = open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
