
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

# Recursive implementation of DLS
def dls(graph, node, goal, depth, current_depth):
    if current_depth == depth:
        return False  # Reached the depth limit without finding the goal

    if node == goal:
        return True  # Goal node found

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth, current_depth + 1):
            return True  # Goal found in a deeper level

    return False  # Goal not found within the specified depth

# Create a function to perform DLS with a specified depth limit
def depth_limited_search(graph, start, goal, depth_limit):
    return dls(graph, start, goal, depth_limit, 0)

# Perform DLS with a depth limit of 3
start_node = '0'
goal_node = '5'
depth_limit = 3

if depth_limited_search(graph, start_node, goal_node, depth_limit):
    print(f"Goal '{goal_node}' found within depth limit.")
else:
    print(f"Goal '{goal_node}' not found within depth limit.")

def depth_limited_search(node, goal, depth_limit):
    if node == goal:
        return True
    if depth_limit <= 0:
        return False

    # Generate child nodes if the function returns a valid iterable
    children = generate_children(node)
    if children is not None:
        for child in children:
            if depth_limited_search(child, goal, depth_limit - 1):
                return True
    return False

def iterative_deepening_search(root, goal):
    depth_limit = 0
    while True:
        if depth_limited_search(root, goal, depth_limit):
            return True, depth_limit
        depth_limit += 1

# Replace this function with your actual problem-specific function to generate children.
def generate_children(node):
    # Implement your logic to generate child nodes from the current node here.
    return []  # Return an empty list in case of no children (not None)

# Usage example
if __name__ == '__main__':
    root_node = 'A'  # Replace with your initial state
    goal_node = 'G'  # Replace with your goal state
    found, depth = iterative_deepening_search(root_node, goal_node)

    if found:
        print(f"Goal found at depth {depth}")
    else:
        print("Goal not found")
