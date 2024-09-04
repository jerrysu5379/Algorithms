def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def main():
    arr = [int(x) for x in input().split()]
    x = int(input())
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

if __name__ == "__main__":
    main()