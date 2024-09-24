def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if not arr:
        return []
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if len(arr) < 4:
        return bubble_sort(left) + middle + bubble_sort(right)
    else:
        return quick_sort(left) + middle + quick_sort(right)

def main():
    arr = list(map(int, input().split()))
    print(quick_sort(arr))

if __name__ == "__main__":
    main()