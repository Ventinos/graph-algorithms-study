import algorithms as algo
graph1 = [[1],[0,2],[1,3],[2,4],[3]]
graph2 = [[1],[0,1,4],[1],[4],[1,3,5],[4]]
graph3 = [[1],[2],[]]
graph4 = [[1],[2,3],[0],[4],[]]
graph5 = [[1,2],[0,2],[0,1],[4],[3,5],[4]]
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

print('\npontes:')
print(algo.hopcroftPontes(graph1))
print(algo.hopcroftPontes(graph2))

print('\nkosaraju:')
print(algo.kosaraju(graph5))

