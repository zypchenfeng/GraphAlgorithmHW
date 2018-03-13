#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    result = 0
    visited = [0] * len(adj)
    for i in range(len(adj)):
        if visited[x] == 0 and visited[y] == 0:
            explore(x, adj, visited)
            if visited[x] == 1 and visited[y] == 1:
                result = 1
    return result

def explore(x, adj, visited):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            explore(adj[x][i], adj, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = '4 4 1 2 3 2 4 3 1 4 1 4'
    # input = '4 2 1 2 3 2 1 4'
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1     # the index for start and end vertices
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
