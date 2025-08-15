candidates = [9,2,2,4,6,1,5]
target = 8
lst = []
visited = [0] * len(candidates)
def combination(nums, target, index = 0, arr = []):
    if sum(arr) == target:
        if arr not in lst:
            lst.append(arr[:])
        return
    if index >= len(nums) or sum(arr) > target:
        return 
    for i in range(index, len(candidates)):
        if not visited[i]:
            visited[i] = 1
            arr.append(candidates[i])
            combination(candidates, target, i + 1, arr)
            arr.pop()
            visited[i] = 0
combination(candidates, target)
print(lst)
