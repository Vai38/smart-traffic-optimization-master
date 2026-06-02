import heapq

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')]*cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]

    pq = [(dist[start[0]][start[1]], start)]
    parent = {}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while pq:
        cost, (x,y) = heapq.heappop(pq)

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0<=nx<rows and 0<=ny<cols:
                new_cost = cost + grid[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    parent[(nx,ny)] = (x,y)
                    heapq.heappush(pq, (new_cost,(nx,ny)))

    # reconstruct path
    path = []
    cur = end
    while cur in parent:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()

    return path