# Basic:
# Recursive DFS:
def dfs(start, graph, visited):
    print(start)
    visited[start] = True
    for u in graph[start]:
        if not visited[u]:
            dfs(u, graph, visited)

# Non-recursive DFS:
# We use a stack to simulate the OS execution stack
def dfs2(start, graph):
    stack = []
    visited = len(graph) * [False]
    stack.append(start)
    visited[start] = True
    while stack:
        w = stack.pop(-1)
        print(w)
        for u in graph[w]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)

# DFS for edge list:
def dfsEdgeList(start, edgeList, visited):
    stack = []
    visited.add(start)
    stack.append(start)
    while stack:
        u = stack.pop()
        for edge in edgeList:
            if u in edge:
                v = edge[0] if u == edge[1] else edge[1]
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

# Non-recursive BFS:
# Same as non-recursive DFS, just change the stack to a queue
def bfs(start, graph):
    queue = []
    visited = len(graph) * [False]
    queue.append(start)
    visited[start] = True
    while queue:
        w = queue.pop(0)
        print(w)
        for u in graph[w]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

# Counting articulation points with simplified Hopcroft:
# This considers removed vertices and is not recursive
def dfs3(start, graph, visited, removed):
    stack = []
    stack.append(start)
    visited[start] = True
    while stack:
        w = stack.pop()
        for u in graph[w]:
            if not visited[u] and not removed[u]:
                visited[u] = True
                stack.append(u)

# This one counts the components:
def components(graph, removed):
    visited = len(graph) * [False]
    count = 0
    for i in range(0, len(graph)):
        if not visited[i] and not removed[i]:
            dfs3(i, graph, visited, removed)
            count += 1
    return count

"""This one counts the components before removing a vertex,
removes the vertex, and counts the components again. If this number increases, it means we found an articulation point in the graph:"""
def hopcroft(graph):
    removed = len(graph) * [False]
    count = components(graph, removed)
    c = 0
    for w in range(0, len(graph)):
        removed[w] = True
        newCount = components(graph, removed)
        removed[w] = False
        if newCount > count:
            c += 1
    return c

# Unfortunately, we can't count bridges like this; for that, we need the complete Hopcroft.

# Kosaraju and counting strongly connected components:
# After each iteration, push the value that was used:
def dfsPosOrder(start, graph, visited, stack):
    if not visited[start]:
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                dfsPosOrder(i, graph, visited, stack)
        stack.append(start)

# Mark the roots during DFS:
def dfsBase(start, graph, visited, root):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            root[i] = root[start]
            dfsBase(i, graph, visited, root)

# Create a transposed graph:
def transpose(graph):
    graphT = [[] for _ in range(len(graph))]
    for w in range(0, len(graph)):
        for i in graph[w]:
            graphT[i].append(w)
    return graphT

# Actual Kosaraju algorithm:
def kosaraju(graph):
    # Transpose the graph:
    graphT = transpose(graph)

    # Vectors that will be used:
    root = []
    visited = len(graphT) * [False]
    posOrder = []

    # Root tells which component the vertex belongs to:
    for i in range(len(graph)):
        root.append(i)
    # Initially, all vertices belong to their own components;

    # Arrange the stack in post-order of graphT using DFS:
    for i in range(len(graph)):
        dfsPosOrder(i, graph, visited, posOrder)

    # Pop the post-order stack and perform DFS on the items:
    visited = len(graph) * [False]
    while posOrder:
        i = posOrder.pop()
        # This DFS saves in root from whom the vertex was accessed:
        dfsBase(i, graph, visited, root)

    # Return the count of different values in root:
    return len(set(root))

# Kruskal and generation of MSTs:
def getRoot(ufds, i):
    if ufds[i] == i:
        return i
    i = getRoot(ufds, ufds[i])
    return i

def isConnected(ufds, i, j):
    u = getRoot(ufds, i)
    v = getRoot(ufds, j)
    return u == v

def kruskal(edgeList):
    # Sort the edge list by weight in ascending and stable order:
    edgeList = sorted(edgeList, key=lambda x: x[2])
    mst = []

    # Initialize the UFDS:
    ufds = []
    for i in range(len(edgeList)):
        ufds.append(i)

    # For every edge in the graph, if it doesn't form a cycle, add it to the MST and update the UFDS:
    for w in edgeList:
        u = getRoot(ufds, w[0])
        v = getRoot(ufds, w[1])
        if u != v:
            mst.append(w)
            ufds[u] = v
    return mst

# Maximum spanning tree:
def kruskalMAX(edgeList):
    # Sort the edge list by weight in ascending and stable order:
    edgeList = sorted(edgeList, key=lambda x: x[2])
    # Literally just added this line to sort in descending order:
    edgeList.reverse()
    mst = []

    # Initialize the UFDS:
    ufds = []
    for i in range(len(edgeList)):
        ufds.append(i)

    # For every edge in the graph, if it doesn't form a cycle, add it to the MST and update the UFDS:
    for w in edgeList:
        u = getRoot(ufds, w[0])
        v = getRoot(ufds, w[1])
        if u != v:
            mst.append(w)
            ufds[u] = v
    return mst

