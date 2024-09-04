def linearSearch(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i
    return "Not found"

def main():
    A = [int(x) for x in input().split()]
    n = len(A)
    x = int(input())
    print(linearSearch(A, n, x))

if __name__ == "__main__":
    main()