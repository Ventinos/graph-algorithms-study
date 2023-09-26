#basico:
def dfs(start,graph,visited):
    print(start)
    visited[start]=True
    for u in graph[start]:
        if not visited[u]:
            dfs(u,graph,visited)

def dfs2(start, graph):
    stack = []
    visited = len(graph)*[False]
    stack.append(start)
    visited[start]=True
    while stack:
        w=stack.pop(-1)
        print(w)
        for u in graph[w]:
            if not visited[u]:
                visited[u]=True
                stack.append(u)

def bfs(start, graph):
    queue = []
    visited = len(graph)*[False]
    queue.append(start)
    visited[start]=True
    while queue:
        w=queue.pop(0)
        print(w)
        for u in graph[w]:
            if not visited[u]:
                visited[u]=True
                queue.append(u)

#contando articulacoes e pontes com hopcroft:
def dfs3(start, graph,visited,removed):
    stack = []
    stack.append(start)
    visited[start]=True
    while stack:
        w=stack.pop()
        for u in graph[w]:
            if not visited[u] and not removed[u]:
                visited[u]=True
                stack.append(u)
    return visited

def components(graph,removed):
    visited = len(graph)*[False]
    count = 0
    i=0
    for i in range(0,len(graph)):
        if not visited[i] and not removed[i]:
            visited=dfs3(i,graph,visited,removed)
            count+=1
    return count

def hopcroft(graph):
    removed = len(graph)*[False]
    count =  components(graph,removed)
    c=0
    for w in range(0,len(graph)):
        removed[w]=True
        newCount=components(graph,removed)
        removed[w]=False
        if newCount>count:
            c+=1
    return c

#errado ainda:
def hopcroftPontes(graph):
    removed = len(graph)*[False]
    count =  components(graph,removed)
    c=0
    for w in range(0,len(graph)):
        removed[w]=True
        newCount=components(graph,removed)
        removed[w]=False
        if newCount>=count:
            c+=1
    return c

#kosaraju:
#dps de cada iteracao empilha o valor que foi usado:
def dfsPosOrder(start,graph,visited,stack):
    if not visited[start]:
        visited[start]=True
        for i in graph[start]:
            if not visited[i]:
                dfsPosOrder(i, graph, visited,stack)
        stack.append(start)

#marca os roots:
def dfsBase(start, graph,visited,root):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            root[i]=root[start]
            dfsBase(i,graph,visited,root)

#faz grafo transposto:
def transpose(graph):
    graphT=[[]for _ in range(len(graph))]
    for w in range(0,len(graph)):
        for i in graph[w]:
            graphT[i].append(w)
    return graphT

#kosaraju de fato:
def kosaraju(graph):
    #transpose graph:
    graphT=transpose(graph)

    #vetores que serao usados:
    root=[]
    visited = len(graphT)*[False]
    posOrder=[]

    #root diz a que componente o vertice pertence:
    for i in range(len(graph)):
        root.append(i)
    #no inicio todos os vertices pertencem às proprias componentes;

    #arruma pilha em posOrdem do graphT com dfs:
    for i in range(len(graph)):
        dfsPosOrder(i,graph,visited,posOrder)

    #desempilha a pilha de posOrdem e faz dfs nos itens:
    visited = len(graph)*[False]
    while posOrder:
        i=posOrder.pop()
        #esse dfs aqui salva no root a partir de quem o vertice foi acessado:
        dfsBase(i,graph,visited,root)

    #retorna a quantidade de valores diferentes no root:
    return len(set(root))




