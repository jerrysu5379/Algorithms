# 7 在2行5列的格子中填入1到10的数字。要求：相邻的格子中的数，右边的大于左边的，下边的大于上边的。请你计算一共有多少种可能的方案，并输出所有的方案。

def dfs(x, y, num):
    global ans
    if x == 3 and y == 5:
        ans += 1
        if ans <= 20:
            for i in range(1, 4):
                for j in range(1, 6):
                    print(num[i][j], end=' ')
                print()
            print()
        return
    if y == 5:
        dfs(x + 1, 1, num)
        return
    for i in range(1, 11):
        if i > num[x][y - 1] and i > num[x - 1][y]:
            num[x][y] = i
            dfs(x, y + 1, num)
            num[x][y] = 0

def main():
    num = [[0] * 6 for _ in range(4)]
    dfs(1, 1, num)
    print(ans)

if __name__ == "__main__":
    ans = 0
    main()