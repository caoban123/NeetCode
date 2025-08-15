matrix = [[1,2,4,8],
          [10,11,12,13],
          [14,20,30,40]]
target = 2

ROW, COL = len(matrix), len(matrix[0])
top, bot = 0, ROW - 1
check = 0
while top <= bot:
    mid = (top + bot) // 2
    if target > matrix[mid][-1]:
        top = mid + 1
    elif target < matrix[mid][0]:
        bot = mid - 1
    else:
        break
print(top, bot)
if not top <= bot:
    check = 0
l, r = 0, COL - 1
row = (top + bot) // 2
while l <= r:
    mid = (l + r) // 2
    if target > matrix[row][mid]:
        l = mid + 1
    elif target < matrix[row][mid]:
        r = mid - 1
    else:
        check = 1
        break
if check:
    print("YES")
else:
    print("False")
    
    