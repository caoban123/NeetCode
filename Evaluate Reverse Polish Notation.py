tokens = ["1","2","+","3","*","4","-"]

stack1 = []
stack2 = []

for i in tokens:
    if i.isalnum():
        stack1.append(int(i))
    else:
        x = stack1.pop()
        y = stack1.pop()
        if i == "+":
            stack1.append(x + y)
        elif i == "-":
            stack1.append(y - x)
        elif i == "*":
            stack1.append(x * y)
        else:
            stack1.append(y / x)
print(stack1)

