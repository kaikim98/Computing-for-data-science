def P3(matrix):
    a = len(matrix) #vertical
    b = len(matrix[0]) #horizontal
    if a == 1:
        return matrix
    # while True:
    #     for x in reversed(range(len(matrix))):
    #         for i in range(x):
    #             for n in range(x):
    #                 if i< a and n<b:
    #                     if matrix[i][n] > matrix[i+1][n+1]:
    #                         matrix[i][n], matrix[i+1][n+1] =matrix[i+1][n+1], matrix[i][n]
    for i in range(a):
        x = 0
        for y in range(b):
            while x + i+y < a-2:
                if matrix[i+x+y][0+x+y] > matrix[i+x+y+1][x+y+1]:
                    matrix[i+x+y][0+x+y], matrix[i+x+y+1][x+y+1] = matrix[i+x+y+1][x+y+1], matrix[i+x+y][0+x+y]
                    x = x+1
                else:
                    x = x+1
    for i in range(b):
        x = 0
        for y in range(a):
            while x+i < b-2:
                if matrix[0+x+y][i+x+y] > matrix[0+x+y+1][i+x+y+1]:
                    matrix[0+x+y][i+x+y], matrix[0+x+y+1][i+x+y+1] = matrix[0+x+y+1][i+x+y+1], matrix[0+x+y][i+x+y]
                    x = x+1
                else:
                    x = x+1
        
    return matrix

P3([[1,5,20,-1,3],[-1,3,20,4,-1],[34,3,12,5,-12],[4,64,612,6,10]])
P3([[1,3,0],[2,5,3],[3,4,1],[2,0,0]])
P3([[1,6,2,4,6,2,4,7,0]])
