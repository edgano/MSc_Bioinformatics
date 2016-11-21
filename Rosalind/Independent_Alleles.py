#-------------------------------------------------------------------------------
#--- Given: Two positive integers kk (k≤7k≤7) and NN (N≤2kN≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
#--- Return: The probability that at least NN Aa Bb organisms will belong to the kk-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
# we define the function, it will recive the string to codify
import math

def prob_het(k,N):
    prob_AaBb = 4/16.0
    prob = []
    total = 2**k
    # summation of your general binomial probability function
    for r in xrange(N,(total+1)):
        prob.append(nCr(total,r)*(prob_AaBb**r)*((1-prob_AaBb)**(total-r)))
    return sum(prob)

# quick combinatorial function
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    
k=5
N=7

print prob_het(k,N)