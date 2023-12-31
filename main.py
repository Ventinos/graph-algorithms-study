import algorithms as algo
graph1 = [[1],[0,2],[1,3],[2,4],[3]]
graph2 = [[1],[0,1,4],[1],[4],[1,3,5],[4]]
graph3 = [[1],[2],[]]
graph4 = [[1],[2,3],[0],[4],[]]
graph5 = [[1,2],[0,2],[0,1],[4],[3,5],[4]]

edgeList = [(0,1,1),(0,2,1),(0,3,1),(0,4,1),(1,2,2),(2,4,2),(4,3,4),(1,3,5)]
edgeList2 = [(0,1,10),(1,2,10),(1,6,8),(1,7,13),(2,3,10),(2,7,8),(2,8,13),(3,4,10),(3,8,8),(5,6,10),(6,7,10),(7,8,10),(8,9,10)]
edgeList3 = [(0,1,9),(0,2,75),(1,2,95),(1,3,19),(1,4,42),(2,3,51),(3,4,31)]

dag1 = [[(1,2),(2,3),(3,4)],[(2,3),(3,4)],[(3,4)],[]]
maxFlowTest = [[(1,4)],[(2,7)],[(3,3)],[]]
visited = 5*[False]

print(graph1)
print(graph2)

print('\ndfs rec:')
algo.dfs(0,graph1,visited)

print('\ndfs nao rec:')
algo.dfs2(0,graph1)

print('\nbfs:')
algo.bfs(0,graph1)

print('\nhopcroft:')
print('articulacoes:')
print(algo.hopcroft(graph1))
print(algo.hopcroft(graph2))

print('\nkosaraju:')
print(algo.kosaraju(graph5))

print('\nMinST:')
print(algo.kruskal(edgeList3))
print('\nMaxST:')
print(algo.kruskalMAX(edgeList3))
print('\nK-MSF:')
print(algo.kmsf(edgeList3,4))

print('\nMin Distance:')
print('\nBFS:',end='')
print(algo.bfsMinDistance(graph1,0,3))
print('\nDAG:',end='')
print('\nWith Topologic Order',end='')
print(algo.DAGMinDist(dag1,0))
print('\nWithout Topologic Order',end='')
print(algo.DAGTest(dag1,0))
print('\nDjikstra:',end='')
print(algo.djikstraBST(dag1,0))

print('\nMaxFlow:',end='')
print(algo.fordFulkerson(maxFlowTest,0,3))
