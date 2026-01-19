def check_brackets(s):
    stack = []
    for c in s:
        if c in "([":
            stack.append(c)
        elif c in ")]" and stack[-1] in "([":
            stack.pop()
    return not stack
            
print(check_brackets("(([]()"))