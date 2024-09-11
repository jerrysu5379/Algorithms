def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# def main():
#     n = int(input())
#     print(fibonacci(n))



def fibonacci_remaster(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

def fibonacci_remaster_list(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = [0, 1]
        for _ in range(2, n+1):
            result.append(result[-1] + result[-2])
        return result

def main():
    n = int(input())
    print(fibonacci_remaster_list(n))

if __name__ == "__main__":
    main()