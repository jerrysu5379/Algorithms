def second_big(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

def main():
    arr = list(map(int, input().split()))
    print(second_big(arr))

if __name__ == "__main__":
    main()