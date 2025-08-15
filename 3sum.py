nums = [-1,0,1,2,-1,-4]
lst = []
nums.sort()
for i in range(len(nums) - 2):
    l = i + 1
    r = len(nums) - 1
    while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total > 0:
            r -= 1
        elif total < 0:
            l += 1
        else:
            if [nums[i], nums[l], nums[r]] not in lst:
                lst.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
print(lst)


    