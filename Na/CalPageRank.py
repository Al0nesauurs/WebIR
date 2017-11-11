import numpy as np
from scipy.sparse import csc_matrix

def pageRank(G, s = .85, maxerr = .001):

    n = G.shape[0]

    # transform G into markov matrix M
    M = csc_matrix(G,dtype=np.float)
    rsums = np.array(M.sum(1))[:,0]
    ri, ci = M.nonzero()
    M.data /= rsums[ri]

    # bool array of sink states
    sink = rsums==0

    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in xrange(0,n):
            # inlinks of state i
            Ii = np.array(M[:,i].todense())[:,0]
            # account for sink states
            Si = sink / float(n)
            # account for teleportation to state i
            Ti = np.ones(n) / float(n)

            r[i] = ro.dot( Ii*s + Si*s + Ti*(1-s) )
    # return normalized pagerank
    return r/sum(r)

with open('456.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
w, h = 10218, 10218
Mat = [[0 for x in range(w)] for y in range(h)] 

data = [[int(n) for n in line.split()] for line in content]
for i in range (len(data)):
    for j in range (len(data[i])) :
        if data[i][j] != -1:
            Mat[i][data[i][j]-1] = 1
G = np.array(Mat)
with open('pagerank.txt') as pl:
    np.savetxt(pl,pageRank(G,s=.85) , newline="\n")




