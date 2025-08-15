grid = [
  [2147483647,-1        ,0         ,2147483647], 
  [2147483647,2147483647,2147483647,-1        ],
  [2147483647,-1        ,2147483647,-1        ],
  [0         ,-1        ,2147483647,2147483647]
]
dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)
visited = [[0] * len(grid[0]) for _ in range(len(grid))]
def bfs(i, j, cnt):
    queue = [(i, j, cnt)]
    while queue:
        x0, y0, cnt = queue.pop(0)
        visited[x0][y0] = 1
        cnt += 1
        for s in range(4):
            x1, y1 = x0 + dx[s], y0 + dy[s]
            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] != -1 and not visited[x1][y1]:
                if grid[x1][y1] == 0:
                    grid[i][j] = cnt
                    return
                else:
                    queue.append((x1, y1, cnt))
        

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != -1 and grid[i][j] != 0 and not visited[i][j]:
            bfs(i, j, 0)
            visited = [[0] * len(grid[0]) for _ in range(len(grid))]

print(grid)
            
