import heapq

class GridNode:
    def __init__(self, x, y, obstacle=False):
        self.x = x
        self.y = y
        self.obstacle = obstacle
        self.parent = None
        self.g_cost = 0  # Cost from start node to current node
        self.heuristic = 0  # Greedy Best-First Search uses only the heuristic for prioritization

    def __lt__(self, other):
        # Compare nodes based on their heuristic values
        return self.heuristic < other.heuristic

def manhattan_distance(node, goal):
    # Calculate Manhattan distance heuristic
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def is_valid_move(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y].obstacle

def get_neighbors(grid, node):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        new_x, new_y = node.x + dx, node.y + dy
        if is_valid_move(grid, new_x, new_y):
            neighbors.append(grid[new_x][new_y])

    return neighbors

def greedy_best_first_search(grid, start, goal):
    open_set = [start]

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node == goal:
            # Goal reached, reconstruct the path
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        neighbors = get_neighbors(grid, current_node)
        for neighbor in neighbors:
            # Calculate the cost from start to neighbor
            tentative_g_cost = current_node.g_cost + 1

            if neighbor not in open_set:
                neighbor.parent = current_node
                neighbor.g_cost = tentative_g_cost
                neighbor.heuristic = manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, neighbor)

    return None  # No path found

def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print("P ", end="")
            elif grid[i][j].obstacle:
                print("# ", end="")
            else:
                print(". ", end="")
        print()

# Example usage:
if __name__ == "__main__":
    # Create a grid
    rows, cols = 5, 5
    grid = [[GridNode(i, j) for j in range(cols)] for i in range(rows)]

    # Set obstacles
    grid[1][2].obstacle = True
    grid[2][2].obstacle = True
    grid[3][2].obstacle = True

    # Define start and goal positions
    start_node = grid[0][0]
    goal_node = grid[4][4]

    # Find path using GBFS
    path = greedy_best_first_search(grid, start_node, goal_node)

    if path:
        print("Path found:")
        print_grid(grid, path)
    else:
        print("No path found.")
