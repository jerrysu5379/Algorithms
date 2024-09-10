class Graph:
    def __init__(self, n):
        self.n = n
        self.e = [[0] * n for _ in range(n)]
        self.vis = [0] * n
        self.path = []
        self.ans = 0

    def add_edge(self, u, v):
        self.e[u][v] = self.e[v][u] = 1

    def dfs(self, u, v):
        self.vis[u] = 1
        self.path.append(u)
        if u == v:
            self.ans += 1
            print(self.path)
        else:
            for i in range(self.n):
                if self.e[u][i] and not self.vis[i]:
                    self.dfs(i, v)
        self.vis[u] = 0
        self.path.pop()

def main():
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    g.dfs(0, n - 1)
    print(g.ans)

if __name__ == "__main__":
    main()
