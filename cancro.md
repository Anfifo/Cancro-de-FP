# Cancro-de-FP
    output = [[0]*len(m1)]*len(m2)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1)):    
                output[i][j] += m1[i][k] * m2[k][j]
    return output

print(mult_matriz([[2,3,6],[-1,0,1]],[[2,-3],[0,1],[4,-7]]))
