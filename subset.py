nums = [1,2,1]
lst = []
visited = [0] * (len(nums))
def subset(nums, index = 0, arr = []):
    if index > len(nums):
        return
    arr.sort()
    if arr not in lst:
        lst.append(arr)
    for i in range(index, len(nums)):
        if not visited[i]:
            visited[i] = 1
            subset(nums, index + 1, arr + [nums[i]])
            visited[i] = 0
subset(nums)
print(lst)
    