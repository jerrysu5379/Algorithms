def hashSearch(arr, x):
    hash_table = {}
    for i, element in enumerate(arr):
        hash_table[element] = i
    if x in hash_table:
        return hash_table[x]
    return "Not found"

def main():
    arr = [int(x) for x in input().split()]
    x = int(input())
    print(hashSearch(arr, x))

if __name__ == "__main__":
    main()