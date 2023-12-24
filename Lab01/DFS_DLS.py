graph = {
  '0' : ['1','2','3'],
  '1' : ['4','5','6'],
  '2' : ['7'],
  '3' : ['8','9'],
  '4' : ['10','11'],
  '5' : ['12'],
  '6' : ['13','14'],
  '7' : ['15', '16'],
  '8' : ['17'],
  '9' : ['18','19','20'],
  '10' : [],
  '11' : [],
  '12' : [],
  '13' : [],
  '14' : [],
  '15' : [],
  '16' : [],
  '17' : [],
  '18' : [],
  '19' : [],
  '20' : []

}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '0')

#DLS

# Define a graph as an adjacency list
graph = {
  '0' : ['1','2','3'],
  '1' : ['4','5','6'],
  '2' : ['7'],
  '3' : ['8','9'],
  '4' : ['10','11'],
  '5' : ['12'],
  '6' : ['13','14'],
  '7' : ['15', '16'],
  '8' : ['17'],
  '9' : ['18','19','20'],
  '10' : [],
  '11' : [],
  '12' : [],
  '13' : [],
  '14' : [],
  '15' : [],
  '16' : [],
  '17' : [],
  '18' : [],
  '19' : [],
  '20' : []
}
