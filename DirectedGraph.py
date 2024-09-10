def create_graph():
    for i in range(10):
        for j in range(10):
            graph[i][j] = 0
    n = int(input())
    for _ in range(n):
        u, v = map(int, input().split())
        graph[u][v] = 1

def dijkstra(source):
    for i in range(10):
        shortest[i] = 0x3f3f3f3f
        pred[i] = -1
    shortest[source] = 0
    vis = [0] * 10
    for _ in range(10):
        u = -1
        for i in range(10):
            if not vis[i] and (u == -1 or shortest[i] < shortest[u]):
                u = i
        vis[u] = 1
        for v in range(10):
            if graph[u][v] and shortest[u] + graph[u][v] < shortest[v]:
                shortest[v] = shortest[u] + graph[u][v]
                pred[v] = u

def show_shortest_path(source):
    for i in range(10):
        if i == source:
            continue
        print('The shortest path from {} to {} is:'.format(source, i))
        path = []
        while i != -1:
            path.append(i)
            i = pred[i]
        path.reverse()
        print(path)
        print('The length is:', shortest[path[-1]])
        print()

def main():
    create_graph()
    source = int(input())
    dijkstra(source)
    show_shortest_path(source)

if __name__ == "__main__":
    graph = [[0] * 10 for _ in range(10)]
    shortest = [0] * 10
    pred = [0] * 10
    main()