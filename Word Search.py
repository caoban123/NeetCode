board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
visited = [[0] * len(board[0]) for _ in range(len(board))]
def find(board, word, i, j, k):
    if k == len(word):
        return True
    if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or
        visited[i][j] or board[i][j] != word[k]):
        return False
    
    visited[i][j] = 1
    for d in range(4):
        i0, j0 = i + dx[d], j + dy[d]
        if find(board, word, i0, j0, k + 1):
            return True
    visited[i][j] = 0
    return False
check = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]== word[0]:
            if find(board, word, i, j, 0):
                check = 1
                break
    if check:
        break
print(check)



