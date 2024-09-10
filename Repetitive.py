def if_repetitive(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def main():
    arr = list(map(int, input().split()))
    print(if_repetitive(arr))

if __name__ == "__main__":
    main()