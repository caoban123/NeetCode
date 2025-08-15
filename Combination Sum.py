nums = [2,5,6,9] 
target = 9
lst = []
def combination(nums, target, index = 0, arr = []):
    if sum(arr) == target:
        lst.append(arr[:])
        return
    if sum(arr) > target or index >= len(nums):
        return 
    combination(nums, target, index , arr + [nums[index]])
    combination(nums, target, index + 1, arr)

combination(nums, target)
print(lst)