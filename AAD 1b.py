from collections import deque
def kahn_topological_sort(graph):

    indegree = {u: 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque(sorted([u for u in indegree if indegree[u] == 0]))
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
                queue = deque(sorted(queue))  

    return topo_order

def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in sorted(graph[u]):
            if v not in visited:
                dfs(v)
        stack.append(u)

    for u in sorted(graph):
        if u not in visited:
            dfs(u)

    return stack[::-1]

graph = {
    0:[1],
    1:[2],
    3:[],
    2:[3],
    4:[5],
    5:[1,2]
}

kahn_order = kahn_topological_sort(graph)
dfs_order = dfs_topological_sort(graph)

with open("topological_sort_results.txt", "w") as f:
    f.write("Topological Sort Results\n\n")
    f.write("Method A - Kahn's Algorithm (BFS-based):\n")
    f.write(" -> ".join(map(str, kahn_order)) + "\n\n")

    f.write("Method B - DFS-based Topological Sort:\n")
    f.write(" -> ".join(map(str, dfs_order)) + "\n")

print("Kahn's Algorithm Order:", kahn_order)
print("DFS-based Order:", dfs_order)