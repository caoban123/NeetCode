import math
piles = [25,10,23,4]
h = 4

def finish(k):
    summ = 0
    for i in piles:
        summ += math.ceil(i / k)
    return summ <= h

l, r = 1, max(piles)

while l <= r:
    mid = (l + r) // 2
    if finish(mid):
        r = mid - 1
    else:
        l = mid + 1
print(l)