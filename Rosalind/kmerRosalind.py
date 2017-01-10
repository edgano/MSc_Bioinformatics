from itertools import product


def parse_fasta(fasta):
    results = []
    strings = fasta.strip().split('>')

    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append((k, v))

    return results


def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]


def kmer_composition(s, k):
    kmers = {}
    
    for kmer in possible_kmers(k):
        kmers[kmer] = 0

    for i in range(len(s) - (k - 1)):
        kmer = s[i:i+k]
        kmers[kmer] += 1

    return kmers


def result(s):
    fastas = parse_fasta(s)
    k_comp = kmer_composition(fastas[0][1], 4)

    result = []
    for kmer in sorted(k_comp.iterkeys()):
        result.append(k_comp[kmer])
        
    return result


small_dataset = """
  >Rosalind_6431
  CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
  CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
  TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
  AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
  GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
  CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
  CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
  """
#large_dataset = open('datasets/rosalind_kmer.txt').read().strip()
print ' '.join(map(str, result(small_dataset)))
    
    
    