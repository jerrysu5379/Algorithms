def locate(str, dest):
    start = dest.find(str)
    return start

def main():
    str = input()
    dest = input()
    print(locate(str, dest))

if __name__ == "__main__":
    main()