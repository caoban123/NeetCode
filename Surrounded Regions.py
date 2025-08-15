board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

n, m = len(board), len(board[0])
visited = [[0] * m for _ in range(n)]
lst = []
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def bfs(i, j):
    queue = [(i, j)]
    check = False
    coor = []
    while queue:
        x, y = queue.pop(0)
        coor.append((x, y))
        visited[x][y] = 1
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            check = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "O" and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    if not check:
        lst.extend(coor)

for i in range(n):
    for j in range(m):
        if board[i][j] == "O" and not visited[i][j]:
            bfs(i, j)
for coor in lst:
    i, j = coor
    board[i][j] = "X"
print(board)



    