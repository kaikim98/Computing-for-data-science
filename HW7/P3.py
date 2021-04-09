def P3(matrix):
    a = len(matrix)
    b = len(matrix[0])
    if a == 1:
        return matrix
    # while True:
    #     for x in reversed(range(len(matrix))):
    #         for i in range(x):
    #             for n in range(x):
    #                 if i< a and n<b:
    #                     if matrix[i][n] > matrix[i+1][n+1]:
    #                         matrix[i][n], matrix[i+1][n+1] =matrix[i+1][n+1], matrix[i][n]
    for x in reversed(range(len(matrix))):
        for i in range(x):
            
    return matrix

P3([[1,3,0],[2,5,3],[3,4,1],[2,0,0]])
P3([[1,6,2,4,6,2,4,7,0]])
