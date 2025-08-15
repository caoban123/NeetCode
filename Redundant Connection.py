edges = [[1,2],[1,3],[3,4],[2,4]]
n = len(edges)
visited = [0] * (n + 1)
adj = {i : [] for i in range(1, n + 1)}
for u, v in  edges:
    adj[u].append(v)
    adj[v].append(u)
parent = [-1] * (n + 1)
def dfs(u, par):
    visited[u] = 1
    for v in adj[u]:
        if not visited[v]:
            parent[v]= u
            res = dfs(v, u)
            if res:
                return res
        elif v != par:
            return v, u
    return None
res = dfs(1, -1)
if res:
    start, end = res 
lst = [[end, start]]
while start != end:
    lst.append([end,parent[end]])
    end= parent[end]
lst = [sorted(x) for x in lst]

for i in range(n - 1, -1, -1):
    if edges[i] in lst:
        return edges[i]
