#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [10**6 + 1] * len(adj)  # initialize all vertices distance to infinity
    prev = [None] * len(adj)
    dist[0] = 0
    H = []
    H.append([dist[0], 0])
    for _ in range(len(adj)):   # finish |V| interations of BellmanFord search
        [d, u] = H.pop()
        for j in range(len(adj[u])):
            if dist[adj[u][j]] > d + cost[u][j]:
                dist[adj[u][j]] = d + cost[u][j]
                prev[adj[u][j]] = u
                H.append([dist[adj[u][j]], adj[u][j]])
        H.sort(reverse = True)
    [d, u] = H.pop()
    A = []
    for j in range(len(adj[u])):
        if dist[adj[u][j]] > d + cost[u][j]:
            dist[adj[u][j]] = d + cost[u][j]
            prev[adj[u][j]] = u
            A.append([dist[adj[u][j]], adj[u][j]])
    verts = []

    while len(A) > 0:
        [_, s] = A.pop()
        [_, temp] = BFS(adj, s)
        verts.append(temp)
    print('All the nodes in the negative are ', verts)
    if len(verts) > 0:
        return 1
    return 0

def BFS(adj, s):
    dist = [10**6 + 1]*len(adj)
    prev2 = [None]*len(adj)
    dist[s] = 0
    Q = [s]
    while len(Q) > 0:
        u = Q.pop(0)
        for i in range(len(adj[u])):
            if dist[adj[u][i]] != 10**6 + 1:
                Q.append(adj[u][i])
                dist[adj[u][i]] = dist[adj[u]] + 1
                prev2[adj[u][i]] = u
    return dist, prev2



if __name__ == '__main__':
    # input = sys.stdin.read()
    input = '4 4 1 2 -5 4 1 2 2 3 2 3 1 1'
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
