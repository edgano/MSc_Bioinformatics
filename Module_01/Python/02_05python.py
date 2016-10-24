#-------------------------------------------------------------------------------
#---The GC‐content of a DNA string is given by the percentage of symbols in the 
#---string that are 'C' or 'G'. For example, the GC‐content of "AGCTATAG" is 37.5%. DNA 
#---strings must be labeled when they are consolidated into a database. A commonly used 
#---method of string labeling is called FASTA format. In this format, the string is introduced 
#---by a line that begins with '>', followed by some labeling information. Subsequent lines 
#---contain the string itself; the first line to begin with '>' indicates the label of the next string.
#---Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#---Return: The ID of the string having the highest GC‐content, followed by the GC‐content 
#---of that string (a default error of 0.001)
#--- Compiled >> https://repl.it/languages/python
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
from __future__ import division

# we define the function, it will recive the string to codify
def gcConcentration( sequence ):
	max=0.0
	seqSplit = sequence.split('\n')
	for i in range (0,len(seqSplit)):
		#we take one DNA seq each iteration
		start = seqSplit[i].index('>')
		#Save the name
		name = seqSplit[i].split(' ')[0].replace(">", "")
		#save the actual seq
		seq = seqSplit[i].split(' ')[1]

		#count C appareance
		valueC=seq.count('C')
		#count G appareance
		valueG=seq.count('G')
		#add G's & C's repetitions
		valueGC = (valueC + valueG)
		#calc the concentration of G's&C's
		concentrationGC = valueGC / (len(seq))
		#We can delete the # to check the value for each sequence
		#print "Name {} concentration {}".format(name,concentrationGC)
		if concentrationGC > max : 
			max=concentrationGC
			valor = name +" "+str(concentrationGC)
	return valor 

sequence = ">Rosalind_0808 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT\n>Rosalind_0801 CCACCCTCGGGGGGGGGGGAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT\n>Rosalind_0802 CCACCCTCGTGGTATGGCTAGGCACCCCCGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT\n>Rosalind_0804 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACACACACACACACACACCTGCGGGCAGTAGGTGGAAT"
print "The sequence with the highest GC Concentration is: "+gcConcentration(sequence)
#----- CANT make it work ------------
#with open('dna.txt') as fp:
#    for line in fp:
#        print line
#        print gcConcentration(line)
#    raw_input("Press Enter to terminate."
