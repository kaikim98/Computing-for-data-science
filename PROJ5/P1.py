def P1(room):
    a = len(room)
    b = len(room[0])
    L2 = []
    for i in range(a):
            for j in range(b):
                if room[i][j] == 0:
                    L2.append([i,j])
    count = 0
    change = True
    # for i in L2:
    #     if 
        
    while change:
        L3 = []
        for i in range(a):
            j = list(filter(lambda x: room[i][x] == 1, range(b)))
            for u in j:
                L3.append([i,j])
        if len(L3) == 0:
            change = False
        for i in range(len(room)):
            for j in range(len(room[0])):
                try:
                    if room[i][j] == 1 and room[i][j+1] != None:
                        if room[i][j+1] ==0:
                            room[i][j+1] = 1
                    if room[i][j] == 1 and room[i][j-1]!= None:
                        if room[i][j-1] == 0:
                            room[i][j-1] = 1
                    if room[i][j] == 1 and room[i+1][j]!= None:
                        if room[i+1][j] ==0:
                            room[i+1][j] = 1
                    if room[i][j] == 1 and room[i-1][j]!= None:
                        if room[i-1][j] ==0:
                            room[i-1][j] = 1
                    else:
                        continue
                except:
                    continue
        count = count + 1
                    # L1.append([i,j])
        # for i in L1:
        #     if room[i[0]+1, i[1]] == 0:
        #         room[i[0]+1, i[1]] = 1
        #     elif room[i[0], i[1]+1] == 0:
        #         room[i[0], i[1]+1] =1
        #     elif room[i[0]-1, i[1]] == 0:
        #         room[i[0]-1, i[1]] = 1
        #     elif room[i[0], i[1]-1] == 0:
        #         room[i[0], i[1]-1] = 1
        #     else:
        #         continue
        #     count = count+1
            
        # L1 = []
        # L3 = []
    
    return count

P1([[-1, 1],
[1, -1]])

P1([[1,0]])

P1([[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,1]])

P1([[1,-1,0,0, 0,0],
[0,-1,0,0, 0,0],
[0, 0,0,0,-1,0],
[0, 0,0,0,-1,1]])

P1([[-1,1, 0, 0,0],
[0,-1,-1,-1,0],
[0,-1,-1,-1,0],
[0,-1,-1,-1,0],
[0, 0, 0, 0,0]])