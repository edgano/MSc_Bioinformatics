#-------------------------------------------------------------------------------
#---An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
#---Given a DNA string t corresponding to a coding
#---strand, its transcribed RNA string u is formed by replacing all occurrences of 'T'in t with 'U' in u.
#---Given: A DNA string t having length at most 1000 nt.
#---Return: The transcribed RNA string of t.
#--- 
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
def reverseSeq (seq):
	return (seq[::-1])	#reverse String

def DNAtoRNA(seq):
	rna=""          	#create empy string
	for x in seq:		#replace whatever we want
        	if x == 'A': x = "T" 
        	elif x == 'T': x = "A"
        	elif x == 'C': x = "G"
        	elif x == 'G': x = "C"
		rna = rna+x		#adding the chars at the end
	return rna
	
s="GTCAGGATATGCGATCAATGCCGTGGCCAACATAGTTACCAGCTGCCGGGTCACAGCACTAGGGTGGTGCTGAATATCCGGCGCCGTGGGTCCATGTACCGCGCTATAATCATGAAAAAGACTCTTGAAATGTTTAGCGGCCCTTAACTGGGGCCCAGCAAATGAGCTAGCATTTGGTTCACCAGCAACTTTCGCAAGTCGAGAATAACAAATATTGTAGACTACTGTAATTCGCTAGTATCCGTCTAGCTGTGAAGTTATGTGACTTAGAATTTGGCACGTAGATGGCTCTTCTGTCACATCTGATGCGCAGCTCCCTTAAAAGCGATACCCGGAATAAATCGTACGAGCACCCCAGTTTGTGGACAGCGAATTTTGAGGCTGACGAAATGCCATTCAAGTCGACCTCACGGAGAAGTCCTATGGGTATGCAGTACACCTAACTGTACCTACGTTCGTGCTACGTGCCGGGCCTCAATAAACATATTGGAGGGGCAGTGATATATCCTGATGCCGGCATCGCCCGCATATAGGTGTTCCGTGTGGTAGGACGCGCAACATATATGATCTTATTAGTTACGTTGATAAGGTCACCAACACACGCTCCGTGAACTCCCCTGGGCCATTGTACCTTCTGTCGAAAGGACCTGGTTCGGAGGACGTCATGAGCTTCTACCGTCACGCGGCCATGAGTAAACTTTCGCTAACCATGGCCGCCTATGTGCTCGCGCTCACATAGAATATTGAAGTTGGGAGTCGGCCCAAAAATACAGTACAATATTCAACTTGTCCTTCAGGTCG"
rna=DNAtoRNA(reverseSeq(s))
print "Sequence DNA: "+s
print "Sequence RNA: "+rna