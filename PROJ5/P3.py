def P3(world):
    import collections
    # for i in world:
    #     if 0 not in i:
    #         return 1
    #     if 1 not in i:
    #         return 0
    m = len(world)
    n = len(world[0])
    dq = collections.deque()
    islands = 0
    for i in range(m):
        for j in range(n):
            if world[i][j] == 1:  # run bfs
                islands += 1
                dq.append([i, j])
                world[i][j] = -1
                while dq:
                    x, y = dq.popleft()
                    if x - 1 >= 0:
                        if world[x - 1][y] == 1:
                            world[x - 1][y] = -1
                            dq.append([x - 1, y])

                    if y - 1 >= 0:
                        if world[x][y - 1] == 1:
                            world[x][y - 1] = -1
                            dq.append([x, y - 1])

                    if x + 1 < m:
                        if world[x + 1][y] == 1:
                            world[x + 1][y] = -1
                            dq.append([x + 1, y])

                    if y + 1 < n:
                        if world[x][y + 1] == 1:
                            world[x][y + 1] = -1
                            dq.append([x, y + 1])
    return islands

P3([[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]])

P3([[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]])

P3([[1,0,0,0,1],
[1,1,0,0,0],
[0,0,0,1,1],
[0,1,0,1,0]])