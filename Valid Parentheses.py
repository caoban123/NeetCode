s = "[]"


stack = []
dic = {"]":"[", ")" : "(", "}" : "{"}
for i in s:
    if i == "[" or i == "(" or i == "{":
        stack.append(i)
    else:
        close = stack.pop()
        if dic[i] != close:
            return False
return True