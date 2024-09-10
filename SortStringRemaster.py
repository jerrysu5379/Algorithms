from SortString import sort_str

def main():
    n = int(input())
    for _ in range(n):
        str = input()
        print(sort_str(str))

if __name__ == "__main__":
    main()