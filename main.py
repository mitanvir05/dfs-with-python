graph = {
  '5' : ['23','27'],
  '23' : ['22', '24'],
  '27' : ['28'],
  '22' : [],
  '24' : ['28'],
  '28' : []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')