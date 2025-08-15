heights = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
lst = []
def bfs(starts):
    queue = starts
    visited = [[0] * len(heights[0]) for _ in range(len(heights))]
    for x, y in starts:
        visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and heights[nx][ny] >= heights[x][y] and not visited[nx][ny] :
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return visited

pacific = []
atlantic = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if i == 0 or j == 0:
            pacific.append((i, j))
        if i == len(heights) - 1 or j == len(heights[0]) - 1:
            atlantic.append((i, j))
v1 = bfs(pacific)
v2 = bfs(atlantic)
result = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if v1[i][j] and v2[i][j]:
            result.append([i, j])
print(result)
