nums = [3,2,3]
target = 7

i = 0
j = len(nums) - 1
while True:
    summ = nums[i] + nums[j]
    if summ > target:
        j -= 1
    elif summ < target:
        i += 1
    else:
        print(i, j)
        break