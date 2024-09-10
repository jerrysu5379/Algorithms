def calculate(expression):
    try:
        num_stack = []
        op_stack = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] in '+-*/':
                op_stack.append(expression[i])
                i += 1
            elif expression[i].isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                num_stack.append(int(expression[i:j]))
                i = j
            else:
                return "Invalid expression"
        while op_stack:
            op = op_stack.pop()
            if op == '+':
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif op == '-':
                num_stack.append(-num_stack.pop() + num_stack.pop())
            elif op == '*':
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif op == '/':
                num_stack.append(1 / num_stack.pop() * num_stack.pop())
        return num_stack[0]
    except ZeroDivisionError:
        return "Division by zero"
    except IndexError:
        return "Invalid expression"


def main():
    expression = input()
    print(calculate(expression))

if __name__ == "__main__":
    main()