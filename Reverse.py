def reverse(arr):
    return arr[::-1]

def main():
    arr = list(map(int, input().split()))
    print(reverse(arr))

if __name__ == "__main__":
    main()