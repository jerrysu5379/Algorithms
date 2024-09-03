def linearSearch(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i
    return "Not found"

def main():
    A = [1, 2, 3, 4, 5]
    n = len(A)
    x = 3
    print(linearSearch(A, n, x))

if __name__ == "__main__":
    main()