# WIP! The print is pretty bad, and there's stuff to fix
# Minimum Spanning Forest with k components:
def componentsMSF(msf):
    visited = set()
    count = 0
    for edge in msf:
        for u in edge:
            if u not in visited:
                dfsEdgeList(u, msf, visited)
                count += 1

    return count

def kmsf(edgeList,k):
    # Sort the edge list by weight in ascending and stable order:
    edgeList=sorted(edgeList,key=lambda x:x[2])
    msf=[]

    # Initialize the UFDS:
    ufds = []
    for i in range(len(edgeList)):
        ufds.append(i)

    # For every edge in the graph, if it doesn't form a cycle, add it to the MST and update the UFDS:
    for w in edgeList:
        u=getRoot(ufds,w[0])
        v=getRoot(ufds,w[1])
        if u != v:
            msf.append(w)
            ufds[u]=v
            comp=componentsMSF(msf)
            if comp == k:
                break
    return msf

#Minimum distance:
#Min distance with bfs:
#if this return -1, it means that end is unreachable from start;
def bfsMinDistance(graph,startV,endV):
    #initializing arrays:
    distance = [-1]*len(graph)
    visited = [False]*len(graph)
    queue = [startV]
    visited[startV]=True
    distance[startV]=0
    while queue:
        w=queue.pop(0)
        for u in graph[w]:
            if not visited[u]:
                visited[u]=True
                queue.append(u)
                distance[u]=distance[w]+1
    #return minimum distance from start to end:
    return distance[endV]

#Min Distance for DAG's (Directed Acyclic Graph) pondered:
#we use a topologic ordenation of the vertices in this one, so
def topologicOrd(graph):
    visited=[False]*len(graph)
    topOrd=[]
    for i in range(len(graph)):
        visited[i]=True
        queue=[i]
        if i not in topOrd:
            topOrd.append(i)
        while queue:
            w=queue.pop(0)
            for (v,p) in graph[w]:
                if not visited[v]:
                    queue.append(v)
                    topOrd.append(v)
                    visited[v]=True
    return topOrd

def DAGMinDist(graph,startV):
    dist = [999999]*len(graph)
    ordTop = topologicOrd(graph)
    dist[startV] = 0
    for u in ordTop:
        for (v,p) in graph[u]:
            dist[v] = dist[u]+p if dist[u]+p < dist[v] else dist[v]
    return dist

#Without the topologic order
def DAGTest(graph,start):
    dist = [99999]*len(graph)
    dist[start] = 0
    for u in range(len(graph)):
        for (v,p) in graph[u]:
            dist[v]=dist[u]+p if dist[u]+p < dist[v] else dist[v]
    return dist
#Djikstra implemented using a BST:
def djikstraBST(graph,startV):
    dist = [999999]*len(graph)
    dist[startV] = 0
    pq = set(())
    
    for i in range(len(graph)):
        pq.add((i,dist[i]))

    while pq:
        (u,dista)=pq.pop()
        for (v,p) in graph[u]:
            if dista+p <= dist[v]: 
                pq.discard((v,dist[v]))
                dist[v]=dista+p
                pq.add((v,dist[v]))
    return dist

#Matching algorithms:
#We're gonna use ford-fulkerson:
def residual(graph):
    gr = [[] for _ in range(len(graph))]
    
    for i in range(len(graph)):
        for (u,p) in graph[i]:
            gr[i].append((u,p,False))
            
    for v in range(len(gr)):
        for (u,_,_) in gr[v]:
            gr[u].append((v,0,True))
    
    return gr

#we're gonna use BFS to find the path from start to end:
def bfsPath(graph,start,end):
    #Normal BFS:
    queue = [start]
    visited = [False] * len(graph)
    visited[start] = True 
    #We're gonna use this for the path
    path = [None] * len(graph)
    minWeight = 999999
    #starting bfs:
    while queue:
        w = queue.pop(0)
        for (u,p,_) in graph[w]:
            if not visited[u] and p>0:
                visited[u] = True
                queue.append(u)
                path[u] = (w,p)
   
    #getting the shortest path
    shortestPath = []
    if path[end] is not None:
        curr = end
        while curr != start:
            (v,p) = path[curr]
            minWeight = p if p<minWeight else minWeight
            shortestPath.insert(0,(curr,p))
            curr = v
        shortestPath.insert(0,(start,0))
    return shortestPath, minWeight

def fordFulkerson(graph,start,end):
    gr = residual(graph)
    fmax=0
    oldPath=[]
    while True:
        path, f = bfsPath(gr, start, end)
        #if the path hasn't change we have the max flow
        if oldPath==path: break
        for i in gr:
            for v in i:
                weight = v[1]
                weight+= f if v[2] else -f
                v = (v[0],weight,v[2])
        fmax+=f
        oldPath = path
    return fmax          
        
        
    




