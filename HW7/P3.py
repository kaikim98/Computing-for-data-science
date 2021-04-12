def P3(matrix):
    a = len(matrix) #vertical
    b = len(matrix[0]) #horizontal
    if a == 1:
        return matrix
    for i in range(a):
        for y in reversed(range(b)):
            for x in range(y):
                if i + x > a-2 or x>b-2:
                    break
                else:
                    if matrix[i+x][0+x] > matrix[i+x+1][x+1]:
                        matrix[i+x][0+x], matrix[i+x+1][x+1] = matrix[i+x+1][x+1], matrix[i+x][0+x]
                    else:
                        continue
    for i in range(b):
        for y in reversed(range(a)):
            for x in range(y):
                if x > a-2 or i+x>b-2:
                    break
                else:
                    if matrix[0+x][i+x] > matrix[0+x+1][i+x+1]:
                        matrix[0+x][i+x], matrix[0+x+1][i+x+1] = matrix[0+x+1][i+x+1], matrix[0+x][i+x]
                    else:
                        continue
        
    return matrix