#-------------------------------------------------------------------------------
#--- Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#--- AA-AA
#--- AA-Aa
#--- AA-aa
#--- Aa-Aa
#--- Aa-aa
#--- aa-aa
#--- Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
# we define the function, it will recive the string to codify
def offspring(hdhd, hdht, hdhr, htht, hthr, hrhr):
	population = hdhd + hdht + hdhr + htht + hthr + hrhr
	freqdom = hdhd + hdht + hdhr + 0.75*htht + 0.5*hthr
	return freqdom*2

#Test
print offspring(17581, 16357, 16600, 16007, 16110, 16665)