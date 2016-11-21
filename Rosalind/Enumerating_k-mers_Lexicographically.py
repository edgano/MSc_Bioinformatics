#-------------------------------------------------------------------------------
#--- Assume that an alphabet AA has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak)A=(a1,a2,…,ak), where a1<a2<⋯<aka1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z)(A,B,…,Z).
#--- Given two strings ss and tt having the same length nn, we say that ss precedes tt in the lexicographic order (and write s<Lexts<Lext) if the first symbol s[j]s[j] that doesn't match t[j]t[j] satisfies sj<tjsj<tj in AA.
#--- Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).
#--- Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically.
#--- Code written by: Edgar Garriga				edgargarriga.com
#-------------------------------------------------------------------------------
# we define the function, it will recive the string to codify
def alpha_combs(alphabet,n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


alphabet = ['P', 'W', 'O', 'S', 'Z', 'Q']
n=3
t= alpha_combs(alphabet,n)

for i in sorted(t):
	print i

