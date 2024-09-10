def brackets_match(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack:
                return False
            if c == ')' and stack[-1] == '(' or \
               c == ']' and stack[-1] == '[' or \
               c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return not stack

def main():
    s = input()
    print(brackets_match(s))

if __name__ == "__main__":
    main()