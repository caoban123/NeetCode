digits = "34"

lst = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
res = []

def backtrack(index, strcur):
    if len(strcur) == len(digits):
        res.append(strcur)
        return
    for c in lst[int(digits[index])]:
        backtrack(index + 1, strcur + c)
    
backtrack(0, "")
print(res)