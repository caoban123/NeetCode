n = 1

chess = [[0] * (n + 1) for _ in range(n + 1)]
d1 = [0] * (n * 2)
d2 = [0] * (n * 2)
cot = [0] * (n + 1)
type = ["." * n for _ in range(n + 1)]

for i in range(1, n + 1):
    type[i] = type[i][:i - 1] + "Q" + type[i][i :]


lst = []
answer = []
def Try(i):
    for j in range(1, n + 1):
        if not d1[i - j + n] and not d2[i + j - 1] and not cot[j]:
            d1[i - j + n] = d2[i + j - 1] = cot[j] = 1
            lst.append(type[j])
            if i == n:
                answer.append(lst[:])
            else:
                Try(i + 1)
            cot[j] = d1[i - j + n] = d2[i + j - 1] = 0
            lst.pop()
Try(1)
for i in answer:
    print(i)


            


