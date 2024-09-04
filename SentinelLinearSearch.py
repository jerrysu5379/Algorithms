def sentinelLinearSearch(A, n, x):
    last = A[n - 1]
    A[n - 1] = x
    i = 0
    while A[i] != x:
        i += 1
    A[n - 1] = last
    if i < n - 1 or A[n - 1] == x:
        return i
    return "Not found"

def main():
    A = [int(x) for x in input().split()]
    n = len(A)
    x = int(input())
    print(sentinelLinearSearch(A, n, x))

if __name__ == "__main__":
    main()