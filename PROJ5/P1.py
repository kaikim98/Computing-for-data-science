def P1(room):
    a = len(room)
    b = len(room[0])
    L1 = []
    count = 0
    for i in range(a):
            for j in range(b):
                if room[i][j] == 0:
                    L1.append([i,j])
                    while L1:
                        x, y = L1.pop(0)
                        if x>=1:
                            if room[x-1][y] == 0:
                                room[x-1][y] = 1
                                L1.append([x-1, y])
                                
                        if x<a-1:
                            if room[x+1][y] == 0:
                                room[x+1][y] = 1
                                L1.append([x+1, y])
                                
                        if y>=1:
                            if room[x][y-1] == 0:
                                room[x][y-1] = 1
                                L1.append([x, y-1])
    
                        if y<b-1:
                            if room[x][y+1] == 0:
                                room[x][y+1] = 1
                                L1.append([x, y+1])
                        count = count +1
    x = int(count/3)
    return x