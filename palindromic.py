def partition(s):
    res = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                backtrack(end, path + [sub])

    backtrack(0, [])
    return res

# Test
s = "aab"
print(partition(s))

        