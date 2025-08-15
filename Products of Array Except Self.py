nums = [1,2,4,6]
prefix = [1] * (len(nums) + 1)
postfix = [1] * (len(nums) + 1)
for i in range(1, len(nums) + 1):
    prefix[i] = prefix[i - 1] * nums[i - 1]
for i in range(len(nums) - 1, -1, -1):
    postfix[i] = postfix[i + 1] * nums[i]

for i in range(len(nums)):
    nums[i] = prefix[i] * postfix[i + 1]
print(nums)
