import string

mers=set()
edges=set()
nodes=set()
edict=dict()

with open("rosalind_long.txt","rU") as f:
    for line in f:
        mers.add(line.strip())
		
n=len(line.strip())                        
for x in mers:
    nodes.add(x[0:n-1])
    nodes.add(x[1:n])
    edges.add((x[0:n-1],x[1:n]))
    edict[x[0:n-1]]=x[1:n]

x=list(nodes)[0]
y=edict[x]
s=x
while y!=x:
    s=s+y[-1]
    y=edict[y]
    
print s[(n-2):]   
raw_input()