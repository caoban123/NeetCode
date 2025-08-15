height = [2,2,2]

l = 0
r = len(height) - 1

maxx = float("-inf")
while l < r:
    area = min(height[l], height[r]) * (r - l)
    maxx = max(area, maxx)
    if height[l] < height[r]:
        l += 1
    elif height[r] < height[l]:
        r -= 1
    else:
        l += 1
        r -= 1
print(maxx)