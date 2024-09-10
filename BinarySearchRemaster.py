def rec_bi_search(key, arr, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return rec_bi_search(key, arr, low, mid-1)
        else:
            return rec_bi_search(key, arr, mid+1, high)
    else:
        return -1

def main():
    arr = list(map(int, input().split()))
    key = int(input())
    print(rec_bi_search(key, arr, 0, len(arr)-1))

if __name__ == "__main__":
    main()