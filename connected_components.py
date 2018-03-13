#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    visited = [0] * len(adj)  # mark all vertices to unvisited
    for i in range(len(adj)): # for all vertices in the adjacent list
        if visited[i] == 0:
            explorer(i, adj, visited)
            result += 1
    return result

def explorer(i, adj, visited):
    visited[i] = 1
    for j in range(len(adj[i])):
        if not visited[adj[i][j]]:
            explorer(adj[i][j], adj, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = '4 4 1 2 3 2 4 3 1 4 1 4'
    # input = '4 2 1 2 3 2 1 4'
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
