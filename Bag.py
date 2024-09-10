def bag( ball, n, w):
    dp = [0] * (w + 1)
    for i in range(1, n + 1):
        for j in range(w, ball[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - ball[i]] + ball[i])
    return dp[w]

def main():
    n, w = map(int, input().split())
    ball = [0] + list(map(int, input().split()))
    print(bag(ball, n, w))

if __name__ == "__main__":
    main()