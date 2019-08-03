import queue as Q

"""
Function implements BFS algorithm to explore the graph.
Additionaly, shortest distance between starting node and current node is found ad stored at respective location in dictionary.
"""
def BFS(G, s):
    key = list(G.keys())
    n = len(key)
    q = Q.Queue(maxsize = n)
    q.put(s)
    G[s]['distance'] = 0
    G[s]['isVisited'] = True
    
    while(not q.empty()):
        v = q.get()
        for w in G[v]['edges']:
            if(not G[w]['isVisited']):
                G[w]['isVisited'] = True
                q.put(w)
                G[w]['distance'] = G[v]['distance'] + 1
    
    return G[key[n-1]]['distance']
