#Uses python3

import sys


def acyclic(adj):
    visited = [0] * len(adj)
    rec_stack = [0] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(i, adj, visited, rec_stack):
                return 1
    return 0

def dfs(x, adj, visited, rec_stack):
    visited[x] = 1
    rec_stack[x] = 1
    for y in range(len(adj[x])):
        if not visited[adj[x][y]] and dfs(adj[x][y], adj, visited, rec_stack):
            return 1
        elif rec_stack[adj[x][y]]:
            return 1
    rec_stack[x] = 0
    return 0

if __name__ == '__main__':
    # input = sys.stdin.read()
    input = '5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5'
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
