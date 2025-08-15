grid=[[2,1,1],[1,1,1],[0,1,2]]
# grid = [[1,1,0],[0,1,1],[0,1,2]]
dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)
visited = [[0] * len(grid[0]) for _ in range(len(grid))]
answer = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

def bfs(i, j):
    queue = [(i, j, 0)]
    while queue:
        x0, y0, cnt = queue.pop(0)
        cnt += 1
        visited[x0][y0] = 1
        for s in range(4):
            x1, y1 = x0 + dx[s], y0 + dy[s]
            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] == 1 and not visited[x1][y1]:
                visited[x1][y1] = 1
                answer[x1][y1].append(cnt)
                queue.append((x1, y1, cnt))
cnt = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            cnt += 1
            bfs(i, j)
            visited = [[0] * len(grid[0]) for _ in range(len(grid))]
if cnt == 1:
    print(max(val for row in answer for cell in row for val in cell))
else:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            answer[i][j] = tuple(set(answer[i][j]))
            if len(answer[i][j]) == 1:
                print(answer[i][j][0])
        
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 1 and not visited[i][j]: 
# [[[], [], []], 
#  [[], [], []], 
#  [[], [], []]]



            
