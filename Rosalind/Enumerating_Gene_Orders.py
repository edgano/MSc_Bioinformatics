#-------------------------------------------------------------------------------
#--- A permutation of length nn is an ordering of the positive integers {1,2,…,n}{1,2,…,n}. For example, π=(5,3,2,1,4)π=(5,3,2,1,4) is a permutation of length 55.
#--- Given: A positive integer  n≤7
#--- Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
# we define the function, it will recive the string to codify
from itertools import permutations
from math import factorial
n = 7
seq = range(1, n+1)

# how many possible combinations
print (factorial(n))

# evaluate all permutations
for perm in permutations(seq):
    print (" ".join(map(str, perm)))

