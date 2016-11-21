def profile(matrix):
    strings = matrix.split()

    default = [0] * len(strings[0])
    results = {
        'A': default[:],
        'C': default[:],
        'G': default[:],
        'T': default[:],
    }

    for s in strings:
        for i, c in enumerate(s):
            results[c][i] += 1

    return results


def consensus(profile):
    result = []

    keys = profile.keys()

    for i in range(len(profile[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = profile[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        result.append(max_k)

    return ''.join(result)
    
small_dataset = """
    ATCCAGCT
    GGGCAACT
    ATGGATCT
    AAGCAACC
    TTGGAACT
    ATGCCATT
    ATGGCACT
    """

p = profile(small_dataset)
c = consensus(p)

print c
for k in sorted(p.iterkeys()):
	print "%s: %s" % (k, ' '.join(map(str, p[k])))