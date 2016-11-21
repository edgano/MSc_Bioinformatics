#-------------------------------------------------------------------------------
#---An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
#---Given a DNA string t corresponding to a coding
#---strand, its transcribed RNA string u is formed by replacing all occurrences of 'T'in t with 'U' in u.
#---Given: A DNA string t having length at most 1000 nt.
#---Return: The transcribed RNA string of t.
#--- 
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
def transcribeDNA (seq):
	seq.upper()     #convert seq to upperCase
	rna=""          #create empy string
	for x in seq:
                if x == 'T': x = "U"    #if T, replace for U
		rna = rna+x             #we add char by char to the solution
	return rna

s="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
rna=transcribeDNA(s)
print "Sequence DNA: "+s
print "Sequence RNA: "+rna
