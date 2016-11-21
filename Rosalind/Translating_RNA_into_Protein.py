#-------------------------------------------------------------------------------
#--- Write a Python function named decode() that decodes a RNA string into the protein it
#--- encodes(look at http://rosalind.info/problems/prot/ for help and for examples)
#--- Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#--- Return: The protein string encoded by s.
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
# we define the function, it will recive the string to codify
def decode( sequence ):
	# we define 3 as the lenght of the substring to "code". we define the 'solution' string (it will be returned at the end)
	n=3
	solution=""
	sequence.upper()
	# we split the original sequence in substring of lenght N (3). We will obtain a list of 3 characters in each position
	splitSeq=[sequence[i:i+n] for i in range(0, len(sequence), n)] #http://stackoverflow.com/questions/9475241/split-python-string-every-nth-character
	for i in range (0,len(splitSeq)):
		#print splitSeq[i]
		# we check if we have arrived to the end -> BREAK 
		if splitSeq[i] == "UAA" or splitSeq[i] == "UAG" or splitSeq[i] == "UGA": break
		# if the 2 first char are in this block we dont care of the 3rd
		elif splitSeq[i][:2] == "UC" : solution= solution + "S"
		elif splitSeq[i][:2] == "CU" : solution= solution + "L"
		elif splitSeq[i][:2] == "CC" : solution= solution + "P"
		elif splitSeq[i][:2] == "CG" : solution= solution + "R"
		elif splitSeq[i][:2] == "AC" : solution= solution + "T"
		elif splitSeq[i][:2] == "GU" : solution= solution + "V"
		elif splitSeq[i][:2] == "GC" : solution= solution + "A"
		elif splitSeq[i][:2] == "GG" : solution= solution + "G"
		
		#now, we just code following the RNA codon table (https://en.wikipedia.org/wiki/Genetic_code#RNA_codon_table)
		elif splitSeq[i] == "UUU" or splitSeq[i] == "UUC": solution= solution + "F"
		elif splitSeq[i] == "UUA" or splitSeq[i] == "UUG": solution= solution + "L"
		
		elif splitSeq[i] == "AUU" or splitSeq[i] == "AUC" or splitSeq[i] == "AUA": solution= solution + "I"
		elif splitSeq[i] == "AUG" : solution= solution + "M"
		
		elif splitSeq[i] == "UAU" or splitSeq[i] == "UAC": solution= solution + "Y"
		elif splitSeq[i] == "CAU" or splitSeq[i] == "CAC": solution= solution + "H"
		elif splitSeq[i] == "CAA" or splitSeq[i] == "CAG": solution= solution + "Q"
		elif splitSeq[i] == "AAU" or splitSeq[i] == "AAC": solution= solution + "N"
		elif splitSeq[i] == "AAA" or splitSeq[i] == "AAG": solution= solution + "K"
		elif splitSeq[i] == "GAU" or splitSeq[i] == "GAC": solution= solution + "D"
		elif splitSeq[i] == "GAA" or splitSeq[i] == "GAG": solution= solution + "E"
		
		elif splitSeq[i] == "UGU" or splitSeq[i] == "UGC": solution= solution + "C"
		elif splitSeq[i] == "UGG" : solution= solution + "W"
		elif splitSeq[i] == "AGU" or splitSeq[i] == "AGC": solution= solution + "S"
		elif splitSeq[i] == "AGA" or splitSeq[i] == "AGG": solution= solution + "R"
	#finally we send back the encode string	
	return solution	

#we define se sequence to codify	
sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA" 
#sent the seq to the codon table coding function
solution = decode(sequence)
#print the solution
print "Sequence: "+sequence
print "Solution: "+solution
