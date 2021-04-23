def P3(world):
    a = len(world)
    b = len(world[0])
    island_list = []
    count = 0
    for i in range(a):
        for j in range(b):
            if world[i][j] == 1:
                world[i][j] = 0
                island_list.append([i, j])
                count = count + 1
                while island_list:
                    x, y = island_list.pop(0)
                    if x>=1:
                        if world[x-1][y] == 1:
                            world[x-1][y] = 0
                            island_list.append([x-1, y])
                            
                    if x<a-1:
                        if world[x+1][y] == 1:
                            world[x+1][y] = 0
                            island_list.append([x+1, y])
                            
                    if y>=1:
                        if world[x][y-1] == 1:
                            world[x][y-1] = 0
                            island_list.append([x, y-1])

                    if y<b-1:
                        if world[x][y+1] == 1:
                            world[x][y+1] = 0
                            island_list.append([x, y+1])
    return count